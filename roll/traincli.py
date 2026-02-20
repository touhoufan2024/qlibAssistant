
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
import gc
import multiprocessing
from tqdm import tqdm
from functools import partialmethod
tqdm.__init__ = partialmethod(tqdm.__init__, disable=True)

from qlib.workflow.task.gen import handler_mod as default_handler_mod


def _train_worker(task, exp_name):
    """
    这是子进程实际执行的函数。
    """
    try:
        # 打印 PID 方便观察
        logger.info(f"🔵 [子进程 PID: {os.getpid()}] 开始训练...", flush=True)

        # 实例化 Trainer 并开始训练
        trainer = TrainerR(experiment_name=exp_name)
        trainer.train(task)

        logger.info(f"🟢 [子进程 PID: {os.getpid()}] 训练完成，准备释放内存。", flush=True)
        os._exit(0)  # 确保子进程正常退出，exitcode 0
    except Exception as e:
        # 捕获异常打印出来，并再次抛出以确保 exitcode 非 0
        logger.info(f"🔴 [子进程 PID: {os.getpid()}] 训练出错: {e}", flush=True)
        raise e

def run_train_blocking(task, exp_name):
    """
    主进程调用的函数。
    功能：启动子进程 -> 阻塞等待 -> 返回结果
    """
    # 1. 创建子进程，目标是上面的 _train_worker 函数
    p = multiprocessing.Process(target=_train_worker, args=(task, exp_name))

    # 2. 启动子进程
    p.start()

    # 3. 【关键】阻塞主进程，直到子进程结束
    # 此时主进程什么都不干，内存也不会增加，静静等待子进程销毁
    p.join()

    logger.info(f"子进程 PID: {p.pid} 已结束，退出代码: {p.exitcode}")
    # 4. 判断子进程是正常结束还是报错挂了
    if p.exitcode == 0:
        return True  # 成功
    else:
        logger.info(f"⚠️ 任务失败，子进程退出代码: {p.exitcode}")
        return False # 失败


def my_enhanced_handler_mod(task, rg):
    # 1. 先调用官方自带的逻辑，帮你处理 end_time 不够长的问题
    default_handler_mod(task, rg)

    # 2. 再加上你自己的逻辑，修复 fit_start_time 的占位符问题
    # 获取当前滚动后的 train 时间段
    train_start, train_end = task["dataset"]["kwargs"]["segments"]["train"]

    # 获取 handler 配置
    h_kwargs = task["dataset"]["kwargs"]["handler"]["kwargs"]

    # 强制覆盖为真实日期
    h_kwargs["fit_start_time"] = train_start
    h_kwargs["fit_end_time"] = train_end

class TrainCLI:
    """
    [子模块] 训练引擎: 负责滚动训练 (Rolling)
    """
    def __init__(
        self,
        exp_name,
        step = 40,
        region=REG_CN,
        experiment_name="rolling_exp",
        **kwargs
    ):
        uri_folder = kwargs["uri_folder"]
        provider_uri = kwargs["provider_uri"]
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
        self.rolling_gen = RollingGen(step=step, rtype=rolling_type, ds_extra_mod_func=my_enhanced_handler_mod)

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

        exp_name = f"{pfx_name}_{model_class}_{data_set}_{stock_pool}_{rolling_type}_step{step}_{sfx_name}_{time_str}"
        print(f"Experiment name: {exp_name}")


        ## 断点续训功能
        exps = R.list_experiments()
        for name in exps:
            if name.rsplit('_', 2)[0] == exp_name.rsplit('_', 2)[0]:
                exp_name = name

        logger.info(f"Using experiment name: {exp_name}")
        self.trainer = TrainerR(experiment_name=exp_name)

        exp = R.get_exp(experiment_name=exp_name)
        exp_train_time_segs_list = []
        for rid in exp.list_recorders():
            rec = exp.get_recorder(recorder_id=rid)
            if not rec.list_artifacts():
                continue
            lista = rec.list_artifacts()
            if "params.pkl" not in lista or "sig_analysis" not in lista:
                continue

            task = rec.load_object("task")
            train_time_seg = task["dataset"]["kwargs"]["segments"]["train"]
            exp_train_time_segs_list.append(train_time_seg)

        print(f"Already trained time segments in experiment: {len(exp_train_time_segs_list)}")

        for idx, task in enumerate(tasks):
            logger.info(f"----- Training task {idx + 1}/{len(tasks)} -----")
            train_time_seg = task["dataset"]["kwargs"]["segments"]["train"]
            print(f"Train time segment: {train_time_seg}")

            if train_time_seg in exp_train_time_segs_list:
                logger.info(f"Skipping training for segment {train_time_seg} as it already exists in the experiment.")
                continue

            run_train_blocking(task, exp_name)
            gc.collect()

    def task_collecting(self):
        print("========== task_collecting ==========")

        def rec_key(recorder):
            task_config = recorder.load_object("task")
            model_key = task_config["model"]["class"]
            rolling_key = task_config["dataset"]["kwargs"]["segments"]["test"]
            return model_key, rolling_key

        def my_filter(recorder):
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
