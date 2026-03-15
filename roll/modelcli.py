from loguru import logger
from tabulate import tabulate
from utils import check_match_in_list, append_to_file, get_normalized_stock_list, filter_csv, get_local_data_date, get_trade_data
import numpy as np
import pandas as pd
import re
import sys
import qlib
from qlib.constant import REG_CN
from qlib.data import D
from qlib.workflow import R
from qlib.config import C
from pathlib import Path
from qlib.utils import init_instance_by_config
import os
from tqdm import tqdm
from functools import partialmethod
from pprint import pprint
from datetime import datetime
from qlib.contrib.data.handler import Alpha158, Alpha360
from dataclasses import dataclass, field
from typing import List
import logging
import tarfile

# --- 常量定义：解决 Magic Strings 问题 ---
PARAMS_FILE = "params.pkl"
SIG_ANALYSIS_DIR = "sig_analysis"
REQUIRED_ARTIFACTS = [PARAMS_FILE, SIG_ANALYSIS_DIR]
DEFAULT_EXP_NAME = 'Default'

# 路径配置：自动识别不同机器的 Home 目录
HOME = Path.home()
# 源目录: ~/.qlibAssistant/mlruns
TARGET_PARENT = HOME / ".qlibAssistant"
SOURCE_DIR = TARGET_PARENT / "mlruns"
# 存放压缩包的目录: ../model_pkl
BACKUP_DIR = Path("../model_pkl").resolve()

@dataclass
class ModelContext:
    exp_name: str
    rid: List[str] = field(default_factory=list)

class ModelCLI:
    """
    [子模块] 模型仓库: 管理历史模型切片
    """
    def __init__(self, region=REG_CN, **kwargs):
        self.kwargs = kwargs
        self._init_qlib(region)
        self.review_result_string = "# 复盘统计分析\n"
        self.review_result_string += f"\n 统计时间 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

    def _init_qlib(self, region):
        """初始化 Qlib 配置"""
        uri_folder = self.kwargs.get("uri_folder")
        provider_uri = self.kwargs.get("provider_uri")
        exp_manager = C["exp_manager"]
        exp_manager["kwargs"]["uri"] = "file:" + str(Path(uri_folder).expanduser())
        logger.info(f"Experiment uri: {exp_manager['kwargs']['uri']}")
        qlib.init(provider_uri=provider_uri, region=region, exp_manager=exp_manager)

    def filter_rec(self, rec):
        _, ic_list = self.get_ic_info(rec)
        ic_filter = self.kwargs.get('rec_filter')
        if not ic_filter:
            return True
        # 使用 all() 简化逻辑判断
        return all(val > list(d.values())[0] for val, d in zip(ic_list, ic_filter))

    def _is_valid_recorder(self, recorder):
        """
        辅助方法：判定一个 recorder 是否符合条件 (降低认知复杂度的核心)
        """
        artifacts = recorder.list_artifacts()
        # 使用 all() 检查所有必要产物是否存在，消除硬编码字符串
        if not artifacts or not all(f in artifacts for f in REQUIRED_ARTIFACTS):
            return False
        return self.filter_rec(recorder)

    def get_model_list(self):
        """
        获取模型列表：通过 Early Return 和辅助函数降低嵌套层级
        """
        uri_folder = self.kwargs.get('uri_folder')
        model_filter = self.kwargs.get('model_filter')
        logger.info(f"get all model in the uri_folder: {uri_folder}")

        exps = R.list_experiments()
        ret = []

        for name in exps:
            # 1. 基础过滤：排除默认项目和不匹配的项目
            if name == DEFAULT_EXP_NAME or not check_match_in_list(name, model_filter):
                continue

            exp = R.get_exp(experiment_name=name)
            mc = ModelContext(name)

            # 2. 遍历记录器
            for rid in exp.list_recorders():
                recorder = exp.get_recorder(recorder_id=rid)
                if self._is_valid_recorder(recorder):
                    mc.rid.append(rid)

            # 只有当这个实验下有符合条件的记录时才添加
            if mc.rid:
                ret.append(mc)

        self._log_summary(ret)
        return ret

    def _log_summary(self, ret):
        """日志输出逻辑抽离"""
        model_filter = self.kwargs.get('model_filter')
        rec_filter = self.kwargs.get('rec_filter')
        total_rids = sum(len(mc.rid) for mc in ret)
        logger.info(f"model_filter {model_filter}, rec_filter {rec_filter}")
        logger.info(f"experiment num: {len(ret)}, rid num: {total_rids}")

    def get_ic_info(self, rec):
        ic_pkl = rec.load_object(f"{SIG_ANALYSIS_DIR}/ic.pkl")
        ric_pkl = rec.load_object(f"{SIG_ANALYSIS_DIR}/ric.pkl")
        ic, rank_ic = ic_pkl.mean(), ric_pkl.mean()
        icir, rank_icir = ic / ic_pkl.std(), rank_ic / ric_pkl.std()

        ic_info = {
            "IC": float(np.around(ic, 3)),
            "ICIR": float(np.around(icir, 3)),
            "Rank IC": float(np.around(rank_ic, 3)),
            "Rank ICIR": float(np.around(rank_icir, 3)),
        }
        return ic_info, [ic, icir, rank_ic, rank_icir]

    def get_train_time(self, rec):
        task = rec.load_object("task")
        start_time = rec.info['start_time'].split()[0]
        end_time = rec.info['end_time'].split()[0]
        data_train = task['dataset']['kwargs']['segments']['train']
        return [data_train[0], data_train[1]], [start_time, end_time]

    def print_rec(self, rec):
        task = rec.load_object("task")
        ic_info, _ = self.get_ic_info(rec)
        data_train_vec, train_time_vec = self.get_train_time(rec)
        info = {
            "id": rec.id,
            "model": task["model"]['class'],
            "dataset": task['dataset']['kwargs']['handler']['class'],
            "ic_info": ic_info,
            "data_train_vec": data_train_vec,
            "train_time_vec": train_time_vec
        }
        print(info)
        return info

    def ls(self, all=False):
        tqdm.__init__ = partialmethod(tqdm.__init__, disable=True)
        logger.info("Listing all model in the uri_folder:")
        model_list = self.get_model_list()
        for mc in model_list:
            exp = R.get_exp(experiment_name=mc.exp_name)
            print(f"Experiment: {exp.name} {exp.id} (Recorders: {len(mc.rid)}/{len(exp.list_recorders())})")
            if all:
                for rid in mc.rid:
                    self.print_rec(exp.get_recorder(recorder_id=rid))

    def clean(self):
        logger.info("清除无效的exp_name 和 rec:")
        exps = R.list_experiments()
        for name in exps:
            if name == DEFAULT_EXP_NAME:
                continue
            exp = R.get_exp(experiment_name=name)
            recorders = exp.list_recorders()
            if not recorders:
                logger.info(f"删除 Experiment: {name} {exp.id}")
                R.delete_exp(experiment_name=name)
                continue
            for rid in recorders:
                if not self._is_valid_recorder(exp.get_recorder(recorder_id=rid)):
                    logger.info(f"Experiment: {name} 删除 Recorder: {rid} ")
                    exp.delete_recorder(rid)

    def analysis(self, stock_list=None):
        logger.info(f"股票列表: {stock_list}")
        ret = []
        model_list = self.get_model_list()
        for mc in model_list:
            exp = R.get_exp(experiment_name=mc.exp_name)
            for rid in mc.rid:
                rec = exp.get_recorder(recorder_id=rid)
                task = rec.load_object("task")
                model = rec.load_object(PARAMS_FILE)
                self.print_rec(rec)

                dataset_config = task['dataset']
                p_dates = self.kwargs['predict_dates'][0]
                predict_date1, predict_date2 = pd.Timestamp(p_dates['start']), pd.Timestamp(p_dates['end'])

                dataset_config['kwargs']['segments']['test'] = (predict_date1, predict_date2)
                dataset_config['kwargs']['handler']['kwargs']['end_time'] = predict_date2
                if stock_list:
                    dataset_config['kwargs']['handler']['kwargs']['instruments'] = stock_list

                dataset = init_instance_by_config(dataset_config)
                pred_score = model.predict(dataset, segment="test")
                ret.append([mc.exp_name, rid, pred_score])
        return ret

    def inquiry(self):
        results = self.analysis(stock_list=self.kwargs.get('stock_list', []))
        if results: self.collect(results, stock_list=self.kwargs.get('stock_list'))

    def selection(self):
        results = self.analysis()
        if results: self.collect(results)

    def collect(self, results, stock_list=None):
        func_name = "inquiry" if stock_list else "selection"
        latest_stock_list = get_normalized_stock_list()

        processed_list = []
        for exp_name, rid, series_data in results:
            df = series_data.to_frame(name='score').reset_index()
            df['exp_name'], df['rid'] = exp_name, rid
            processed_list.append(df)

        df_final = pd.concat(processed_list, axis=0, ignore_index=True)
        df_final['datetime'] = pd.to_datetime(df_final['datetime'])
        df_final = df_final.sort_values(by='datetime')

        real_df = self.get_real_label()
        label_clean = real_df.reset_index()
        label_clean = label_clean[['datetime', 'instrument', 'real_label']]
        df_final['datetime'] = pd.to_datetime(df_final['datetime'])
        label_clean['datetime'] = pd.to_datetime(label_clean['datetime'])
        result_df = pd.merge(
            df_final,
            label_clean,
            on=['datetime', 'instrument'],
            how='left',
            validate="many_to_one" # df_fainal 是 多个 模型预测的结果, label_clean 是 每个股票每天一个真实结果
        )
        result_df['error'] = result_df['score'] - result_df['real_label']
        result_df['abs_error'] = result_df['error'].abs()
        df_final = result_df
        print(result_df.head())

        self._save_results(df_final, func_name, stock_list, latest_stock_list)

    def _record_model_info(self, md_file = "model_info.md"):
        print(f"record model info to {md_file}")
        append_to_file(md_file, f"\n\n # model info \n\n")
        model_list = self.get_model_list()
        for mc in model_list:
            exp = R.get_exp(experiment_name=mc.exp_name)
            print(f"Experiment: {exp.name} {exp.id} (Recorders: {len(mc.rid)}/{len(exp.list_recorders())})")
            append_to_file(md_file, f"Experiment: {exp.name} {exp.id} (Recorders: {len(mc.rid)}/{len(exp.list_recorders())})\n")
            for rid in mc.rid:
                info = self.print_rec(exp.get_recorder(recorder_id=rid))
                append_to_file(md_file, f"\n\tRecorder: {rid}\n")
                append_to_file(md_file, f"\n\t\tModel: {info}\n")

    def _save_results(self, df_final, func_name, stock_list, latest_stock_list):
        base_dir = Path(self.kwargs['analysis_folder']).expanduser()
        save_dir = base_dir / f"{func_name}_{datetime.now().strftime('%Y%m%d_%H_%M_%S')}"
        save_dir.mkdir(parents=True, exist_ok=True)
        md_file = save_dir / "total.md"

        append_to_file(md_file, f"# params \n")
        append_to_file(md_file, f" {self.kwargs}\n\n")
        self._record_model_info(md_file)

        if stock_list:
            for stock in stock_list:
                res = df_final[df_final['instrument'] == stock]
                append_to_file(md_file, f"\n\n # {stock}\n\n{res.to_markdown(index=False)}\n\n")
        else:
            alpha158_df = self.get_alpha_data().reset_index()
            for date, group_df in df_final.groupby('datetime'):
                date_str = str(date.date())
                ret_df = group_df.groupby('instrument')['score'].agg(avg_score='mean', pos_ratio=lambda x: (x > 0).mean()).reset_index()

                cols_to_restore = ['instrument', 'real_label', 'error', 'abs_error']
                # 确保这些列在 group_df 中确实存在
                existing_cols = [c for c in cols_to_restore if c in group_df.columns]
                # 获取唯一的映射关系
                restore_df = group_df[existing_cols].drop_duplicates('instrument')
                # 重新合并回来
                ret_df = pd.merge(
                    ret_df,
                    restore_df,
                    on='instrument',
                    how='left',
                    validate='one_to_one'  # 确保一对一，防止重复
                )
                ret_df = ret_df.sort_values(by='avg_score', ascending=False)
                if latest_stock_list is not None:
                    ret_df = pd.merge(ret_df, latest_stock_list, left_on='instrument', right_on='code', how='left', validate='one_to_one')

                ret_df = pd.merge(ret_df, alpha158_df[alpha158_df['datetime'] == date], on='instrument', how='left', validate='one_to_one')
                ret_filter_df = self.filter_ret_df(ret_df)
                ret_df.to_csv(save_dir / f"{date_str}_ret.csv", index=False, encoding="utf-8-sig")
                ret_filter_df.to_csv(save_dir / f"{date_str}_filter_ret.csv", index=False, encoding="utf-8-sig")

        df_final.to_csv(save_dir / "total.csv", index=False, encoding="utf-8-sig")

    def filter_ret_df(self, df):
        # 稳健性过滤逻辑
        df = df[(df['STD5'] < 0.10) & (df['STD20'] < 0.10) & (df['STD60'] < 0.10)]
        df = df[(df['STD60'] < 0.05) & (df['STD5'] < 0.06)]
        df = df[df['STD5'] < (df['STD60'] * 2)]
        df = df[(df['ROC10'] > 0.80) & (df['ROC20'] > 0.80) & (df['ROC60'] > 0.80)]
        return df[df['ROC20'] < 1.30]

    def get_real_label(self, dates = None):
        if dates is None:
            dates = self.kwargs['predict_dates'][0]
        df = D.features(D.instruments('all'), ['Ref($close, -2)/Ref($close, -1) - 1'], start_time=dates['start'], end_time=dates['end'], freq='day')
        df.columns = ['real_label']
        return df

    def get_orignal_data(self, dates=None, instruments='csi300'):
        if dates is None:
            dates = self.kwargs['predict_dates'][0]
        fields = [
            '$close * $factor', 
            '$open * $factor', 
            '$high * $factor', 
            '$low * $factor',
        ]

        df = D.features(
            D.instruments(instruments),
            fields,
            start_time=dates['start'],
            end_time=dates['end'],
            freq='day'
        )
        df.columns = ['close', 'open', 'high', 'low']
        df = df.reset_index()
        # 检查返回结果是否为空，并提醒用户
        if df.empty:
            print(f"数据为空, 请检查参数: instruments={instruments}, dates={dates}")
        return df

    def get_alpha_data(self, name="Alpha158"):
        dates = self.kwargs['predict_dates'][0]
        handler_kwargs = {"instruments": "csi300", "start_time": dates['start'], "end_time": dates['end'], "infer_processors": []}
        handler = Alpha158(**handler_kwargs) if name == "Alpha158" else Alpha360(**handler_kwargs)
        return handler.fetch(col_set="feature")

    def compress_mlruns(self):
        """压缩 ~/.qlibAssistant/mlruns 到 ../model_pkl/mlruns_yyyyMMdd_HHmm.tar.gz"""
        if not SOURCE_DIR.exists():
            print(f"⚠️ 找不到路径: {SOURCE_DIR}，跳过压缩。")
            return

        # 确保目标文件夹存在
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)

        # 精确到分钟的时间戳
        timestamp = get_local_data_date(self.kwargs['provider_uri']).strip()
        archive_path = BACKUP_DIR / f"mlruns_{timestamp}.tar.gz"

        print(f"📦 正在打包: {SOURCE_DIR} -> {archive_path.name}")
        with tarfile.open(archive_path, "w:gz") as tar:
            # arcname="mlruns" 保证解压后文件夹名字正确
            tar.add(SOURCE_DIR, arcname=SOURCE_DIR.name)
        print("✅ 压缩完成。")

    def decompress_mlruns(self):
        """解压 ../model_pkl/ 下所有 mlruns_*.tar.gz 到 ~/.qlibAssistant/"""
        if not BACKUP_DIR.exists():
            print(f"⚠️ 备份目录 {BACKUP_DIR} 不存在。")
            return

        # 确保父目录 ~/.qlibAssistant 存在
        TARGET_PARENT.mkdir(parents=True, exist_ok=True)

        # 获取目录下所有匹配的压缩包
        archives = list(BACKUP_DIR.glob("mlruns_*.tar.gz"))

        if not archives:
            print("ℹ️ 没有发现可供恢复的压缩包。")
            return

        for archive in archives:
            print(f"📂 正在解压: {archive.name} -> {TARGET_PARENT}")
            with tarfile.open(archive, "r:gz") as tar:
                # 解压到 ~/.qlibAssistant/，会自动还原 mlruns 文件夹
                tar.extractall(path=TARGET_PARENT)

        print("✅ 恢复完成。")

    def _review_csv(self, df, real_df, n1, n2):
        df = df[df["avg_score"] > 0].copy()  # 避免 SettingWithCopyWarning
        real_map = real_df.drop_duplicates('instrument').set_index('instrument')['real_label']
        df['real_label'] = df['instrument'].map(real_map)

        df['error'] = df['avg_score'] - df['real_label']
        df['abs_error'] = df['error'].abs()

        date_str = df['datetime'].iloc[0]
        print(f"分析 {date_str} csv")

        # 把 n1 的 close 和 n2 的 high 按照 instrument 合并到 df 里面，且名称叫做 n1close n2high
        # n1: DataFrame, 包含 'instrument', 'close'
        # n2: DataFrame, 包含 'instrument', 'high'

        n1_renamed = n1[['instrument', 'close']].rename(columns={'close': 'n1close'})
        n2_renamed = n2[['instrument', 'high']].rename(columns={'high': 'n2high'})

        df = df.merge(n1_renamed, on='instrument', how='left')
        df = df.merge(n2_renamed, on='instrument', how='left')

        top_num_list = [10, 20, 30, 50, 80, 100]
        profit_num_list = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10]

        # 使用一个 DataFrame 记录循环里的统计信息
        import pandas as pd
        # 这里用于保存结果，每个 top 如 Top10/Top30... 对应一个 list: 1%~10%止盈胜率, 持有一天平均收益, 持有一天正收益率
        topk_result_dict = {
            # 示例结构: "Top10": [止盈1%, 止盈2%, ..., 止盈10%, 持有一天平均收益, 一天正收益占比]
        }
        topk_result_index = ["止盈1%胜率", "止盈2%胜率", "止盈3%胜率", "止盈4%胜率", "止盈5%胜率", "止盈6%胜率", "止盈7%胜率", "止盈8%胜率", "止盈9%胜率", "止盈10%胜率", "持有一天平均收益", "一天正收益占比"]
        for top_num in top_num_list:  # 遍历 top 数字
            topk_df = df.sort_values(by='avg_score', ascending=False).head(top_num)
            topk_avg_profit = topk_df['real_label'].mean()
            topk_radio = ((topk_df['real_label'] * topk_df['avg_score']) > 0).sum() / len(topk_df)
            profit_list = []
            for profit_num in profit_num_list:  # 遍历止盈比例 0.01 0.02 .. 0.1
                topk_df_profit = (topk_df['n2high'] > topk_df['n1close'] * (1 + profit_num)).sum() / len(topk_df)
                profit_list.append(topk_df_profit)
            # 持有一天平均收益, 一天正收益占比 也加进去
            profit_list.append(topk_avg_profit)
            profit_list.append(topk_radio)
            topk_result_dict[f"Top{top_num}"] = profit_list
        topk_result_df = pd.DataFrame(topk_result_dict, index=topk_result_index)
        topk_result_df.index.name = date_str
        # 将所有数值转为百分比字符串（保留两位小数），仅对float类型进行格式化
        def to_percent(val):
            if isinstance(val, float) or isinstance(val, int):
                return f"{val*100:.2f}%"
            else:
                return val
        pct_df = topk_result_df.applymap(to_percent)
        print(pct_df.to_markdown(index=True))

        self.review_result_string += pct_df.to_markdown(index=True) + "\n"
        return pct_df

    def _review_subdir(self, subdir):
        print(f"- {subdir.name}")
        self.review_result_string += f"## {subdir.name}\n"
        # 优化：集中提取日期，减少冗余检查
        date_str = next(
            (
                re.match(r"(\d{4}-\d{2}-\d{2})_.*\.csv", file.name).group(1)
                for file in subdir.iterdir()
                if file.is_file() and re.match(r"(\d{4}-\d{2}-\d{2})_.*\.csv", file.name)
            ),
            None,
        )
        if date_str:
            print(f"直接从文件名提取的日期: {date_str}")
        else:
            print("未发现格式为 xxxx-xx-xx_ 的 CSV 文件名")

        trade_data_list = get_trade_data(self.kwargs.get("provider_uri"))
        if date_str and trade_data_list and date_str in trade_data_list[-2:]:
            logger.info(f"还不能复盘 {date_str}")
            self.review_result_string += f"\n{subdir.name} 还不能复盘 {date_str}\n"
            return

        next1_date = None
        if date_str and trade_data_list:
            try:
                idx = trade_data_list.index(date_str)
                if idx + 1 < len(trade_data_list):
                    next1_date = trade_data_list[idx + 1]
            except ValueError:
                next1_date = None

        next2_date = None
        if next1_date and trade_data_list:
            try:
                idx = trade_data_list.index(next1_date)
                if idx + 1 < len(trade_data_list):
                    next2_date = trade_data_list[idx + 1]
            except ValueError:
                next2_date = None

        logger.info(f"开始复盘 {date_str if date_str else '[未知日期]'}  btw:[下1个交易日: {next1_date if next1_date else '[未知日期]'}  下2个交易日: {next2_date if next2_date else '[未知日期]'}]")
        df_filter_ret, df_ret = None, None
        if date_str:
            filter_ret_path = subdir / f"{date_str}_filter_ret.csv"
            ret_path = subdir / f"{date_str}_ret.csv"

            # 读取 filter_ret
            if filter_ret_path.exists():
                try:
                    df_filter_ret = pd.read_csv(filter_ret_path)
                    print(f"已读取: {filter_ret_path.name}, 行数: {len(df_filter_ret)}")
                except Exception as e:
                    print(f"读取 {filter_ret_path.name} 出错: {e}")
            else:
                print(f"  未找到: {filter_ret_path.name}")

            # 读取 ret
            if ret_path.exists():
                try:
                    df_ret = pd.read_csv(ret_path)
                    print(f"已读取: {ret_path.name}, 行数: {len(df_ret)}")
                except Exception as e:
                    print(f"读取 {ret_path.name} 出错: {e}")
            else:
                print(f"未找到: {ret_path.name}")

        real_df = self.get_real_label(dates={"start": date_str, "end": date_str})
        real_df = real_df.reset_index()

        # 删除 'KMID' 及其右侧所有表项（包含 KMID）
        for name, df in [('df_ret', df_ret), ('df_filter_ret', df_filter_ret)]:
            if df is not None and not df.empty:
                if 'KMID' in df.columns:
                    kmid_idx = df.columns.get_loc('KMID')
                    # 只保留 KMID 左侧的所有列（不包含 KMID 本身）
                    if name == 'df_ret':
                        df_ret = df.iloc[:, :kmid_idx]
                    else:
                        df_filter_ret = df.iloc[:, :kmid_idx]
                else:
                    print(f"⚠️ {name} 中不存在 'KMID' 列，未做裁剪。")

        next1_date_original_data = self.get_orignal_data(dates={"start": next1_date, "end": next1_date})
        next2_date_original_data = self.get_orignal_data(dates={"start": next2_date, "end": next2_date})

        print("分析 df_ret:")
        self.review_result_string += f"### {date_str}_ret.csv\n"
        self._review_csv(df_ret, real_df, next1_date_original_data, next2_date_original_data)

        print("分析 df_filter_ret:")
        self.review_result_string += f"### {date_str}_filter_ret.csv\n"
        self._review_csv(df_filter_ret, real_df, next1_date_original_data, next2_date_original_data)

    def review(self):
        """马后炮"""
        base_dir = Path("../qlib_score_csv")
        if not base_dir.exists() or not base_dir.is_dir():
            print(f"⚠️ 目录不存在: {base_dir.resolve()}")
            return

        subdirs = [d for d in base_dir.iterdir() if d.is_dir()]
        print(f"共发现 {len(subdirs)} 个子目录：")
        # 按照日期从新到旧遍历
        def extract_date(subdir):
            import re
            m = re.match(r"selection_(\d{8})_", subdir.name)
            if m:
                return m.group(1)
            return ""  # 未识别返回空字符串，排在后面

        sorted_subdirs = sorted(
            subdirs,
            key=lambda d: extract_date(d),
            reverse=True  # 从新到旧
        )
        for subdir in sorted_subdirs:
            self._review_subdir(subdir)
        print(self.review_result_string)
        append_to_file("/tmp/review_result.md", self.review_result_string, mmode='w')
        logger.info(f"review result saved to /tmp/review_result.md")