from loguru import logger
from utils import check_match_in_list
import numpy as np
import pandas as pd
import sys
import qlib
from qlib.constant import REG_CN
from qlib.workflow import R
from qlib.config import C
from qlib.workflow.task.gen import RollingGen, task_generator
from qlib.workflow.task.manage import TaskManager, run_task
from qlib.workflow.task.collect import RecorderCollector
from qlib.model.ens.group import RollingGroup
from qlib.model.trainer import TrainerR, TrainerRM, task_train
from pathlib import Path
from myconfig import CSI300_RECORD_LGB_TASK_CONFIG, CSI100_RECORD_XGBOOST_TASK_CONFIG
from qlib.utils import init_instance_by_config
import os
from tqdm import tqdm
from functools import partialmethod
from pprint import pprint
logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>"
)
from dataclasses import dataclass, field
from typing import List
import logging

@dataclass
class ModelContext:
    exp_name: str
    rid: List[str] = field(default_factory=list)

class ModelCLI:
    """
    [子模块] 模型仓库: 管理历史模型切片
    """
    def __init__(
        self,
        region=REG_CN,
        provider_uri="~/.qlib/qlib_data/cn_data",
        **kwargs
    ):
        uri_folder = kwargs["uri_folder"]
        self.kwargs = kwargs
        exp_manager = C["exp_manager"]
        exp_manager["kwargs"]["uri"] = "file:" + str(Path(uri_folder).expanduser())
        logger.info(f"Experiment uri: {exp_manager['kwargs']['uri']}")
        qlib.init(provider_uri=provider_uri, region=region, exp_manager=exp_manager, n_jobs = 8) 

    def filter_rec(self, rec):
        ic_info, ic_list = self.get_ic_info(rec)
        ic_filter = self.kwargs['rec_filter']
        if not ic_filter:
            return True
        # print(ic_list, ic_filter)
        all_passed = all(val > list(d.values())[0] for val, d in zip(ic_list, ic_filter))
        # print("all_passed:", all_passed)
        if not all_passed:
            return False
        return True

    def get_model_list(self):
        logger.info("get all model in the uri_folder:")
        f_list = self.kwargs['model_filter']
        exps = R.list_experiments()
        ret = []
        for a, b in exps.items():
            if a == 'Default':
                continue
            if not check_match_in_list(a, f_list):
                continue
            mc =  ModelContext(a) 
            exp = R.get_exp(experiment_name=a)
            for rid in exp.list_recorders():
                rec = exp.get_recorder(recorder_id=rid)
                if not rec.list_artifacts():
                    continue
                lista = rec.list_artifacts()
                if "params.pkl" not in lista or "sig_analysis" not in lista:
                    continue
                if not self.filter_rec(rec):
                    continue
                mc.rid.append(rid)
            ret.append(mc)
        return ret

    def get_ic_info(self, rec):
        ic = rec.load_object("sig_analysis/ic.pkl")
        ric = rec.load_object("sig_analysis/ric.pkl")
        IC = ic.mean()
        ICIR = ic.mean() / ic.std()
        RankIC = ric.mean()
        RankICIR = ric.mean() / ric.std()

        ic_info = {
            "IC": float(np.around(IC, 3)),
            "ICIR": float(np.around(ICIR, 3)),
            "Rank IC": float(np.around(RankIC, 3)),
            "Rank ICIR": float(np.around(RankICIR, 3)),
        }
        return ic_info, [IC, ICIR, RankIC, RankICIR]

    def get_train_time(self, rec):
        task = rec.load_object("task")
        start_time = rec.info['start_time'].split()[0]
        end_time = rec.info['end_time'].split()[0]
        data_train = task['dataset']['kwargs']['segments']['train']
        data_train_vec = [data_train[0].strftime("%Y-%m-%d"), data_train[1].strftime("%Y-%m-%d")]
        train_time_vec = [start_time, end_time]
        return data_train_vec, train_time_vec

    def print_rec(self, rec):
        task = rec.load_object("task")
        ic_info, ic_list = self.get_ic_info(rec)
        data_train_vec, train_time_vec = self.get_train_time(rec)
        print("\t", rec.id, task["model"]['class'], task['dataset']['kwargs']['handler']['class'], ic_info, data_train_vec, train_time_vec)
        # print(task)


    def ls(self, all=False):
        tqdm.__init__ = partialmethod(tqdm.__init__, disable=True)
        logger.info("Listing all model in the uri_folder:")
        model_list = self.get_model_list()
        for mc in model_list:
            exp = R.get_exp(experiment_name=mc.exp_name)
            count = len(mc.rid)
            print(f"Experiment: {exp.name} {exp.id} (Recorders: {count}/{len(exp.list_recorders())})")
            if all:
                for rid in mc.rid:
                    rec = exp.get_recorder(recorder_id=rid)
                    self.print_rec(rec)

    def clean(self):
        logger.info("清除无效的exp_name 和 rec:")
        exps = R.list_experiments()
        for name in exps:
            if name == 'Default':
                continue
            exp = R.get_exp(experiment_name=name)
            if len(exp.list_recorders()) == 0:
                logger.info(f"删除 Experiment: {name} {exp.id}")
                R.delete_exp(experiment_name=name)
                continue
            for rid in exp.list_recorders():
                rec = exp.get_recorder(recorder_id=rid)
                if (not rec.list_artifacts()) or ("params.pkl" not in rec.list_artifacts()) or ("sig_analysis" not in rec.list_artifacts()):
                    logger.info(f"Experiment: {name} 删除 Recorder: {rid} ")
                    exp.delete_recorder(rid)

    def anilysis(self, stock_list = None):
        """
        模型分析, 问股或者选股
        """
        logger.info("This is a placeholder for the analysis method.")
        logger.info(f"股票列表: {stock_list}")

        model_list = self.get_model_list()
        for mc in model_list:
            exp = R.get_exp(experiment_name=mc.exp_name)
            print(f"Experiment: {exp.name} {exp.id}")
            for rid in mc.rid:
                rec = exp.get_recorder(recorder_id=rid)
                task = rec.load_object("task")

                model = rec.load_object("params.pkl")
                logger.info(f"模型加载成功:{rec.id}")
                self.print_rec(rec)
                # print(rec.load_object("task"))
                dataset_config = task['dataset']
                # pprint(dataset_config)

                predict_date1 = pd.Timestamp(self.kwargs['predict_dates'][0]['start'])
                predict_date2 = pd.Timestamp(self.kwargs['predict_dates'][0]['end'])
                dataset_config['kwargs']['segments']['test'] = (predict_date1, predict_date2)
                dataset_config['kwargs']['handler']['kwargs']['end_time'] = predict_date2
                if stock_list is not None:
                    dataset_config['kwargs']['handler']['kwargs']['instruments'] = stock_list
                # pprint(dataset_config)

                dataset = init_instance_by_config(dataset_config)

                logger.info("数据集加载成功")
                # example_df = dataset.prepare("test")
                # print(example_df.head())
                pred_score = model.predict(dataset, segment="test")
                pprint(pred_score)

    def inquiry(self):
        """
        问股, 分析股票列表的 score
        """
        logger.info("This is a placeholder for the inquiry method.")
        stock_list = self.kwargs['stock_list']
        self.anilysis(stock_list=stock_list)

    def selection(self):
        """
        选股, 分析csi300成分股的 score
        """
        logger.info("This is a placeholder for the selection method.")
        self.anilysis(stock_list=None)