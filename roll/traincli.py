import copy
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
from datetime import datetime
import gc
import multiprocessing
from tqdm import tqdm
from functools import partialmethod
from utils import generate_qlib_segments, get_mlruns_dates, get_local_data_date

tqdm.__init__ = partialmethod(tqdm.__init__, disable=True)

from qlib.workflow.task.gen import handler_mod as default_handler_mod


def _train_worker(task, exp_name, qlib_config=None):
    """
    这是子进程实际执行的函数。
    """
    try:
        # 如果你有特殊的配置，建议通过 qlib_config 传进来
        # 如果只是默认配置，可以直接 qlib.init()
        if qlib_config:
            qlib.init(**qlib_config)
        else:
            qlib.init()
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

def run_train_blocking(task, exp_name, qlib_config=None):
    """
    主进程调用的函数。
    功能：启动子进程 -> 阻塞等待 -> 返回结果
    """
    # 1. 创建子进程，目标是上面的 _train_worker 函数
    p = multiprocessing.Process(target=_train_worker, args=(task, exp_name, qlib_config))

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
        step = 40,
        region=REG_CN,
        **kwargs
    ):
        uri_folder = kwargs["uri_folder"]
        provider_uri = kwargs["provider_uri"]
        self.step = step
        self.kwargs = kwargs
        exp_manager = C["exp_manager"]
        exp_manager["kwargs"]["uri"] = "file:" + str(Path(uri_folder).expanduser())
        logger.info(f"Experiment uri: {exp_manager['kwargs']['uri']}")
        self.qlib_config = dict(provider_uri=provider_uri, region=region, exp_manager=exp_manager)
        qlib.init(**self.qlib_config)
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

        now = datetime.now()
        time_str = now.strftime("%Y%m%d_%H")

        pfx_name = self.kwargs['pfx_name']
        sfx_name = self.kwargs['sfx_name']
        stock_pool =  task["dataset"]['kwargs']['handler']['kwargs']['instruments']
        step = self.step
        rolling_type = self.kwargs["rolling_type"]
        if rolling_type == "custom":
            step = "0"

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

            run_train_blocking(task, exp_name, self.qlib_config)
            gc.collect()

    def start_custom(self):
        self.kwargs["rolling_type"] = "custom"
        tasks = []
        for i in range(1, 6):
            segments = generate_qlib_segments(months_total=12 * i)
            _task = copy.deepcopy(self.task_config)
            _task["dataset"]["kwargs"]["segments"] = segments
            tasks.append(_task)
        self.task_training(tasks)
    
    def need_train(self):
        mlruns_dates = get_mlruns_dates()
        print(f"mlruns_dates: {mlruns_dates}")
        local_data_date = get_local_data_date(self.kwargs['provider_uri'])
        print(f"local_data_date: {local_data_date}")
    
        max_mlruns_date = max(mlruns_dates)
        
        return max_mlruns_date < local_data_date


