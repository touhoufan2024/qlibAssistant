import multiprocessing
import os
from loguru import logger
from typing import Dict, Any, Optional

def _train_worker(task: Dict[str, Any], exp_name: str, qlib_config: Dict[str, Any]):
    """
    这是子进程实际执行的训练函数。
    """
    try:
        # 延迟导入：确保子进程独立后才加载 Qlib
        import qlib
        from qlib.model.trainer import TrainerR
        
        qlib.init(**qlib_config)
        
        logger.info(f"🔵 [子进程 PID: {os.getpid()}] 开始训练...", flush=True)

        # 实例化 Trainer 并开始训练
        trainer = TrainerR(experiment_name=exp_name)
        trainer.train(task)

        logger.info(f"🟢 [子进程 PID: {os.getpid()}] 训练完成。", flush=True)
        # 强制自杀，确保不进行任何 Python 层的清理（防止 Windows 上的导入死锁/挂起）
        os._exit(0)  
    except Exception as e:
        logger.error(f"🔴 [子进程 PID: {os.getpid()}] 训练出错: {e}", flush=True)
        os._exit(1)

def run_train_process(task: Dict[str, Any], exp_name: str, qlib_config: Dict[str, Any]) -> bool:
    """
    主进程调用的训练管理函数。
    不使用 Queue，彻底规避 IPC 造成的死锁。
    """
    p = multiprocessing.Process(target=_train_worker, args=(task, exp_name, qlib_config))
    p.start()
    p.join()

    if p.exitcode == 0:
        return True
    else:
        logger.warning(f"⚠️ 任务失败，子进程退出代码: {p.exitcode}")
        return False
