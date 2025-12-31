
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
from pprint import pprint
import datetime
logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>"
)

class TrainCLI:
    """
    [子模块] 训练引擎: 负责滚动训练 (Rolling)
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
        self.task_config = [CSI300_RECORD_LGB_TASK_CONFIG]
        rolling_type=RollingGen.ROLL_EX,
        self.rolling_gen = RollingGen(step=step, rtype=rolling_type)

    def start(self):
        """开始自动滚动训练"""
        logger.info(f"启动滚动训练... step={self.step}")
        tasks = self.gen()
        self.task_training(tasks)

    def gen(self):
        print("========== task_generating ==========")
        tasks = task_generator(
            tasks=self.task_config,
            generators=self.rolling_gen,  # generate different date segments
        )
        pprint(tasks)
        return tasks

    def task_training(self, tasks):
        print("========== task_training ==========")
        task = tasks[0]
        model_class = task["model"]["class"]
        data_set = task["dataset"]["kwargs"]["handler"]["class"]

        now = datetime.datetime.now()
        time_str = now.strftime("%Y%m%d_%H")

        exp_name = model_class + "_" + data_set + "_" + time_str
        print(f"Experiment name: {exp_name}")
        self.trainer = TrainerR(experiment_name=exp_name)
        self.trainer.train(tasks)

    def task_collecting(self):
        print("========== task_collecting ==========")

        def rec_key(recorder):
            task_config = recorder.load_object("task")
            model_key = task_config["model"]["class"]
            rolling_key = task_config["dataset"]["kwargs"]["segments"]["test"]
            return model_key, rolling_key

        def my_filter(recorder):
            # only choose the results of "LGBModel"
            model_key, rolling_key = rec_key(recorder)
            if model_key == "LGBModel":
                return True
            return False

        collector = RecorderCollector(
            experiment=self.exp_name,
            process_list=RollingGroup(),
            rec_key_func=rec_key,
            rec_filter_func=my_filter,
        )
        print(collector())