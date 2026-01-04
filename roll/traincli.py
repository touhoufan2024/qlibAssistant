
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
from myconfig import get_my_config
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
        **kwargs
    ):
        uri_folder = kwargs["uri_folder"]
        self.exp_name = exp_name
        self.step = step
        self.kwargs = kwargs
        exp_manager = C["exp_manager"]
        exp_manager["kwargs"]["uri"] = "file:" + str(Path(uri_folder).expanduser())
        logger.info(f"Experiment uri: {exp_manager['kwargs']['uri']}")
        qlib.init(provider_uri=provider_uri, region=region, exp_manager=exp_manager)
        model_name = kwargs["model_name"]
        dataset_name = kwargs["dataset_name"]
        stock_pool = kwargs["stock_pool"]
        self.task_config = get_my_config(model_name, dataset_name, stock_pool)
        rolling_type = kwargs["rolling_type"]
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

        pfx_name = self.kwargs['pfx_name']
        sfx_name = self.kwargs['sfx_name']
        stock_pool =  task["dataset"]['kwargs']['handler']['kwargs']['instruments']
        step = self.step
        rolling_type = self.kwargs["rolling_type"]

        # exp_name = pfx_name + "_" + model_class + "_" + data_set + "_" + stock_pool + "_" + sfx_name + "_" + time_str
        exp_name = f"{pfx_name}_{model_class}_{data_set}_{stock_pool}_{rolling_type}_step{step}_{sfx_name}_{time_str}"
        print(f"Experiment name: {exp_name}")
        # self.trainer = TrainerR(experiment_name=exp_name)
        # self.trainer.train(tasks)

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

    def test(self):
        base_task = {
            "model": {
                "class": "LGBModel",
                "module_path": "qlib.contrib.model.gbdt",
                "kwargs": {
                    "learning_rate": 0.01,  # 默认值，会被覆盖
                    "num_threads": 20
                }
            },
            "dataset": {
                "class": "DatasetH",
                "kwargs": {
                    "handler": {
                        "class": "Alpha158",
                        "kwargs": {
                            "start_time": "2020-01-01",
                            "end_time": "2026-08-01", 
                            "instruments": "csi300"
                        }
                    },
                    "segments": {
                        "train": ("2015-01-01", "2016-12-31"), 
                        "valid": ("2017-01-01", "2017-02-28"),
                        "test":  ("2017-03-01", "2025-12-31") 
                    }
                }
            }
        }
        gen_rolling = RollingGen(
            step=50, 
            rtype=RollingGen.ROLL_EX
        )
        
        final_tasks = task_generator(
            tasks=base_task,
            generators=gen_rolling  # 注意顺序，先切时间，再改参数
        )

        # ==========================================
        # 5. 验证结果
        # ==========================================
        print(f"最终生成的任务数量: {len(final_tasks)}") 
        # 预期: 2个时间段 * 2个参数 = 4 个任务

        print("\n--- 任务详情 ---")
        for i, task in enumerate(final_tasks):
            lr = task['model']['kwargs']['learning_rate']
            test_seg = task['dataset']['kwargs']['segments']  # ['test']
            print(f"Test Segment={test_seg}")