import re
from pathlib import Path
from typing import Dict

import pandas as pd
from loguru import logger
from pprint import pprint
from utils import append_to_file, TradeDate

top_num_list = [10, 20, 30, 50, 80, 100]

class ModelReviewHelper:
    """负责模型预测结果的回测复盘逻辑，拆分自 ModelCLI 降低单文件复杂度。"""

    def __init__(self, cli: "ModelCLI"):
        # 延迟注入，避免循环依赖（类型仅作注释使用）
        self.cli = cli
        self.kwargs: Dict = cli.kwargs

        self.review_result_string = "# 复盘统计分析\n"
        self.review_result_string += (
            f"\n 统计时间 {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        self.review_result_df = {}
        self.review_result_df_filter = {}
        self.trade_date = TradeDate(self.kwargs.get("provider_uri"))


    # ---------- CSV 单日回测 ----------
    def _review_csv(self, df, real_df, n1, n2):
        df = df[df["avg_score"] > 0].copy()  # 避免 SettingWithCopyWarning
        real_map = real_df.drop_duplicates("instrument").set_index("instrument")["real_label"]
        df["real_label"] = df["instrument"].map(real_map)

        df["error"] = df["avg_score"] - df["real_label"]
        df["abs_error"] = df["error"].abs()

        date_str = df["datetime"].iloc[0]
        print(f"分析 {date_str} csv")

        n1_renamed = n1[["instrument", "close"]].rename(columns={"close": "n1close"})
        n2_renamed = n2[["instrument", "high"]].rename(columns={"high": "n2high"})

        df = df.merge(n1_renamed, on="instrument", how="left")
        df = df.merge(n2_renamed, on="instrument", how="left")

        profit_num_list = [0.01 * i for i in range(1, 11)]  # 0.01 ~ 0.10

        topk_result_dict = {}
        topk_result_index = [
            "止盈1%胜率",
            "止盈2%胜率",
            "止盈3%胜率",
            "止盈4%胜率",
            "止盈5%胜率",
            "止盈6%胜率",
            "止盈7%胜率",
            "止盈8%胜率",
            "止盈9%胜率",
            "止盈10%胜率",
            "持有一天平均收益",
            "一天正收益占比",
        ]

        for top_num in top_num_list:
            topk_df = df.sort_values(by="avg_score", ascending=False).head(top_num)
            topk_avg_profit = topk_df["real_label"].mean()
            topk_radio = ((topk_df["real_label"] * topk_df["avg_score"]) > 0).sum() / len(topk_df)

            profit_list = []
            for profit_num in profit_num_list:
                topk_df_profit = (topk_df["n2high"] > topk_df["n1close"] * (1 + profit_num)).sum() / len(
                    topk_df
                )
                profit_list.append(topk_df_profit)

            profit_list.append(topk_avg_profit)
            profit_list.append(topk_radio)
            topk_result_dict[f"Top{top_num}"] = profit_list

        topk_result_df = pd.DataFrame(topk_result_dict, index=topk_result_index)
        topk_result_df.index.name = date_str

        def to_percent(val):
            if isinstance(val, (float, int)):
                return f"{val * 100:.2f}%"
            return val

        pct_df = topk_result_df.applymap(to_percent)
        print(pct_df.to_markdown(index=True))

        self.review_result_string += pct_df.to_markdown(index=True) + "\n"
        return df

    # ---------- 遍历单日子目录 ----------
    def _extract_date_from_csv_name(self, subdir: Path):
        return next(
            (
                re.match(r"(\d{4}-\d{2}-\d{2})_.*\.csv", file.name).group(1)
                for file in subdir.iterdir()
                if file.is_file() and re.match(r"(\d{4}-\d{2}-\d{2})_.*\.csv", file.name)
            ),
            None,
        )

    def _review_subdir(self, subdir: Path):
        print(f"- {subdir.name}")
        self.review_result_string += f"## {subdir.name}\n"

        date_str = self._extract_date_from_csv_name(subdir)
        if date_str:
            print(f"直接从文件名提取的日期: {date_str}")
        else:
            print("未发现格式为 xxxx-xx-xx_ 的 CSV 文件名")

        idx = self.trade_date.get_date_index(date_str)
        if idx is None:
            logger.info(f"{subdir.name} 日期 {date_str} 不在交易日日历中，不能复盘")
            return

        # 复盘依赖下一个与下下个交易日，任一缺失都不执行复盘。
        if idx + 2 >= len(self.trade_date.get_trade_date_list()):
            logger.info(f"还不能复盘 {date_str}")
            self.review_result_string += f"还不能复盘 {date_str}\n"
            return

        next1_date = self.trade_date.get_next_date(date_str, 1) if idx + 1 < len(self.trade_date.get_trade_date_list()) else None
        next2_date = self.trade_date.get_next_date(date_str, 2) if idx + 2 < len(self.trade_date.get_trade_date_list()) else None

        logger.info(
            f"开始复盘 {date_str if date_str else '[未知日期]'}  "
            f"btw:[下1个交易日: {next1_date if next1_date else '[未知日期]'}  "
            f"下2个交易日: {next2_date if next2_date else '[未知日期]'}]"
        )

        df_filter_ret = pd.read_csv(subdir / f"{date_str}_filter_ret.csv")
        df_ret = pd.read_csv(subdir / f"{date_str}_ret.csv")

        real_df = self.cli.get_real_label(dates={"start": date_str, "end": date_str})
        real_df = real_df.reset_index()

        # 删除 'KMID' 及其右侧所有表项（包含 KMID）
        for name, df in [("df_ret", df_ret), ("df_filter_ret", df_filter_ret)]:
            if df is not None and not df.empty:
                if "KMID" in df.columns:
                    kmid_idx = df.columns.get_loc("KMID")
                    if name == "df_ret":
                        df_ret = df.iloc[:, :kmid_idx]
                    else:
                        df_filter_ret = df.iloc[:, :kmid_idx]
                else:
                    print(f"⚠️ {name} 中不存在 'KMID' 列，未做裁剪。")

        next1_date_original_data = self.cli.get_orignal_data(
            dates={"start": next1_date, "end": next1_date}
        )
        next2_date_original_data = self.cli.get_orignal_data(
            dates={"start": next2_date, "end": next2_date}
        )

        print("分析 df_ret:")
        self.review_result_string += f"### {date_str}_ret.csv\n"
        df = self._review_csv(df_ret, real_df, next1_date_original_data, next2_date_original_data)
        self.review_result_df[subdir.name] = df

        print("分析 df_filter_ret:")
        self.review_result_string += f"### {date_str}_filter_ret.csv\n"
        df = self._review_csv(
            df_filter_ret, real_df, next1_date_original_data, next2_date_original_data
        )
        self.review_result_df_filter[subdir.name] = df

    # ---------- 最终结果落盘 ----------
    def save_review_result(self):
        review_dir = Path("../review_csv")
        review_dir.mkdir(parents=True, exist_ok=True)
        for name, df in self.review_result_df.items():
            df.to_csv(review_dir / f"{name}_ret.csv", index=True)
        for name, df in self.review_result_df_filter.items():
            df.to_csv(review_dir / f"{name}_filter_ret.csv", index=True)

    def _get_review_subdirs(self) -> list[Path] | None:
        """获取复盘用的子目录列表，按日期倒序。目录不存在时返回 None。"""
        base_dir = Path("../qlib_score_csv")
        if not base_dir.exists() or not base_dir.is_dir():
            print(f"⚠️ 目录不存在: {base_dir.resolve()}")
            return None

        subdirs = [d for d in base_dir.iterdir() if d.is_dir()]
        print(f"共发现 {len(subdirs)} 个子目录：")

        def extract_date(subdir: Path):
            m = re.match(r"selection_(\d{8})_", subdir.name)
            if m:
                return m.group(1)
            return ""

        return sorted(subdirs, key=extract_date, reverse=True)

    # ---------- 对外入口 ----------
    def review(self):
        """马后炮"""
        sorted_subdirs = self._get_review_subdirs()
        if sorted_subdirs is None:
            return

        for subdir in sorted_subdirs:
            self._review_subdir(subdir)

        print(self.review_result_string)
        append_to_file("/tmp/review_result.md", self.review_result_string, mmode="w")
        logger.info("review result saved to /tmp/review_result.md")

        self.save_review_result()
        logger.info("review result saved to ../review_csv")

        pprint(self.review_result_df)
        pprint(self.review_result_df_filter)

    def backtest(self):
        sorted_subdirs = self._get_review_subdirs()
        if sorted_subdirs is None:
            return
        date_list = [self._extract_date_from_csv_name(sorted_subdirs[-1]), self._extract_date_from_csv_name(sorted_subdirs[0])]
        logger.info(f"backtest data list: {date_list}")

        csi300_df = self.cli.get_real_label_csi300(dates={"start": date_list[0], "end": date_list[1]}).reset_index()
        csi300_df = csi300_df.rename(columns={"real_label": "csi300_real_label"})

        date_range_list = self.trade_date.get_date_range(date_list[0], date_list[1])

        real_df = self.cli.get_real_label(dates={"start": date_list[0], "end": date_list[1]})
        real_df = real_df.reset_index()
        real_df["datetime"] = pd.to_datetime(real_df["datetime"])
        real_label_map = real_df.set_index(["datetime", "instrument"])["real_label"]
        # 拿到 topk 的 实际 real_label 列表, 并计算出 每天的 平均收益 df_avg_profit
        # 两个: ret 和 filter_ret
        for subdir in sorted_subdirs:
            date_str = self._extract_date_from_csv_name(subdir)
            df_ret = pd.read_csv(subdir / f"{date_str}_ret.csv", parse_dates=["datetime"])
            # 直接覆盖原列，保持 real_label 列位置不变，避免 merge 产生 _x/_y 列
            df_ret["real_label"] = df_ret.set_index(["datetime", "instrument"]).index.map(real_label_map)

            df_filter_ret = pd.read_csv(subdir / f"{date_str}_filter_ret.csv", parse_dates=["datetime"])
            df_filter_ret["real_label"] = df_filter_ret.set_index(["datetime", "instrument"]).index.map(real_label_map)

            self.review_result_df[date_str] = df_ret
            self.review_result_df_filter[date_str] = df_filter_ret
        

        print(date_range_list)

        df_top10 = []
        for date in date_range_list:
            df_ret = self.review_result_df[date]
            # 获取df_ret的instrument排序前10名
            top10_instruments = df_ret['instrument'].head(10).tolist()
            # 计算 top10 instrument 的 avg_score 平均值
            avg_real_label = df_ret[df_ret['instrument'].isin(top10_instruments)]['real_label'].mean()
            # 根据 date 合并 csi300_df
            csi300_row = csi300_df[csi300_df['datetime'] == pd.to_datetime(date)]
            if not csi300_row.empty:
                csi300_label = csi300_row.iloc[0]["csi300_real_label"]
            else:
                csi300_label = None
            # 将每一行数据作为字典存入列表，最后汇总为一个 DataFrame
            row_dict = {'date': date}
            for i, inst in enumerate(top10_instruments):
                row_dict[f'top{i+1}'] = inst
            # 填充不足10只股票
            for i in range(len(top10_instruments), 10):
                row_dict[f'top{i+1}'] = None
            row_dict['avg_real_label'] = avg_real_label
            row_dict['csi300_real_label'] = csi300_label
            df_top10.append(row_dict)
        df_top10 = pd.DataFrame(df_top10)
        print(df_top10)