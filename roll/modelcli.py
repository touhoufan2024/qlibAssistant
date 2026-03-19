from loguru import logger
from utils import (
    check_match_in_list,
    append_to_file,
    get_normalized_stock_list,
)
import numpy as np
import pandas as pd
import qlib
from qlib.constant import REG_CN
from qlib.data import D
from qlib.workflow import R
from qlib.config import C
from pathlib import Path
from qlib.utils import init_instance_by_config
from tqdm import tqdm
from functools import partialmethod
from datetime import datetime
from qlib.contrib.data.handler import Alpha158, Alpha360
from dataclasses import dataclass, field
from typing import Dict, List

from model_backup import (
    compress_mlruns as _compress_mlruns,
    decompress_mlruns as _decompress_mlruns,
)
from model_review import ModelReviewHelper

# --- 常量定义：解决 Magic Strings 问题 ---
PARAMS_FILE = "params.pkl"
SIG_ANALYSIS_DIR = "sig_analysis"
REQUIRED_ARTIFACTS = [PARAMS_FILE, SIG_ANALYSIS_DIR]
DEFAULT_EXP_NAME = 'Default'

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
        # 复盘逻辑拆分到独立助手类，降低本文件认知复杂度
        self.reviewer = ModelReviewHelper(self)
        # 注意：dataclasses.field 只能用于 dataclass 字段，这里必须用普通 dict
        self.rid_rank_icir: Dict[str, float] = {}
        self.rid_weight: Dict[str, float] = {}

    @staticmethod
    def _round3(x: float) -> float:
        return float(np.around(float(x), 3))

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

            # 2. 遍历记录器（收集 rid + rank_icir）
            for rid in exp.list_recorders():
                recorder = exp.get_recorder(recorder_id=rid)
                if self._is_valid_recorder(recorder):
                    mc.rid.append(rid)
                    _, ic_list = self.get_ic_info(recorder)
                    self.rid_rank_icir[rid] = self._round3(ic_list[3])

            # 只有当这个实验下有符合条件的记录时才添加
            if mc.rid:
                ret.append(mc)
        # 通过 rank_icir 为 rid_weight 分配权重（归一化处理）
        total_rank_icir = sum(self.rid_rank_icir[rid] for mc in ret for rid in mc.rid)
        self.rid_weight = {}
        for mc in ret:
            for rid in mc.rid:
                if total_rank_icir != 0:
                    self.rid_weight[rid] = self._round3(self.rid_rank_icir[rid] / total_rank_icir)
                else:
                    self.rid_weight[rid] = self._round3(1.0 / (sum(len(mc.rid) for mc in ret) or 1))
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
            "train_time_vec": train_time_vec,
            "rank_icir": f"{self.rid_rank_icir[rec.id]:.3f}",
            "weight": f"{self.rid_weight[rec.id]:.3f}",
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

    def analysis(self):
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

                dataset = init_instance_by_config(dataset_config)
                pred_score = model.predict(dataset, segment="test")
                ret.append([mc.exp_name, rid, pred_score])
        return ret

    def selection(self):
        results = self.analysis()
        if results: self.collect(results)

    def collect(self, results):
        func_name = "selection"
        latest_stock_list = get_normalized_stock_list()

        processed_list = []
        for exp_name, rid, series_data in results:
            df = series_data.to_frame(name='score').reset_index()
            df['exp_name'], df['rid'] = exp_name, rid
            df['weight'] = self.rid_weight.get(rid, 0.0)
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

        self._save_results(df_final, func_name, latest_stock_list)

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

    def _save_results(self, df_final, func_name, latest_stock_list):
        base_dir = Path(self.kwargs['analysis_folder']).expanduser()
        save_dir = base_dir / f"{func_name}_{datetime.now().strftime('%Y%m%d_%H_%M_%S')}"
        save_dir.mkdir(parents=True, exist_ok=True)
        md_file = save_dir / "total.md"

        append_to_file(md_file, f"# params \n")
        append_to_file(md_file, f" {self.kwargs}\n\n")
        self._record_model_info(md_file)

        alpha158_df = self.get_alpha_data().reset_index()
        for date, group_df in df_final.groupby('datetime'):
            date_str = str(date.date())
            # 使用模型权重(基于 rid_rank_icir 归一化得到的 self.rid_weight)计算加权平均分
            group_df = group_df.copy()
            ret_df = (
                group_df.groupby('instrument')
                .apply(
                    lambda g: pd.Series(
                        {
                            "avg_score": (g['score'] * g['weight']).sum() / g['weight'].sum()
                            if g['weight'].sum() != 0
                            else g['score'].mean(),
                            "pos_ratio": (g['score'] > 0).mean(),
                        }
                    )
                )
                .reset_index()
            )

            cols_to_restore = ['instrument', 'real_label', 'error', 'abs_error']
            existing_cols = [c for c in cols_to_restore if c in group_df.columns]
            restore_df = group_df[existing_cols].drop_duplicates('instrument')
            ret_df = pd.merge(
                ret_df,
                restore_df,
                on='instrument',
                how='left',
                validate='one_to_one'
            )
            ret_df = ret_df.sort_values(by='avg_score', ascending=False)
            if latest_stock_list is not None:
                ret_df = pd.merge(ret_df, latest_stock_list, left_on='instrument', right_on='code', how='left', validate='one_to_one')

            ret_df = pd.merge(ret_df, alpha158_df[alpha158_df['datetime'] == date], on='instrument', how='left', validate='one_to_one')
            ret_filter_df = self.filter_ret_df(ret_df)
            ret_df.to_csv(save_dir / f"{date_str}_ret.csv", index=True, encoding="utf-8-sig")
            ret_filter_df = ret_filter_df.reset_index(drop=True)
            ret_filter_df.to_csv(save_dir / f"{date_str}_filter_ret.csv", index=True, encoding="utf-8-sig")

        df_final.to_csv(save_dir / "total.csv", index=True, encoding="utf-8-sig")

    def filter_ret_df(self, df):
        # 稳健性过滤逻辑
        df = df[(df['STD5'] < 0.10) & (df['STD20'] < 0.10) & (df['STD60'] < 0.10)]
        df = df[(df['STD60'] < 0.05) & (df['STD5'] < 0.06)]
        df = df[df['STD5'] < (df['STD60'] * 2)]
        df = df[(df['ROC10'] > 0.80) & (df['ROC20'] > 0.80) & (df['ROC60'] > 0.80)]
        return df[df['ROC20'] < 1.30]

    def get_real_label(self, dates = None, instruments='csi300'):
        if dates is None:
            dates = self.kwargs['predict_dates'][0]
        df = D.features(D.instruments(instruments), ['Ref($close, -2)/Ref($close, -1) - 1'], start_time=dates['start'], end_time=dates['end'], freq='day')
        df.columns = ['real_label']
        return df

    def get_real_label_csi300(self, dates = None):
        if dates is None:
            dates = self.kwargs['predict_dates'][0]
        df = D.features(['SH000300'], ['Ref($close, -2)/Ref($close, -1) - 1'], start_time=dates['start'], end_time=dates['end'], freq='day')
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

    def review(self):
        """马后炮：复盘逻辑委托给 ModelReviewHelper"""
        self.reviewer.review()

    def backtest(self):
        self.reviewer.backtest()

    def compress_mlruns(self):
        """调用独立的备份助手进行压缩"""
        _compress_mlruns(self.kwargs["provider_uri"])

    def decompress_mlruns(self):
        """调用独立的备份助手进行解压"""
        _decompress_mlruns()