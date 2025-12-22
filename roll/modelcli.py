from loguru import logger
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
        self.exp_name = exp_name
        self.step = step
        exp_manager = C["exp_manager"]
        exp_manager["kwargs"]["uri"] = "file:" + str(Path(uri_folder).expanduser())
        logger.info(f"Experiment uri: {exp_manager['kwargs']['uri']}")
        qlib.init(provider_uri=provider_uri, region=region, exp_manager=exp_manager)

    def best(self, window=3, metric="IC"):
        """获取当前表现最好的模型"""
        logger.info(f"正在根据最近 {window} 个周期的 {metric} 指标筛选最佳模型...")
        # TODO: 计算 avg(metric)
        best_rid = "abcde12345"
        logger.success(f"推荐最佳模型 ID: <green>{best_rid}</green>")

    def prune(self, keep=50):
        """清理过期的旧模型文件"""
        logger.warning(f"正在清理旧模型，仅保留最近 {keep} 个...")

    def ls(self):
        logger.info("Listing all model in the uri_folder:")
        exps = R.list_experiments()

        for a, b in exps.items():
            if a == 'Default':
                continue
            exp = R.get_exp(experiment_name=a)
            print(f"Experiment: {a} ")
            for rid in exp.list_recorders():
                rec = exp.get_recorder(recorder_id=rid)
                if not rec.list_artifacts():
                    continue
                task = rec.load_object("task")
                print("\t", rid, task["model"]['class'], task['dataset']['kwargs']['handler']['class'])