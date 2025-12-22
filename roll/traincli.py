
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
        exp_manager["kwargs"]["uri"] = "file:" + str(Path(os.getcwd()).resolve() / uri_folder)
        logger.info(f"Experiment uri: {exp_manager['kwargs']['uri']}")
        qlib.init(provider_uri=provider_uri, region=region, exp_manager=exp_manager)
        self.task_config = [CSI300_RECORD_LGB_TASK_CONFIG]
        rolling_type=RollingGen.ROLL_EX,
        self.rolling_gen = RollingGen(step=step, rtype=rolling_type)
        self.trainer = TrainerR(experiment_name=self.exp_name)

    def init(self, model="LGB", step=20):
        """
        [警告] 初始化并全量重新训练
        :param model: 模型配置文件名 (如 LGB, XGB)
        :param step: 滚动步长
        """
        logger.warning(f"!!! 准备重置实验 [{self.exp_name}] 并全量训练 !!!")
        logger.info(f"模型配置: {model} | 滚动步长: {step}")
        # TODO: inst = RollingTaskExample(experiment_name=self.exp_name, ...)
        # TODO: inst.reset()
        # TODO: inst.run()

    def update(self, step=20):
        """
        [核心] 增量滚动训练: 仅训练新产生的时间段
        """
        logger.info(f"检查实验 [{self.exp_name}] 是否需要增量训练...")
        # TODO: 比较 R.list_recorders 的 max(test_end_date) 与 数据最新日期
        need_train = True # 模拟判断
        if need_train:
            logger.info("发现新数据，开始训练新的滚动子模型...")
            # TODO: inst = RollingTaskExample(...)
            # TODO: inst.task_training(...)
            logger.success("增量训练完成")
        else:
            logger.info("当前模型已是最新的，无需训练。")

    def repair(self, rid):
        """修复特定 Recorder ID 的训练"""
        logger.info(f"正在修复/重跑 Recorder ID: [{rid}]...")

    def start(self):
        """开始自动滚动训练"""
        logger.info(f"启动滚动训练... step={self.step}")
        tasks = self.task_generating()
        self.task_training(tasks)
        self.task_collecting()

    def task_generating(self):
        print("========== task_generating ==========")
        tasks = task_generator(
            tasks=self.task_config,
            generators=self.rolling_gen,  # generate different date segments
        )
        pprint(tasks)
        return tasks

    def task_training(self, tasks):
        print("========== task_training ==========")
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