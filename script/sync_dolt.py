"""
通过 DoltHub HTTP SQL API 双向同步 CSV（云端 ↔ 本地）。

- **pull** = 云端 → 本地（``pull <表名>`` / ``pull_all`` / ``pull_backtest_*`` 等）
- **push** = 本地 → 云端（``push`` / ``push_*``；合并 ``backtest_csv`` / ``review_csv`` / ``qlib_score_csv`` 用 ``push_backtest_*`` / ``push_review_*`` / ``push_qlib_score_*``；**qlib_score 目录合并上传时默认不提交 ``name`` 列**；backtest 文件名**开头数字**为 ``top_k``）
- 读（云端 → 本地）: pull（分页 SELECT）
- 写（本地 → 云端）: push（Write API：临时分支 DELETE + INSERT，再空 POST merge 回 main；DoltHub 写 API **不支持** ``SET NAMES``/多语句；``merge_message`` 仅打印到终端；默认按云端 DESCRIBE 列对齐，本地多出的列不提交）
- 盘点: inspect（默认详细：DESCRIBE / 行数 / 时间范围 / 样本）；inspect_table 单表；--brief 仅一行汇总

文档:
  https://docs.dolthub.com/products/dolthub/api/sql

环境变量:
  DOLT_TOKEN       读公开库可选；写入云端必填
  DOLT_REF         读数据所用分支，默认 main
  DOLT_OUT_DIR     pull/push 默认 CSV 目录，默认 ./dolt_export
  DOLT_PUSH_FROM_BRANCH  push 时基于哪个分支开临时分支，默认与 DOLT_REF 一致
  REVIEW_CSV_DIR         覆盖 review 目录；未设置时固定为「项目根目录/review_csv」
  QLIB_SCORE_CSV_DIR     覆盖 qlib_score_csv；未设置时固定为「项目根目录/qlib_score_csv」；push_qlib_score_* 递归子目录
  BACKTEST_CSV_DIR       覆盖 backtest_csv；未设置时固定为「项目根目录/backtest_csv」；push_backtest_* 仅一层目录
"""
from __future__ import annotations

import os
import re
import sys
import tempfile
from datetime import datetime
from pathlib import Path
import time
import uuid
import json
from typing import Any, Callable

import fire
import numpy as np
import pandas as pd
import requests

# 默认仓库（可被 Fire 顶层参数覆盖）
OWNER = "touhoufan"
DATABASE = "qlibDailyCsv"
REF = os.getenv("DOLT_REF", "main").strip() or "main"
TOKEN = os.getenv("DOLT_TOKEN")

API_ROOT = "https://www.dolthub.com/api/v1alpha1"

# 业务约定的 6 张表（与盘点结果一致）
EXPORT_TABLES = (
    "backtest_filter_ret",
    "backtest_ret",
    "qlib_score_filter_ret",
    "qlib_score_ret",
    "review_filter_ret",
    "review_ret",
)

# push_qlib_score_*（目录合并）递归扫描时跳过的文件名（小写比较）
QLIB_SCORE_EXCLUDED_CSV_BASENAMES: frozenset[str] = frozenset({"total.csv"})


def _default_out_dir() -> str:
    return os.getenv("DOLT_OUT_DIR", "dolt_export").strip() or "dolt_export"


def _push_from_branch() -> str:
    return os.getenv("DOLT_PUSH_FROM_BRANCH", REF).strip() or "main"


def _sql_url() -> str:
    return f"{API_ROOT}/{OWNER}/{DATABASE}/{REF}"


class DoltHubSqlError(RuntimeError):
    """DoltHub SQL API 返回非成功状态。"""


def dolt_sql(query: str) -> dict[str, Any]:
    """执行只读 SQL，返回 DoltHub JSON 体。失败则抛出异常。"""
    headers: dict[str, str] = {}
    if TOKEN:
        headers["Authorization"] = f"token {TOKEN}"

    resp = requests.get(
        _sql_url(),
        params={"q": query},
        headers=headers,
        timeout=300,
    )
    try:
        data = resp.json()
    except Exception as e:  # noqa: BLE001
        raise DoltHubSqlError(f"响应不是合法 JSON: {e}\n{resp.text[:500]}") from e

    if resp.status_code != 200:
        raise DoltHubSqlError(f"HTTP {resp.status_code}: {data}")

    status = data.get("query_execution_status")
    if status not in ("Success", "RowLimit"):
        msg = data.get("query_execution_message", status)
        q = data.get("sql_query", query)
        raise DoltHubSqlError(f"SQL 执行失败: {status} — {msg}\n  查询: {q}")

    return data


def _auth_headers_write() -> dict[str, str]:
    if not TOKEN:
        raise DoltHubSqlError("写入 DoltHub 必须设置环境变量 DOLT_TOKEN")
    return {"Authorization": f"token {TOKEN}"}


def _poll_write_operation(operation_name: str, headers: dict[str, str]) -> dict[str, Any]:
    """轮询异步写操作直到完成。"""
    url = f"{API_ROOT}/{OWNER}/{DATABASE}/write"
    last: dict[str, Any] = {}
    for _ in range(900):  # 最多约 30 分钟
        resp = requests.get(
            url,
            params={"operationName": operation_name},
            headers=headers,
            timeout=120,
        )
        try:
            last = resp.json()
        except Exception as e:  # noqa: BLE001
            raise DoltHubSqlError(f"轮询返回非 JSON: {e}\n{resp.text[:500]}") from e
        if resp.status_code != 200:
            raise DoltHubSqlError(f"轮询 HTTP {resp.status_code}: {last}")
        if last.get("done"):
            rd = last.get("res_details") or {}
            qes = rd.get("query_execution_status", "")
            if qes and "Success" not in str(qes) and "OK" not in str(qes):
                raise DoltHubSqlError(f"异步写入失败: {rd}")
            return last
        time.sleep(2)
    raise DoltHubSqlError("异步写入轮询超时")


def dolt_sql_write(
    query: str,
    from_branch: str,
    to_branch: str,
    *,
    poll: bool = True,
) -> dict[str, Any]:
    """
    发起异步写 SQL（POST /write/{from}/{to}）。
    返回 poll 后的最终 JSON（若 poll=True）。
    """
    headers = _auth_headers_write()
    url = f"{API_ROOT}/{OWNER}/{DATABASE}/write/{from_branch}/{to_branch}"
    if len(query) > 8000:
        resp = requests.post(url, json={"query": query}, headers=headers, timeout=600)
    else:
        resp = requests.post(url, params={"q": query}, headers=headers, timeout=600)
    try:
        data = resp.json()
    except Exception as e:  # noqa: BLE001
        raise DoltHubSqlError(f"写入响应非 JSON: {e}\n{resp.text[:800]}") from e
    if resp.status_code != 200:
        raise DoltHubSqlError(f"写入 HTTP {resp.status_code}: {data}")
    if data.get("query_execution_status") != "Success":
        raise DoltHubSqlError(f"未创建写入任务: {data}")
    op = data.get("operation_name")
    if not op:
        raise DoltHubSqlError(f"响应缺少 operation_name: {data}")
    if not poll:
        return data
    return _poll_write_operation(op, headers)


def _dolt_merge_branches_empty_post(feature_branch: str, into_branch: str) -> dict[str, Any]:
    """将 feature_branch 合并进 into_branch（POST /write/{feature}/{into} 空 body）。"""
    headers = _auth_headers_write()
    url = f"{API_ROOT}/{OWNER}/{DATABASE}/write/{feature_branch}/{into_branch}"
    resp = requests.post(url, headers=headers, timeout=600)
    try:
        data = resp.json()
    except Exception as e:  # noqa: BLE001
        raise DoltHubSqlError(f"merge 响应非 JSON: {e}\n{resp.text[:800]}") from e
    if resp.status_code != 200:
        raise DoltHubSqlError(f"merge HTTP {resp.status_code}: {data}")
    if data.get("query_execution_status") != "Success":
        raise DoltHubSqlError(f"merge 未创建任务: {data}")
    op = data.get("operation_name")
    if not op:
        raise DoltHubSqlError(f"merge 缺少 operation_name: {data}")
    return _poll_write_operation(op, headers)


def dolt_merge_branches(
    feature_branch: str,
    into_branch: str,
    *,
    message: str | None = None,
) -> dict[str, Any]:
    """
    将 feature_branch 合并进 into_branch。

    DoltHub HTTP 写 API **仅支持**空 POST merge（官方示例），**不支持**在此执行
    ``CALL DOLT_MERGE(..., '-m', ...)``，会报 ``Unsupported SQL statement``。

    若传入 ``message``，仅在**终端打印**作本地日志，**不会**写入 Dolt 上的 merge commit。
    """
    msg = (message or "").strip()
    if msg:
        if len(msg) > 500:
            msg = msg[:497] + "..."
        print(
            "ℹ️  merge 说明（仅终端日志；DoltHub API 无法在 merge 上写入自定义 commit）："
            f" {msg}",
        )
    return _dolt_merge_branches_empty_post(feature_branch, into_branch)


def _default_merge_commit_message(table: str, csv_path: str, n_rows: int) -> str:
    """push 合并步骤在终端打印的简短说明（DoltHub 无法写入为 merge commit）。"""
    base = os.path.basename(csv_path)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"sync {table} ({n_rows} rows) from {base} @ {ts}"


def _sql_ident(name: str) -> str:
    return f"`{name.replace('`', '``')}`"


def _sql_literal(val: Any) -> str:
    if val is None:
        return "NULL"
    if isinstance(val, (pd.Timestamp,)):
        return "'" + str(val).replace("'", "''") + "'"
    # 避免 bool 被当成 int（Python 里 bool 是 int 子类）
    if isinstance(val, (bool, np.bool_)):
        return "1" if bool(val) else "0"
    if isinstance(val, (int, np.integer)):
        return str(int(val))
    if isinstance(val, (float, np.floating)):
        if pd.isna(val) or np.isnan(val):
            return "NULL"
        return repr(float(val))
    if isinstance(val, str):
        return "'" + val.replace("'", "''") + "'"
    if pd.isna(val):
        return "NULL"
    s = str(val)
    return "'" + s.replace("'", "''") + "'"


def _dataframe_omit_name_column(df: pd.DataFrame) -> pd.DataFrame:
    """去掉列名（大小写不敏感）为 ``name`` 的列，用于 qlib_score 推送时避免中文 name 触发 DoltHub 写入问题。"""
    drop_cols = [c for c in df.columns if str(c).lower() == "name"]
    if not drop_cols:
        return df
    print("ℹ️  qlib_score 推送：已去掉列 name，INSERT 不包含该列。")
    return df.drop(columns=drop_cols)


def _insert_batch_sql(table: str, df: pd.DataFrame, start: int, end: int) -> str:
    safe_t = _sql_ident(table)
    cols = [_sql_ident(c) for c in df.columns]
    col_list = ", ".join(cols)
    parts: list[str] = []
    for i in range(start, min(end, len(df))):
        row = df.iloc[i]
        vals = ", ".join(_sql_literal(row[c]) for c in df.columns)
        parts.append(f"({vals})")
    return f"INSERT INTO {safe_t} ({col_list}) VALUES " + ", ".join(parts)


def push_table_from_csv(
    table: str,
    csv_path: str,
    *,
    from_branch: str | None = None,
    to_branch: str | None = None,
    merge: bool = True,
    insert_batch_rows: int = 80,
    match_dolt_columns: bool = True,
    merge_message: str | None = None,
    omit_name_column: bool = False,
) -> None:
    """
    本地 CSV → 云端：在临时分支上清空表并插入 CSV 数据，可选合并回 from_branch（通常 main）。

    说明: DoltHub 写 API 在「分支」上执行；默认从 DOLT_PUSH_FROM_BRANCH（默认同 DOLT_REF）
    拉出临时分支，写完再 merge 回去。

    match_dolt_columns=True（默认）: 先 DESCRIBE 读云端列名，只 INSERT 这些列；
    本地 CSV 多出的列会忽略；云端有而本地缺的列填 NULL。

    merge_message: 合并时在**终端**打印的说明；未传时自动生成。DoltHub API 不会将其写入 merge commit。

    omit_name_column: 为 True 时在列对齐后去掉 ``name`` 列（``push_qlib_score_*`` 目录合并上传默认开启）。
    """
    fb = from_branch or _push_from_branch()
    tb = to_branch or f"dolt-csv-{uuid.uuid4().hex[:12]}"

    if not os.path.isfile(csv_path):
        raise DoltHubSqlError(f"本地文件不存在: {csv_path}")

    df = pd.read_csv(csv_path, encoding="utf-8")
    df.columns = [str(c).strip() for c in df.columns]
    safe = table.replace("`", "``")

    if match_dolt_columns:
        dolt_cols = fetch_dolt_table_columns(table)
        overlap = [c for c in dolt_cols if c in df.columns]
        if len(df) > 0 and not overlap:
            raise DoltHubSqlError(
                "本地 CSV 与 Dolt 表列名无交集，无法提交（请检查列名是否与云端一致）",
            )
        df = align_dataframe_to_dolt_columns(df, dolt_cols)

    if omit_name_column:
        df = _dataframe_omit_name_column(df)

    print(f"📤 写入分支 `{tb}`（基于 `{fb}`），目标表 `{table}`，共 {len(df)} 行，列 {list(df.columns)} …")

    # 1) 清空表（在临时分支上）
    dolt_sql_write(f"DELETE FROM `{safe}`", fb, tb)

    # 2) 分批 INSERT
    if len(df) == 0:
        print("ℹ️  CSV 无数据行，跳过 INSERT。")
    else:
        n = len(df)
        step = max(1, insert_batch_rows)
        for start in range(0, n, step):
            end = min(start + step, n)
            q = _insert_batch_sql(table, df, start, end)
            dolt_sql_write(q, fb, tb)
            print(f"   … 已插入 {end}/{n} 行")

    # 3) 合并回主线（说明仅终端日志，见 dolt_merge_branches）
    if merge:
        mmsg = (merge_message or "").strip() or _default_merge_commit_message(
            table,
            csv_path,
            len(df),
        )
        print(f"🔀 将 `{tb}` 合并进 `{fb}` …")
        dolt_merge_branches(tb, fb, message=mmsg)
        print(f"✅ 已合并到 `{fb}`，表 `{table}` 与本地 `{csv_path}` 对齐。")
    else:
        print(f"✅ 数据已写在分支 `{tb}`，未合并（请自行在 DoltHub 上 merge）。")


def _project_root() -> str:
    """本文件在 ``script/sync_dolt.py``，项目根目录为其父级的父级。"""
    return str(Path(__file__).resolve().parent.parent)


def _default_review_csv_dir() -> str:
    """
    默认 ``<项目根>/review_csv``，不随当前工作目录变化。
    若设置 ``REVIEW_CSV_DIR``，则使用该路径（相对路径按当前工作目录解析）。
    """
    env = (os.getenv("REVIEW_CSV_DIR") or "").strip()
    if env:
        return os.path.abspath(env)
    return os.path.join(_project_root(), "review_csv")


def _default_qlib_score_csv_dir() -> str:
    """
    默认 ``<项目根>/qlib_score_csv``。
    若设置 ``QLIB_SCORE_CSV_DIR``，则使用该路径（相对路径按当前工作目录解析）。
    """
    env = (os.getenv("QLIB_SCORE_CSV_DIR") or "").strip()
    if env:
        return os.path.abspath(env)
    return os.path.join(_project_root(), "qlib_score_csv")


def _default_backtest_csv_dir() -> str:
    """
    默认 ``<项目根>/backtest_csv``。
    若设置 ``BACKTEST_CSV_DIR``，则使用该路径（相对路径按当前工作目录解析）。
    """
    env = (os.getenv("BACKTEST_CSV_DIR") or "").strip()
    if env:
        return os.path.abspath(env)
    return os.path.join(_project_root(), "backtest_csv")


def _top_k_from_backtest_basename(basename: str) -> int:
    """从文件名解析 ``top_k``：须以数字开头（如 ``10_ret.csv`` → 10，``100_filter_ret.csv`` → 100）。"""
    m = re.match(r"^(\d+)", basename)
    if not m:
        raise DoltHubSqlError(
            f"backtest CSV 文件名须以数字开头表示 top_k：{basename!r}",
        )
    return int(m.group(1))


def _csv_matches_name_filter(filename: str, *, name_contains_filter: bool) -> bool:
    low = filename.lower()
    has_filter = "filter" in low
    if name_contains_filter:
        return has_filter
    return not has_filter


def _collect_csv_paths_by_name_filter(
    root: str,
    *,
    name_contains_filter: bool,
    recursive: bool,
) -> list[str]:
    """
    在 ``root`` 下收集 .csv（文件名含/不含 ``filter`` 规则同 review）。

    - ``recursive=False``：仅 ``root`` 一层，不进入子目录
    - ``recursive=True``：``os.walk`` 全遍历子目录
    """
    if not os.path.isdir(root):
        raise DoltHubSqlError(f"目录不存在: {root}")
    paths: list[str] = []
    if recursive:
        for dirpath, _dirnames, filenames in os.walk(root):
            for fn in filenames:
                if not fn.endswith(".csv"):
                    continue
                if not _csv_matches_name_filter(fn, name_contains_filter=name_contains_filter):
                    continue
                paths.append(os.path.join(dirpath, fn))
    else:
        for fn in sorted(os.listdir(root)):
            if not fn.endswith(".csv"):
                continue
            if not _csv_matches_name_filter(fn, name_contains_filter=name_contains_filter):
                continue
            paths.append(os.path.join(root, fn))
    return sorted(paths)


def _read_review_csv_normalized(path: str) -> pd.DataFrame:
    """读取 review 导出的 CSV，去掉首列无名列（Unnamed: 0）。"""
    df = pd.read_csv(path, encoding="utf-8")
    df.columns = [str(c).strip() for c in df.columns]
    if len(df.columns) and (
        str(df.columns[0]).startswith("Unnamed") or df.columns[0] == ""
    ):
        df = df.drop(columns=[df.columns[0]])
    return df


def _review_date_column_name(df: pd.DataFrame) -> str | None:
    """优先 ``datetime`` 列，否则第一个列名含 ``date`` 的列。"""
    for c in df.columns:
        if str(c).lower() == "datetime":
            return str(c)
    for c in df.columns:
        if "date" in str(c).lower():
            return str(c)
    return None


def _sort_merged_review_by_date_only(df: pd.DataFrame) -> pd.DataFrame:
    """
    仅按日期/时间列排序；``kind=mergesort`` 为稳定排序，同一日期（或同一时刻）内
    保持各 CSV 原先行顺序，不会按 instrument 等再排。
    """
    dt_col = _review_date_column_name(df)
    if dt_col is None:
        return df
    return df.sort_values(
        by=dt_col,
        kind="mergesort",
        na_position="last",
        key=lambda s: pd.to_datetime(s, errors="coerce"),
    )


def _merge_review_csvs_to_tempfile(paths: list[str]) -> tuple[str, int]:
    """合并多个 CSV 到临时文件，返回 (路径, 行数)。"""
    dfs = [_read_review_csv_normalized(p) for p in paths]
    merged = pd.concat(dfs, ignore_index=True)
    merged = _sort_merged_review_by_date_only(merged)
    n = len(merged)
    fd, tmp_path = tempfile.mkstemp(suffix=".csv", prefix="review_merge_")
    os.close(fd)
    merged.to_csv(tmp_path, index=False, encoding="utf-8")
    return tmp_path, n


def _read_backtest_csv_normalized(path: str) -> pd.DataFrame:
    """
    读取 backtest 导出的 CSV；若仅有 ``date`` 列则改名为 ``datetime`` 以便与 Dolt 表对齐；
    根据**文件名开头数字**写入列 ``top_k``（若 CSV 内已有 ``top_k`` 则覆盖为文件名值）。
    """
    df = _read_review_csv_normalized(path)
    if "datetime" not in df.columns and "date" in df.columns:
        df = df.rename(columns={"date": "datetime"})
    bn = os.path.basename(path)
    top_k = _top_k_from_backtest_basename(bn)
    drop_tk = [c for c in df.columns if str(c).lower() == "top_k"]
    if drop_tk:
        df = df.drop(columns=drop_tk)
    df["top_k"] = top_k
    return df


def _merge_backtest_csvs_to_tempfile(paths: list[str]) -> tuple[str, int]:
    """合并多个 backtest CSV（带 top_k）到临时文件，返回 (路径, 行数)。"""
    dfs = [_read_backtest_csv_normalized(p) for p in paths]
    merged = pd.concat(dfs, ignore_index=True)
    merged = _sort_merged_review_by_date_only(merged)
    n = len(merged)
    fd, tmp_path = tempfile.mkstemp(suffix=".csv", prefix="backtest_merge_")
    os.close(fd)
    merged.to_csv(tmp_path, index=False, encoding="utf-8")
    return tmp_path, n


def push_merged_backtest_csvs_to_table(
    table: str,
    paths: list[str],
    *,
    label: str,
    from_branch: str | None = None,
    to_branch: str | None = None,
    merge: bool = True,
    insert_batch_rows: int = 80,
    match_dolt_columns: bool = True,
) -> None:
    """将多个 backtest CSV 合并后 push 到指定 Dolt 表（整表覆盖，逻辑同 push_table_from_csv）。"""
    if not paths:
        raise DoltHubSqlError(f"{label}: 没有匹配的 CSV 文件")
    tmp, n = _merge_backtest_csvs_to_tempfile(paths)
    try:
        print(
            f"📎 {label}: 合并 {len(paths)} 个文件 → 临时表 {n} 行，目标 Dolt 表 `{table}`",
        )
        ts = datetime.now().strftime("%Y-%m-%d %H:%M")
        merged_msg = f"sync {table} ({n} rows, {len(paths)} files) @ {ts}"
        push_table_from_csv(
            table,
            tmp,
            from_branch=from_branch,
            to_branch=to_branch,
            merge=merge,
            insert_batch_rows=insert_batch_rows,
            match_dolt_columns=match_dolt_columns,
            merge_message=merged_msg,
            omit_name_column=False,
        )
    finally:
        try:
            os.unlink(tmp)
        except OSError:
            pass


def push_backtest_csvs_by_name_rule(
    table: str,
    *,
    name_contains_filter: bool,
    backtest_dir: str | None = None,
    path: str | None = None,
    from_branch: str | None = None,
    to_branch: str | None = None,
    merge: bool = True,
    insert_batch_rows: int = 80,
    match_dolt_columns: bool = True,
) -> None:
    """
    合并 ``backtest_csv`` 目录下符合文件名规则的 CSV，push 到 ``table``。

    - 文件名含 ``filter`` → ``backtest_filter_ret``；不含 → ``backtest_ret``
    - 文件名**须以数字开头**，该数字写入列 ``top_k``（如 ``10_ret.csv`` → ``top_k=10``）
    - 默认仅扫描目录一层（不递归子目录）
    """
    other = "push_backtest_filter_ret" if not name_contains_filter else "push_backtest_ret"
    if path:
        if not os.path.isfile(path):
            raise DoltHubSqlError(f"文件不存在: {path}")
        bn = os.path.basename(path).lower()
        has_f = "filter" in bn
        if name_contains_filter and not has_f:
            raise DoltHubSqlError(f"该文件名不含 filter，请改用 {other}")
        if not name_contains_filter and has_f:
            raise DoltHubSqlError(f"该文件名含 filter，请改用 {other}")
        paths = [path]
    else:
        root = backtest_dir or _default_backtest_csv_dir()
        paths = _collect_csv_paths_by_name_filter(
            root,
            name_contains_filter=name_contains_filter,
            recursive=False,
        )

    if not paths:
        raise DoltHubSqlError(
            "没有可提交的 backtest CSV（检查目录或 filter 规则）",
        )

    mode = "文件名含 filter" if name_contains_filter else "文件名不含 filter"
    push_merged_backtest_csvs_to_table(
        table,
        paths,
        label=f"{table}（{mode}）",
        from_branch=from_branch,
        to_branch=to_branch,
        merge=merge,
        insert_batch_rows=insert_batch_rows,
        match_dolt_columns=match_dolt_columns,
    )


def _run_backtest_push_cli(
    table: str,
    name_contains_filter: bool,
    *,
    backtest_dir: str | None = None,
    path: str | None = None,
    from_branch: str | None = None,
    to_branch: str | None = None,
    merge: bool = True,
    insert_batch_rows: int = 80,
    match_dolt_columns: bool = True,
) -> None:
    try:
        push_backtest_csvs_by_name_rule(
            table,
            name_contains_filter=name_contains_filter,
            backtest_dir=backtest_dir,
            path=path,
            from_branch=from_branch,
            to_branch=to_branch,
            merge=merge,
            insert_batch_rows=insert_batch_rows,
            match_dolt_columns=match_dolt_columns,
        )
    except DoltHubSqlError as e:
        print(f"❌ {e}")
        sys.exit(1)


def push_merged_review_csvs_to_table(
    table: str,
    paths: list[str],
    *,
    label: str,
    from_branch: str | None = None,
    to_branch: str | None = None,
    merge: bool = True,
    insert_batch_rows: int = 80,
    match_dolt_columns: bool = True,
    omit_name_column: bool = False,
) -> None:
    """
    将多个本地 CSV 合并后 push 到指定 Dolt 表（整表覆盖，逻辑同 push_table_from_csv）。
    """
    if not paths:
        raise DoltHubSqlError(f"{label}: 没有匹配的 CSV 文件")
    tmp, n = _merge_review_csvs_to_tempfile(paths)
    try:
        print(
            f"📎 {label}: 合并 {len(paths)} 个文件 → 临时表 {n} 行，目标 Dolt 表 `{table}`",
        )
        ts = datetime.now().strftime("%Y-%m-%d %H:%M")
        merged_msg = f"sync {table} ({n} rows, {len(paths)} files) @ {ts}"
        push_table_from_csv(
            table,
            tmp,
            from_branch=from_branch,
            to_branch=to_branch,
            merge=merge,
            insert_batch_rows=insert_batch_rows,
            match_dolt_columns=match_dolt_columns,
            merge_message=merged_msg,
            omit_name_column=omit_name_column,
        )
    finally:
        try:
            os.unlink(tmp)
        except OSError:
            pass


def push_csv_group_by_name_rule(
    table: str,
    *,
    name_contains_filter: bool,
    other_command: str,
    scan_dir: str | None = None,
    path: str | None = None,
    recursive: bool = False,
    default_root: Callable[[], str] = _default_review_csv_dir,
    exclude_basenames: frozenset[str] | None = None,
    from_branch: str | None = None,
    to_branch: str | None = None,
    merge: bool = True,
    insert_batch_rows: int = 80,
    match_dolt_columns: bool = True,
    omit_name_column: bool = False,
) -> None:
    """
    合并本地目录下符合文件名规则的 CSV（可选递归子目录），push 到 ``table``。

    - ``name_contains_filter=True``：只选文件名含 ``filter`` 的 .csv
    - ``name_contains_filter=False``：只选文件名不含 ``filter`` 的 .csv
    - ``exclude_basenames``：按文件名（小写）再排除，例如 qlib_score 排除 ``total.csv``
    - ``omit_name_column``：合并上传前去掉列 ``name``（qlib_score 流程为 True）
    """
    if path:
        if not os.path.isfile(path):
            raise DoltHubSqlError(f"文件不存在: {path}")
        bn = os.path.basename(path).lower()
        has_f = "filter" in bn
        if name_contains_filter and not has_f:
            raise DoltHubSqlError(f"该文件名不含 filter，请改用 {other_command}")
        if not name_contains_filter and has_f:
            raise DoltHubSqlError(f"该文件名含 filter，请改用 {other_command}")
        paths = [path]
    else:
        root = scan_dir or default_root()
        paths = _collect_csv_paths_by_name_filter(
            root,
            name_contains_filter=name_contains_filter,
            recursive=recursive,
        )

    if exclude_basenames:
        ex = {n.lower() for n in exclude_basenames}
        paths = [p for p in paths if os.path.basename(p).lower() not in ex]

    if not paths:
        raise DoltHubSqlError(
            "没有可提交的 CSV 文件（检查目录、filter 规则或排除列表）",
        )

    mode = "文件名含 filter" if name_contains_filter else "文件名不含 filter"
    depth = "（递归子目录）" if recursive else ""
    push_merged_review_csvs_to_table(
        table,
        paths,
        label=f"{table}（{mode}）{depth}",
        from_branch=from_branch,
        to_branch=to_branch,
        merge=merge,
        insert_batch_rows=insert_batch_rows,
        match_dolt_columns=match_dolt_columns,
        omit_name_column=omit_name_column,
    )


def push_review_csvs_by_name_rule(
    table: str,
    *,
    name_contains_filter: bool,
    review_dir: str | None = None,
    path: str | None = None,
    from_branch: str | None = None,
    to_branch: str | None = None,
    merge: bool = True,
    insert_batch_rows: int = 80,
    match_dolt_columns: bool = True,
) -> None:
    """``review_csv`` 单层目录，规则同 :func:`push_csv_group_by_name_rule`。"""
    other = "push_review_filter_ret" if not name_contains_filter else "push_review_ret"
    push_csv_group_by_name_rule(
        table,
        name_contains_filter=name_contains_filter,
        other_command=other,
        scan_dir=review_dir,
        path=path,
        recursive=False,
        default_root=_default_review_csv_dir,
        from_branch=from_branch,
        to_branch=to_branch,
        merge=merge,
        insert_batch_rows=insert_batch_rows,
        match_dolt_columns=match_dolt_columns,
        omit_name_column=False,
    )


def push_qlib_score_csvs_by_name_rule(
    table: str,
    *,
    name_contains_filter: bool,
    qlib_score_dir: str | None = None,
    path: str | None = None,
    from_branch: str | None = None,
    to_branch: str | None = None,
    merge: bool = True,
    insert_batch_rows: int = 80,
    match_dolt_columns: bool = True,
) -> None:
    """``qlib_score_csv`` 下**递归**遍历所有子目录中的 .csv（默认排除 ``total.csv``）；上传前会去掉 ``name`` 列（INSERT 不包含）。"""
    other = "push_qlib_score_filter_ret" if not name_contains_filter else "push_qlib_score_ret"
    push_csv_group_by_name_rule(
        table,
        name_contains_filter=name_contains_filter,
        other_command=other,
        scan_dir=qlib_score_dir,
        path=path,
        recursive=True,
        default_root=_default_qlib_score_csv_dir,
        exclude_basenames=QLIB_SCORE_EXCLUDED_CSV_BASENAMES,
        from_branch=from_branch,
        to_branch=to_branch,
        merge=merge,
        insert_batch_rows=insert_batch_rows,
        match_dolt_columns=match_dolt_columns,
        omit_name_column=True,
    )


def _run_review_push_cli(
    table: str,
    name_contains_filter: bool,
    *,
    review_dir: str | None = None,
    path: str | None = None,
    from_branch: str | None = None,
    to_branch: str | None = None,
    merge: bool = True,
    insert_batch_rows: int = 80,
    match_dolt_columns: bool = True,
) -> None:
    try:
        push_review_csvs_by_name_rule(
            table,
            name_contains_filter=name_contains_filter,
            review_dir=review_dir,
            path=path,
            from_branch=from_branch,
            to_branch=to_branch,
            merge=merge,
            insert_batch_rows=insert_batch_rows,
            match_dolt_columns=match_dolt_columns,
        )
    except DoltHubSqlError as e:
        print(f"❌ {e}")
        sys.exit(1)


def _run_qlib_score_push_cli(
    table: str,
    name_contains_filter: bool,
    *,
    qlib_score_dir: str | None = None,
    path: str | None = None,
    from_branch: str | None = None,
    to_branch: str | None = None,
    merge: bool = True,
    insert_batch_rows: int = 80,
    match_dolt_columns: bool = True,
) -> None:
    try:
        push_qlib_score_csvs_by_name_rule(
            table,
            name_contains_filter=name_contains_filter,
            qlib_score_dir=qlib_score_dir,
            path=path,
            from_branch=from_branch,
            to_branch=to_branch,
            merge=merge,
            insert_batch_rows=insert_batch_rows,
            match_dolt_columns=match_dolt_columns,
        )
    except DoltHubSqlError as e:
        print(f"❌ {e}")
        sys.exit(1)


def _rows(data: dict[str, Any]) -> list[dict[str, Any]]:
    return list(data.get("rows") or [])


def _schema_columns(data: dict[str, Any]) -> list[str] | None:
    schema = data.get("schema") or []
    if not schema:
        return None
    return [str(c.get("columnName", "")) for c in schema]


def _rows_to_dataframe(data: dict[str, Any]) -> pd.DataFrame:
    cols = _schema_columns(data)
    rows = _rows(data)
    if not rows:
        if cols:
            return pd.DataFrame(columns=cols)
        return pd.DataFrame()
    df = pd.DataFrame(rows)
    return df


def _table_names_from_show(data: dict[str, Any]) -> list[str]:
    names: list[str] = []
    for row in _rows(data):
        if not row:
            continue
        if "Table" in row:
            names.append(str(row["Table"]))
        elif "Tables_in_" in str(next(iter(row.keys()), "")):
            names.append(str(next(iter(row.values()))))
        else:
            names.append(str(next(iter(row.values()))))
    return names


def _scalar(data: dict[str, Any]) -> Any:
    rows = _rows(data)
    if not rows:
        return None
    return next(iter(rows[0].values()))


def _column_names_from_describe(df_desc: pd.DataFrame) -> list[str]:
    """从 DESCRIBE 结果中解析字段名（兼容 Field / COLUMN_NAME）。"""
    if df_desc.empty:
        return []
    for col in ("Field", "field", "COLUMN_NAME"):
        if col in df_desc.columns:
            return [str(x) for x in df_desc[col].tolist()]
    # 退化：第一列视为字段名
    return [str(x) for x in df_desc.iloc[:, 0].tolist()]


def fetch_dolt_table_columns(table: str) -> list[str]:
    """从 DoltHub 当前 ref 上读取表的列名（DESCRIBE），顺序与云端一致。"""
    safe = table.replace("`", "``")
    data = dolt_sql(f"DESCRIBE `{safe}`")
    df_desc = _rows_to_dataframe(data)
    cols = _column_names_from_describe(df_desc)
    if not cols:
        raise DoltHubSqlError(f"无法读取表 `{table}` 的列定义（或表不存在）")
    return cols


def align_dataframe_to_dolt_columns(df: pd.DataFrame, dolt_columns: list[str]) -> pd.DataFrame:
    """
    按 Dolt 表列对齐：仅保留云端已存在的列名；本地多出的列丢弃；
    云端有而本地 CSV 没有的列补 NaN（INSERT 时写成 NULL）。
    """
    dolt_set = set(dolt_columns)
    extra = [str(c) for c in df.columns if c not in dolt_set]
    if extra:
        print(f"ℹ️  本地多出字段（已忽略，仅提交 Dolt 已有列）: {extra}")
    missing = [c for c in dolt_columns if c not in df.columns]
    if missing:
        print(f"ℹ️  云端有、本地无（将插入 NULL）: {missing}")
    out = pd.DataFrame(index=df.index)
    for c in dolt_columns:
        if c in df.columns:
            out[c] = df[c]
        else:
            out[c] = np.nan
    return out


def _pick_datetime_column(names: list[str]) -> str | None:
    """优先选名为 datetime 的列，否则选第一个含 date/time 的列名。"""
    lower_map = {n.lower(): n for n in names}
    if "datetime" in lower_map:
        return lower_map["datetime"]
    for n in names:
        nl = n.lower()
        if "date" in nl or nl.endswith("time"):
            return n
    return None


def collect_table_detail(table: str, sample_rows: int = 5) -> dict[str, Any]:
    """
    收集单张表的详细元数据：DESCRIBE、行数、时间列 MIN/MAX、样本行。
    用于 inspect / inspect_table / 导出报告。
    """
    safe = table.replace("`", "``")
    detail: dict[str, Any] = {"table": table}

    try:
        desc_data = dolt_sql(f"DESCRIBE `{safe}`")
        df_desc = _rows_to_dataframe(desc_data)
        detail["describe"] = df_desc
    except DoltHubSqlError as e:
        detail["describe"] = pd.DataFrame()
        detail["describe_error"] = str(e)
        df_desc = pd.DataFrame()

    names = _column_names_from_describe(df_desc)
    detail["column_names"] = names

    try:
        count_data = dolt_sql(f"SELECT COUNT(*) AS c FROM `{safe}`")
        detail["row_count"] = _scalar(count_data)
    except DoltHubSqlError as e:
        detail["row_count"] = None
        detail["count_error"] = str(e)

    dt_col = _pick_datetime_column(names)
    detail["datetime_column"] = dt_col
    if dt_col:
        dc = dt_col.replace("`", "``")
        for agg, key in (("MIN", "min_datetime"), ("MAX", "max_datetime")):
            try:
                agg_data = dolt_sql(
                    f"SELECT {agg}(`{dc}`) AS v FROM `{safe}`",
                )
                detail[key] = _scalar(agg_data)
            except DoltHubSqlError:
                detail[key] = None
    else:
        detail["min_datetime"] = None
        detail["max_datetime"] = None

    if sample_rows > 0:
        try:
            lim = max(0, min(int(sample_rows), 500))
            sample_data = dolt_sql(f"SELECT * FROM `{safe}` LIMIT {lim}")
            detail["sample"] = _rows_to_dataframe(sample_data)
        except DoltHubSqlError as e:
            detail["sample"] = pd.DataFrame()
            detail["sample_error"] = str(e)
    else:
        detail["sample"] = pd.DataFrame()

    return detail


def _detail_to_jsonable(detail: dict[str, Any]) -> dict[str, Any]:
    """将 collect_table_detail 结果转为可 JSON 序列化的 dict。"""
    out: dict[str, Any] = {}
    for k, v in detail.items():
        if isinstance(v, pd.DataFrame):
            out[k] = v.replace({np.nan: None}).to_dict(orient="records")
        elif isinstance(v, (np.integer, np.floating)):
            x = v.item()
            if isinstance(x, float) and (np.isnan(x) or np.isinf(x)):
                out[k] = None
            else:
                out[k] = x
        else:
            out[k] = v
    return out


def print_table_detail(detail: dict[str, Any]) -> None:
    """将 collect_table_detail 的结果打印到终端。"""
    table = detail["table"]
    line = "=" * 72
    print(f"\n{line}")
    print(f"📋 表: {table}")
    print(line)

    if detail.get("describe_error"):
        print(f"\n❌ DESCRIBE 失败: {detail['describe_error']}")
    else:
        df_desc = detail.get("describe")
        if isinstance(df_desc, pd.DataFrame) and not df_desc.empty:
            print("\n【列结构】(DESCRIBE)")
            print(df_desc.to_string(index=False))
        else:
            print("\n【列结构】无")

    rc = detail.get("row_count")
    print(f"\n【行数】 {rc if rc is not None else 'N/A'}")
    if detail.get("count_error"):
        print(f"   ⚠️ COUNT 错误: {detail['count_error']}")

    dtc = detail.get("datetime_column")
    if dtc:
        print(f"\n【时间列】 `{dtc}`")
        print(f"   MIN(`{dtc}`) = {detail.get('min_datetime')}")
        print(f"   MAX(`{dtc}`) = {detail.get('max_datetime')}")
    else:
        print("\n【时间列】未识别到 datetime / *date* 列，已跳过 MIN/MAX。")

    if detail.get("sample_error"):
        print(f"\n❌ 样本行失败: {detail['sample_error']}")
    else:
        df_s = detail.get("sample")
        if isinstance(df_s, pd.DataFrame) and not df_s.empty:
            print(f"\n【样本行】前 {len(df_s)} 行")
            print(df_s.to_string(index=False))
        elif isinstance(df_s, pd.DataFrame):
            print("\n【样本行】（空表）")


def pull_table_to_csv(
    table: str,
    out_path: str,
    *,
    chunk_size: int = 10_000,
) -> str:
    """
    将整张表拉取为本地 CSV（分页 SELECT，应对 API 行数上限）。
    返回写入的文件路径。
    """
    os.makedirs(os.path.dirname(os.path.abspath(out_path)) or ".", exist_ok=True)
    safe = table.replace("`", "``")

    offset = 0
    first = True
    while True:
        q = f"SELECT * FROM `{safe}` LIMIT {chunk_size} OFFSET {offset}"
        data = dolt_sql(q)
        df = _rows_to_dataframe(data)
        n = len(df)
        if n == 0:
            if first:
                empty = dolt_sql(f"SELECT * FROM `{safe}` LIMIT 0")
                df0 = _rows_to_dataframe(empty)
                df0.to_csv(out_path, index=False, mode="w", encoding="utf-8")
            break
        mode = "w" if first else "a"
        header = first
        df.to_csv(out_path, index=False, mode=mode, header=header, encoding="utf-8")
        first = False
        if n < chunk_size:
            break
        offset += n

    return out_path


class DoltHubCLI:
    """DoltHub SQL API 命令行（Fire）：pull=云端→本地，push=本地→云端。"""

    def __init__(
        self,
        owner: str = OWNER,
        database: str = DATABASE,
        ref: str | None = None,
    ) -> None:
        global OWNER, DATABASE, REF
        OWNER = owner
        DATABASE = database
        REF = (ref or os.getenv("DOLT_REF", "main") or "main").strip() or "main"

    def inspect(
        self,
        brief: bool = False,
        sample_rows: int = 5,
        path: str | None = None,
    ) -> None:
        """
        盘点仓库中所有表。

        默认（brief=False）对每张表输出：DESCRIBE 列结构、行数、时间列 MIN/MAX、样本行。
        brief=True 时仅输出一行汇总（表名 / 行数 / MAX(datetime)）。

        :param brief: 是否仅简要一行汇总
        :param sample_rows: 每张表展示的样本行数；0 表示不拉样本
        :param path: 若指定，将「详细」结果写入 JSON（UTF-8），结构与 inspect_table 返回一致
        """
        print(f"🔍 正在盘点 Dolt 仓库: {OWNER}/{DATABASE} (ref={REF}) ...\n")
        if not TOKEN:
            print("ℹ️  未设置 DOLT_TOKEN：仅适合公开库；私有库请设置环境变量 DOLT_TOKEN\n")

        try:
            show = dolt_sql("SHOW TABLES;")
        except DoltHubSqlError as e:
            print(f"❌ {e}")
            sys.exit(1)

        tables = _table_names_from_show(show)

        if not tables:
            print("⚠️ 仓库是空的，一张表都没有。")
            return

        if brief:
            summary = []
            for table in tables:
                safe = table.replace("`", "``")
                count_sql = f"SELECT COUNT(*) AS c FROM `{safe}`"
                try:
                    count_data = dolt_sql(count_sql)
                    row_count = _scalar(count_data)
                except DoltHubSqlError as e:
                    row_count = f"错误: {e}"

                latest_date: Any = "N/A"
                try:
                    max_sql = f"SELECT MAX(datetime) AS m FROM `{safe}`"
                    max_data = dolt_sql(max_sql)
                    latest_date = _scalar(max_data)
                except DoltHubSqlError:
                    latest_date = "N/A"

                summary.append(
                    {
                        "Table Name": table,
                        "Rows": row_count,
                        "Latest Data": latest_date,
                    }
                )

            df_summary = pd.DataFrame(summary)
            print(df_summary.to_string(index=False))
            print("\n✅ 简要盘点完成！（需要列结构等请加 --brief=False）")
            return

        all_json: list[dict[str, Any]] = []
        for table in tables:
            detail = collect_table_detail(table, sample_rows=sample_rows)
            print_table_detail(detail)
            all_json.append(_detail_to_jsonable(detail))

        if path:
            os.makedirs(os.path.dirname(os.path.abspath(path)) or ".", exist_ok=True)
            payload = {
                "owner": OWNER,
                "database": DATABASE,
                "ref": REF,
                "tables": all_json,
            }
            with open(path, "w", encoding="utf-8") as f:
                json.dump(payload, f, ensure_ascii=False, indent=2)
            print(f"\n📄 详细结果已写入 JSON: {path}")

        print("\n✅ 详细盘点完成！")

    def inspect_table(
        self,
        table: str,
        sample_rows: int = 5,
        path: str | None = None,
    ) -> dict[str, Any]:
        """
        单表详细盘点：返回可 JSON 序列化的 dict（describe/sample 为 list[dict]）。

        同时打印分块说明。数据量大时建议加 --path=xxx.json，避免终端刷屏。
        通过 Fire 调用时也会打印返回值；脚本内可直接用本函数返回值。

        :param table: 表名
        :param sample_rows: 样本行数，0 表示不要样本
        :param path: 可选，另存单表 JSON（含 owner/database/ref）
        """
        detail = collect_table_detail(table, sample_rows=sample_rows)
        print_table_detail(detail)
        out = _detail_to_jsonable(detail)
        payload = {"owner": OWNER, "database": DATABASE, "ref": REF, **out}
        if path:
            os.makedirs(os.path.dirname(os.path.abspath(path)) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(payload, f, ensure_ascii=False, indent=2)
            print(f"\n📄 已写入: {path}")
        return out

    def query(
        self,
        sql: str,
        path: str | None = None,
        max_rows: int | None = 500,
    ) -> None:
        """
        执行只读 SQL。默认最多拉取 API 返回的一段结果；打印前 max_rows 行或写入 path。

        :param sql: SQL 语句
        :param path: 若指定，将完整返回行写入该 CSV（仍受 API 单次返回限制）
        :param max_rows: 终端预览最大行数；None 表示不截断打印
        """
        if not TOKEN:
            print("ℹ️  未设置 DOLT_TOKEN：公开库可读；私有库请设置 DOLT_TOKEN\n")

        try:
            data = dolt_sql(sql)
        except DoltHubSqlError as e:
            print(f"❌ {e}")
            sys.exit(1)

        df = _rows_to_dataframe(data)
        status = data.get("query_execution_status")
        if status == "RowLimit":
            print("⚠️  本次结果被 API 截断 (RowLimit)；大结果请用 pull 整表导出。\n")

        if path:
            os.makedirs(os.path.dirname(os.path.abspath(path)) or ".", exist_ok=True)
            df.to_csv(path, index=False, encoding="utf-8")
            print(f"✅ 已写入 {path} ，共 {len(df)} 行。")
            return

        if max_rows is not None and len(df) > max_rows:
            print(df.head(max_rows).to_string(index=False))
            print(f"\n… 共 {len(df)} 行，仅显示前 {max_rows} 行。写入文件请加 --path=...")
        else:
            print(df.to_string(index=False))
        print(f"\n✅ 查询完成（{len(df)} 行）。")


    # ----- 六张表：云端 → 本地 -----
    def pull_qlib_score_filter_ret(
        self,
        qlib_score_dir: str | None = None,
        path: str | None = None,
        from_branch: str | None = None,
        to_branch: str | None = None,
        merge: bool = True,
        insert_batch_rows: int = 80,
        match_dolt_columns: bool = True,
    ) -> None:
        """
        **本地 → 云端**：在 ``qlib_score_csv`` 下**递归**合并「文件名含 filter」的 .csv，提交到 ``qlib_score_filter_ret``。

        默认排除 ``total.csv``；与 ``push_qlib_score_ret`` 仅文件名规则与目标表不同；需 ``DOLT_TOKEN``。
        从云端**下载**请用：``pull qlib_score_filter_ret``（或 ``pull`` + 表名）。
        """
        pass
    def pull_qlib_score_ret(
        self,
        qlib_score_dir: str | None = None,
        path: str | None = None,
        from_branch: str | None = None,
        to_branch: str | None = None,
        merge: bool = True,
        insert_batch_rows: int = 80,
        match_dolt_columns: bool = True,
    ) -> None:
        """
        **本地 → 云端**：在 ``qlib_score_csv`` 下**递归**合并「文件名不含 filter」的 .csv，提交到 ``qlib_score_ret``。

        默认排除 ``total.csv``；与 ``push_qlib_score_filter_ret`` 仅文件名规则与目标表不同；需 ``DOLT_TOKEN``。
        从云端**下载**请用：``pull qlib_score_ret``。
        """
        pass
    def pull_review_ret(
        self,
        review_dir: str | None = None,
        path: str | None = None,
        from_branch: str | None = None,
        to_branch: str | None = None,
        merge: bool = True,
        insert_batch_rows: int = 80,
        match_dolt_columns: bool = True,
    ) -> None:
        """
        **本地 → 云端**：在 ``review_csv`` 下合并「文件名不含 filter」的 .csv，提交到 ``review_ret``。

        与 ``push_review_filter_ret`` 仅文件名规则与目标表不同；需 ``DOLT_TOKEN``。
        """
        pass
    def pull_review_filter_ret(
        self,
        review_dir: str | None = None,
        path: str | None = None,
        from_branch: str | None = None,
        to_branch: str | None = None,
        merge: bool = True,
        insert_batch_rows: int = 80,
        match_dolt_columns: bool = True,
    ) -> None:
        """
        **本地 → 云端**：在 ``review_csv`` 下合并「文件名含 filter」的 .csv，提交到 ``review_filter_ret``。

        与 ``push_review_ret`` 仅文件名规则与目标表不同；需 ``DOLT_TOKEN``。
        """
        pass

    # ----- 六张表：本地 → 云端  -----

    def push_backtest_filter_ret(
        self,
        backtest_dir: str | None = None,
        path: str | None = None,
        from_branch: str | None = None,
        to_branch: str | None = None,
        merge: bool = True,
        insert_batch_rows: int = 80,
        match_dolt_columns: bool = True,
    ) -> None:
        """
        **本地 → 云端**：在 ``backtest_csv`` 下合并「文件名含 filter」的 .csv，提交到 ``backtest_filter_ret``。

        文件名须以数字开头，该数字写入列 ``top_k``；与 ``push_backtest_ret`` 仅文件名规则与目标表不同；需 ``DOLT_TOKEN``。
        """
        _run_backtest_push_cli(
            "backtest_filter_ret",
            True,
            backtest_dir=backtest_dir,
            path=path,
            from_branch=from_branch,
            to_branch=to_branch,
            merge=merge,
            insert_batch_rows=insert_batch_rows,
            match_dolt_columns=match_dolt_columns,
        )

    def push_backtest_ret(
        self,
        backtest_dir: str | None = None,
        path: str | None = None,
        from_branch: str | None = None,
        to_branch: str | None = None,
        merge: bool = True,
        insert_batch_rows: int = 80,
        match_dolt_columns: bool = True,
    ) -> None:
        """
        **本地 → 云端**：在 ``backtest_csv`` 下合并「文件名不含 filter」的 .csv，提交到 ``backtest_ret``。

        文件名须以数字开头，该数字写入列 ``top_k``；与 ``push_backtest_filter_ret`` 仅文件名规则与目标表不同；需 ``DOLT_TOKEN``。
        """
        _run_backtest_push_cli(
            "backtest_ret",
            False,
            backtest_dir=backtest_dir,
            path=path,
            from_branch=from_branch,
            to_branch=to_branch,
            merge=merge,
            insert_batch_rows=insert_batch_rows,
            match_dolt_columns=match_dolt_columns,
        )



    def push_qlib_score_filter_ret(
        self,
        qlib_score_dir: str | None = None,
        path: str | None = None,
        from_branch: str | None = None,
        to_branch: str | None = None,
        merge: bool = True,
        insert_batch_rows: int = 80,
        match_dolt_columns: bool = True,
    ) -> None:
        _run_qlib_score_push_cli(
            "qlib_score_filter_ret",
            True,
            qlib_score_dir=qlib_score_dir,
            path=path,
            from_branch=from_branch,
            to_branch=to_branch,
            merge=merge,
            insert_batch_rows=insert_batch_rows,
            match_dolt_columns=match_dolt_columns,
        )

    def push_qlib_score_ret(
        self,
        qlib_score_dir: str | None = None,
        path: str | None = None,
        from_branch: str | None = None,
        to_branch: str | None = None,
        merge: bool = True,
        insert_batch_rows: int = 80,
        match_dolt_columns: bool = True,
    ) -> None:
        _run_qlib_score_push_cli(
            "qlib_score_ret",
            False,
            qlib_score_dir=qlib_score_dir,
            path=path,
            from_branch=from_branch,
            to_branch=to_branch,
            merge=merge,
            insert_batch_rows=insert_batch_rows,
            match_dolt_columns=match_dolt_columns,
        )

    def push_review_ret(
        self,
        review_dir: str | None = None,
        path: str | None = None,
        from_branch: str | None = None,
        to_branch: str | None = None,
        merge: bool = True,
        insert_batch_rows: int = 80,
        match_dolt_columns: bool = True,
    ) -> None:
        _run_review_push_cli(
            "review_ret",
            False,
            review_dir=review_dir,
            path=path,
            from_branch=from_branch,
            to_branch=to_branch,
            merge=merge,
            insert_batch_rows=insert_batch_rows,
            match_dolt_columns=match_dolt_columns,
        )

    def push_review_filter_ret(
        self,
        review_dir: str | None = None,
        path: str | None = None,
        from_branch: str | None = None,
        to_branch: str | None = None,
        merge: bool = True,
        insert_batch_rows: int = 80,
        match_dolt_columns: bool = True,
    ) -> None:
        _run_review_push_cli(
            "review_filter_ret",
            True,
            review_dir=review_dir,
            path=path,
            from_branch=from_branch,
            to_branch=to_branch,
            merge=merge,
            insert_batch_rows=insert_batch_rows,
            match_dolt_columns=match_dolt_columns,
        )


def main() -> None:
    fire.Fire(DoltHubCLI)


if __name__ == "__main__":
    main()
