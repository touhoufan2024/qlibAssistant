from loguru import logger
from utils import check_match_in_list
import numpy as np
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
import os
from tqdm import tqdm
from functools import partialmethod
# 强制禁用所有 tqdm 进度条
tqdm.__init__ = partialmethod(tqdm.__init__, disable=True)
from pprint import pprint
logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>"
)
from dataclasses import dataclass, field
from typing import List

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
        exp_name,
        step = 40,
        region=REG_CN,
        provider_uri="~/.qlib/qlib_data/cn_data",
        experiment_name="rolling_exp",
        uri_folder="~/.qlibAssistant/mlruns",
        **kwargs
    ):
        self.kwargs = kwargs
        self.exp_name = exp_name
        self.step = step
        exp_manager = C["exp_manager"]
        exp_manager["kwargs"]["uri"] = "file:" + str(Path(uri_folder).expanduser())
        logger.info(f"Experiment uri: {exp_manager['kwargs']['uri']}")
        qlib.init(provider_uri=provider_uri, region=region, exp_manager=exp_manager)

    def filter(self):
        f_list = self.kwargs['model_filter']

        exps = R.list_experiments()
        for a, b in exps.items():
            if a == 'Default':
                continue
            if not check_match_in_list(a, f_list):
                continue
            exp = R.get_exp(experiment_name=a)
            print(f"Experiment: {a} {exp.id}")

    def get_model_list(self):
        logger.info("get all model in the uri_folder:")
        exps = R.list_experiments()
        ret = []
        for a, b in exps.items():
            if a == 'Default':
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
        return ic_info

    def ls(self):
        logger.info("Listing all model in the uri_folder:")
        model_list = self.get_model_list()
        for mc in model_list:
            exp = R.get_exp(experiment_name=mc.exp_name)
            print(f"Experiment: {exp.name} {exp.id}")
            for rid in mc.rid:
                rec = exp.get_recorder(recorder_id=rid)
                task = rec.load_object("task")
                ic_info = self.get_ic_info(rec)
                data_train = task['dataset']['kwargs']['segments']['train']
                data_train_vec = [data_train[0].strftime("%Y-%m-%d"), data_train[1].strftime("%Y-%m-%d")]
                print("\t", rid, task["model"]['class'], task['dataset']['kwargs']['handler']['class'], ic_info, data_train_vec)