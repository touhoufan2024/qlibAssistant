import os
import re
import sys
import subprocess
import hashlib
from typing import Optional, Tuple, List, Union
from pathlib import Path
from datetime import datetime
from dateutil.relativedelta import relativedelta

# 第三方库
import requests
from bs4 import BeautifulSoup
import akshare as ak
import pandas as pd
from loguru import logger

import locale

# --- 常量定义 ---
DEFAULT_ENCODING = "utf-8"
DEFAULT_TIMEOUT = (10, 30)  # (连接超时, 读取超时)
GITHUB_ASSETS_PATTERN = re.compile(r"expanded_assets")
# MLflow 路径修复正则：使用命名组提高可读性
MLFLOW_PATH_PATTERN = re.compile(
    r"^(?P<key>artifact_(location|uri)):\s+file:///home/[^/]+/(?P<suffix>.*)"
)

def check_match(str_a: str, pattern: str) -> bool:
    """检查字符串是否匹配正则"""
    return bool(re.search(pattern, str_a))

def filter_csv(file_path: Union[str, Path]) -> str:
    """过滤 CSV 并返回股票代码字符串"""
    try:
        df = pd.read_csv(file_path)
        # 链式过滤提高性能
        mask = (df['avg_score'] > 0) & (df['pos_ratio'] > 0.8)
        filtered_df = df[mask].copy()

        def clean_code(text):
            return "".join(re.findall(r'\d+', str(text)))

        stock_codes = filtered_df['instrument'].apply(clean_code).tolist()
        return ",".join(stock_codes)
    except Exception as e:
        logger.error(f"过滤 CSV 失败: {e}")
        return ""

def check_match_in_list(target_str: str, regex_list: List[str]) -> bool:
    """检查目标字符串是否匹配列表中的任一正则"""
    return any(re.search(pattern, target_str) for pattern in regex_list)

def get_latest_url(base_url: str) -> str:
    """追踪 URL 重定向获取最终地址"""
    try:
        response = requests.get(base_url, allow_redirects=True, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        logger.info(f"Final download URL: {response.url}")
        return response.url
    except requests.RequestException as e:
        logger.error(f"追踪 URL 失败: {e}")
        return base_url

def run_command(cmd: str) -> Tuple[int, str, str]:
    """执行 Shell 命令并捕获输出"""
    # 获取当前运行环境的系统编码
    current_encoding = locale.getpreferredencoding()
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            encoding=current_encoding
        )
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return -1, "", str(e)

def calculate_file_sha256(file_path: Union[str, Path]) -> Optional[str]:
    """计算文件的 SHA256 哈希值"""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        logger.warning(f"文件未找到: {file_path}")
        return None

def get_real_github_hash(repo_url: str, target_filename: str) -> Optional[str]:
    """从 GitHub Release 页面提取资源的 SHA256"""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    try:
        session = requests.Session()
        response = session.get(repo_url, headers=headers, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        fragment_tag = soup.find("include-fragment", src=GITHUB_ASSETS_PATTERN)

        target_soup = soup
        if fragment_tag:
            assets_url = fragment_tag['src']
            if not assets_url.startswith("http"):
                assets_url = f"https://github.com{assets_url}"
            resp_assets = session.get(assets_url, headers=headers, timeout=DEFAULT_TIMEOUT)
            target_soup = BeautifulSoup(resp_assets.text, 'html.parser')

        # 定位文件链接
        file_link = target_soup.find("a", href=re.compile(re.escape(target_filename) + r"$"))
        if not file_link:
            logger.error(f"GitHub 上未找到文件: {target_filename}")
            return None

        # 向上搜索哈希剪贴板
        current = file_link.parent
        for _ in range(5):
            if not current: break
            clipboard = current.find("clipboard-copy")
            if clipboard and clipboard.get("value") and "sha256" in clipboard["value"]:
                return clipboard["value"][7:] # 移除 'sha256 ' 前缀
            current = current.parent

    except Exception as e:
        logger.error(f"解析 GitHub 哈希失败: {e}")
    return None

def append_to_file(file_path: Union[str, Path], content: str, mmode: str = 'a'):
    """追加内容到文件"""
    try:
        with open(file_path, mode=mmode, encoding=DEFAULT_ENCODING) as f:
            f.write(content)
    except Exception as e:
        logger.error(f"文件追加失败: {e}")

def process_stock_code_v2(code: str) -> str:
    """标准化股票代码（带市场前缀）"""
    code_str = str(code).zfill(6)
    if code_str.startswith("6"):
        return f"SH{code_str}"
    elif code_str.startswith(("0", "3")):
        return f"SZ{code_str}"
    elif code_str.startswith(("8", "4", "920")):
        return f"BJ{code_str}"
    return f"unknown{code_str}"

def _stock_list_from_sina() -> Optional[pd.DataFrame]:
    """新浪数据源：stock_zh_a_spot，GitHub Actions 环境通常可访问"""
    df = ak.stock_zh_a_spot()
    df = df.rename(columns={"代码": "code", "名称": "name"})
    df["code"] = df["code"].str.upper()  # bj430017 -> BJ430017, sz000001 -> SZ000001
    return df[["code", "name"]]


def _stock_list_from_exchanges() -> Optional[pd.DataFrame]:
    """沪深京交易所官网：非东方财富，海外 IP 通常可访问"""
    parts = []
    try:
        sh_df = ak.stock_info_sh_name_code(symbol="主板A股")
        sh_df = sh_df.rename(columns={"证券代码": "code", "证券简称": "name"})
        sh_df["code"] = sh_df["code"].apply(process_stock_code_v2)
        parts.append(sh_df[["code", "name"]])
    except Exception as e:
        logger.warning(f"上交所股票列表获取失败: {e}")
    try:
        sh_kcb = ak.stock_info_sh_name_code(symbol="科创板")
        sh_kcb = sh_kcb.rename(columns={"证券代码": "code", "证券简称": "name"})
        sh_kcb["code"] = sh_kcb["code"].apply(process_stock_code_v2)
        parts.append(sh_kcb[["code", "name"]])
    except Exception as e:
        logger.warning(f"科创板股票列表获取失败: {e}")
    try:
        sz_df = ak.stock_info_sz_name_code(symbol="A股列表")
        sz_df = sz_df.rename(columns={"A股代码": "code", "A股简称": "name"})
        sz_df["code"] = sz_df["code"].apply(process_stock_code_v2)
        parts.append(sz_df[["code", "name"]])
    except Exception as e:
        logger.warning(f"深交所股票列表获取失败: {e}")
    try:
        bj_df = ak.stock_info_bj_name_code()
        bj_df = bj_df.rename(columns={"证券代码": "code", "证券简称": "name"})
        bj_df["code"] = bj_df["code"].apply(process_stock_code_v2)
        parts.append(bj_df[["code", "name"]])
    except Exception as e:
        logger.warning(f"北交所股票列表获取失败: {e}")
    if not parts:
        return None
    return pd.concat(parts, ignore_index=True).drop_duplicates(subset=["code"])


def get_normalized_stock_list() -> Optional[pd.DataFrame]:
    """获取并标准化 A 股股票列表，多源 fallback 避免东方财富在 GitHub Actions 失败"""
    for env_key in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy']:
        os.environ.pop(env_key, None)

    # 1. 优先沪深京交易所官网（非东方财富，海外/国内 IP 通常可访问）
    try:
        df = _stock_list_from_exchanges()
        if df is not None and len(df) > 1000:
            return df
    except Exception as e:
        logger.warning(f"交易所股票列表获取失败: {e}")

    # 2. 备选新浪（单次请求，易返回 HTML 被限流）
    try:
        df = _stock_list_from_sina()
        if df is not None and len(df) > 1000:
            return df
    except Exception as e:
        logger.warning(f"新浪股票列表获取失败: {e}")

    # 3. 最后尝试东方财富（stock_info_a_code_name，GitHub Actions 常失败）
    try:
        df = ak.stock_info_a_code_name()
        df["code"] = df["code"].apply(process_stock_code_v2)
        return df
    except Exception as e:
        logger.error(f"AkShare 股票列表全部数据源拉取失败: {e}")
        return None

def get_latest_trade_date_ak():
    """获取最近一个已收盘的交易日"""
    try:
        trade_calendar = ak.tool_trade_date_hist_sina()
        today = datetime.now().date()
        past_days = [d for d in trade_calendar['trade_date'].tolist() if d <= today]

        if not past_days: return None

        last_day = past_days[-1]
        # 如果是今天且未收盘（15:00），取前一天
        if today == last_day and datetime.now().hour < 15:
            return past_days[-2] if len(past_days) > 1 else last_day
        return last_day
    except Exception as e:
        logger.error(f"获取交易日历失败: {e}")
        return None

def get_local_data_date(provider_uri):
    """获取本地数据日历的最后一行日期，支持跨平台路径和 ~ 符号"""
    # 处理 ~ 符号并转换为系统标准路径
    base_path = Path(provider_uri).expanduser()
    calendar_path = base_path / "calendars" / "day.txt"

    if not calendar_path.exists():
        logger.error(f"日历文件不存在: {calendar_path}")
        return ""

    try:
        with open(calendar_path, 'rb') as f:
            f.seek(0, 2)  # 移动到文件末尾
            file_size = f.tell()
            if file_size == 0:
                return ""

            # 从倒数第二个字节开始向前找换行符（避开文件末尾可能的换行）
            pos = file_size - 2
            while pos > 0:
                f.seek(pos)
                if f.read(1) == b'\n':
                    break
                pos -= 1

            # 读取最后一行
            last_line = f.readline().decode('utf-8', errors='ignore')
            return last_line.strip()
    except Exception as e:
        logger.error(f"读取本地数据日期失败: {e}")
        return ""

def fix_mlflow_paths(mlruns_dir: Optional[str] = None):
    """精准修复 MLflow 配置文件中的用户路径"""
    # 使用 as_posix() 确保在 Windows 下也是正斜杠，避免正则替换时的 \U 转义错误
    current_home = Path.home().as_posix()
    # MLflow URI 在 Windows 上通常使用 file:///C:/... 格式（3个斜杠）
    current_prefix = f"file:///{current_home.lstrip('/')}"

    if mlruns_dir is None:
        mlruns_dir = Path.home() / ".qlibAssistant" / "mlruns"

    base_path = Path(mlruns_dir).expanduser().resolve()
    if not base_path.exists():
        logger.warning(f"目录不存在: {base_path}")
        return

    logger.info(f"正在修复 MLflow 路径前缀为: {current_prefix}")

    fix_count = 0
    for root, _, files in os.walk(base_path):
        if "meta.yaml" in files:
            yaml_path = Path(root) / "meta.yaml"
            try:
                content = yaml_path.read_text(encoding=DEFAULT_ENCODING)
                # 使用命名分组替换
                new_content, count = MLFLOW_PATH_PATTERN.subn(
                    rf"\g<key>: {current_prefix}/\g<suffix>", content
                )
                if count > 0:
                    yaml_path.write_text(new_content, encoding=DEFAULT_ENCODING)
                    fix_count += count
            except Exception as e:
                logger.error(f"修复失败 {yaml_path}: {e}")

    logger.info(f"路径修复完成，共修改 {fix_count} 处。")


def get_mlruns_dates(backup_dir="../model_pkl"):
    """从 model_pkl 目录解析 mlruns_YYYY-MM-DD 格式的日期列表"""
    backup_path = Path(backup_dir).resolve()
    if not backup_path.exists():
        print(f"目录不存在: {backup_path}")
        return []

    pattern = re.compile(r"mlruns_(\d{4}-\d{2}-\d{2})")
    dates = []
    for file in backup_path.glob("mlruns_*.tar.gz"):
        match = pattern.search(file.name)
        if match:
            dates.append(match.group(1))
    return dates


def generate_qlib_segments(months_total=12, end_date_str=None):
    """
    根据给定的总月数，按 9:2:1 比例动态生成 train, valid, test 范围
    :param months_total: 总共回溯的月数
    :param end_date_str: 截止日期 (YYYY-MM-DD)，留空则默认为今天
    """
    if end_date_str:
        t_end = datetime.strptime(end_date_str, "%Y-%m-%d")
    else:
        t_end = datetime.now()

    # 1. 计算比例单位 (9 + 2 + 1 = 12 份)
    # 每一份代表的月数 = 总月数 / 12
    unit = months_total / 12.0

    # 2. 计算各段长度（月数）
    test_months = unit * 1  # 占 1 份
    valid_months = unit * 2 # 占 2 份
    train_months = unit * 9 # 占 9 份

    # 3. 倒推各个时间节点
    # t0(起点) ----[train]---- t1 ----[valid]---- t2 ----[test]---- t3(终点)
    t3 = t_end
    t2 = t3 - relativedelta(months=int(test_months))
    t1 = t2 - relativedelta(months=int(valid_months))
    t0 = t1 - relativedelta(months=int(train_months))

    def to_s(dt): return dt.strftime("%Y-%m-%d")

    # 4. 组装结果 (减去 1 天确保区间不重叠)
    segments = {
        "train": (to_s(t0), to_s(t1 - relativedelta(days=1))),
        "valid": (to_s(t1), to_s(t2 - relativedelta(days=1))),
        "test":  (to_s(t2), to_s(t3))
    }

    return segments


# 管理本地数据的交易日列表
class TradeDate:
    # 初始化交易日列表
    def __init__(self, provider_uri):
        # 使用 Path 处理跨平台路径
        self.provider_uri = Path(provider_uri).expanduser()
        self.trade_date_file = self.provider_uri / "calendars" / "day.txt"
        
        self.trade_date_list = []
        if self.trade_date_file.exists():
            try:
                with open(self.trade_date_file, "r", encoding=DEFAULT_ENCODING) as f:
                    # 过滤空行并去除换行符
                    self.trade_date_list = [line.strip() for line in f if line.strip()]
            except Exception as e:
                logger.error(f"读取交易日历文件失败: {e}")

    # 获取 start_date 和 end_date 之间的交易日列表
    def get_date_range(self, start_date, end_date):
        idx_s = self.trade_date_list.index(start_date)
        idx_e = self.trade_date_list.index(end_date)
        return self.trade_date_list[idx_s : idx_e + 1]

    # 获取所有交易日列表
    def get_trade_date_list(self):
        return self.trade_date_list

    # 获取指定日期的索引
    def get_date_index(self, date):
        return self.trade_date_list.index(date)

    # 获取指定日期之后的第 idx 个交易日
    def get_next_date(self, date, idx):
        i = self.get_date_index(date)
        if i + idx >= len(self.trade_date_list):
            return self.trade_date_list[-1]
        return self.trade_date_list[i + idx]