
from abc import ABC, abstractmethod
from utils import get_config
import os
from loguru import logger
import requests
import subprocess
import utils
import qlib
import pandas as pd
from qlib.constant import REG_CN
from qlib.utils import init_instance_by_config, flatten_dict
from qlib.workflow import R
from qlib.config import C
from qlib.workflow.record_temp import SignalRecord, PortAnaRecord, SigAnaRecord
from qlib.tests.data import GetData
from qlib.tests.config import CSI300_BENCH, CSI300_GBDT_TASK

from qlib.contrib.report import analysis_model, analysis_position

from loguru import logger

from dataclasses import dataclass, field
from typing import List

# 统计 某个mlrun目录内的结果
# 重点关注的内容有 label 的排序, 以及性能的排序

class Collector(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def analysis(self):
        pass

@dataclass
class ExperimentInfo:
    id: str
    name: str
    recorders: List[str] = field(default_factory=list)

    def set_recorder(self, recorder):
        self.recorder = recorder

    def load_pkl(self):
        self.pred_df = self.recorder.load_object("pred.pkl")
        self.ic_data = self.recorder.load_object("sig_analysis/ic.pkl")
        self.ric_data = self.recorder.load_object("sig_analysis/ric.pkl")
        self.indicators_normal_1day_obj = self.recorder.load_object("portfolio_analysis/indicators_normal_1day_obj.pkl")
        self.report_normal_1day_df = self.recorder.load_object("portfolio_analysis/report_normal_1day.pkl")
        self.positions_normal_1day = self.recorder.load_object("portfolio_analysis/positions_normal_1day.pkl")
        self.indicators_normal_1day = self.recorder.load_object("portfolio_analysis/indicators_normal_1day.pkl") # 注意这个和上面的 _obj 区分开
        self.port_analysis_1day_df = self.recorder.load_object("portfolio_analysis/port_analysis_1day.pkl")
        self.indicator_analysis_1day_df = self.recorder.load_object("portfolio_analysis/indicator_analysis_1day.pkl")
        self.label_df = self.recorder.load_object("label.pkl")
        self.params_data = self.recorder.load_object("params.pkl")

class CollectorMlrunDir(Collector):
    def __init__(self, config):
        super().__init__(config)
        self.config = config
        self.experiment_list: List[ExperimentInfo] = []
    
    def qlib_init(self, mlrun_dir = "../mlruns"):
        logger.info(f"Initializing Qlib with mlrun dir: {mlrun_dir}")
        provider_uri = "~/.qlib/qlib_data/cn_data"  # target_dir
        exp_manager = C["exp_manager"]
        # exp_manager["kwargs"]["uri"] = "file:" + self.config.get_output_folder()
        exp_manager["kwargs"]["uri"] = "file:" + mlrun_dir
        qlib.init(provider_uri=provider_uri, region=REG_CN, exp_manager=exp_manager)

    def get_all_exps(self):
        exps = R.list_experiments()
        for a, b in exps.items():
            exp_info = ExperimentInfo(id=b.id, name=b.name, recorders=b.info['recorders'])
            self.experiment_list.append(exp_info)

    def show_all_exps(self):
        logger.info(f"Found {len(self.experiment_list)} experiments:")
        for exp in self.experiment_list:
            logger.info(f"Experiment ID: {exp.id}, Name: {exp.name}, Recorders: {exp.recorders}")
            expp = R.get_exp(experiment_name=exp.name, create=False)
            rec = expp.get_recorder(recorder_id=exp.recorders[0])
            exp.set_recorder(rec)

    def load_all_pkls(self):
        logger.info("Loading PKL files for all experiments...")
        for exp in self.experiment_list:
            logger.info(f"Loading PKL files for Experiment ID: {exp.id}, Name: {exp.name} rid: {exp.recorder.id}..")
            exp.load_pkl()

    def analysis(self, mlrun_dir=None):
        if mlrun_dir is None:
            mlrun_dir = self.config.get_output_folder()
        logger.info(f"Analyzing mlrun dir: {mlrun_dir} ...")
        self.qlib_init(mlrun_dir)
        self.get_all_exps()
        self.show_all_exps()
        self.load_all_pkls()


if __name__ == "__main__":
    cfig = utils.ConfigLoader()
    coll = CollectorMlrunDir(cfig)
    coll.analysis("/home/ash/.qlibAssistant/2025-11-26-21/")
