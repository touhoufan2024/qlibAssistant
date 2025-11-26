
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

    def analysis(self, mlrun_dir=None):
        if mlrun_dir is None:
            mlrun_dir = self.config.get_output_folder()
        logger.info(f"Analyzing mlrun dir: {mlrun_dir} ...")
        self.qlib_init(mlrun_dir)
        self.get_all_exps()
        self.show_all_exps()


if __name__ == "__main__":
    cfig = utils.ConfigLoader()
    coll = CollectorMlrunDir(cfig)
    coll.analysis("/home/ash/.qlibAssistant/2025-11-26-16/")
