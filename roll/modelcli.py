from loguru import logger
from tabulate import tabulate
from utils import check_match_in_list, append_to_file, get_normalized_stock_list, filter_csv
import numpy as np
import pandas as pd
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

    def get_real_label(self):
        dates = self.kwargs['predict_dates'][0]
        df = D.features(D.instruments('all'), ['Ref($close, -2)/Ref($close, -1) - 1'], start_time=dates['start'], end_time=dates['end'], freq='day')
        df.columns = ['real_label']
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
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
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