import multiprocessing
import os
from loguru import logger
from typing import Dict, Any, Optional

def _train_worker(task: Dict[str, Any], exp_name: str, qlib_config: Dict[str, Any], result_queue: multiprocessing.Queue):
    """
    这是子进程执行的训练函数。
    """
    try:
        # 保持延迟导入，确保子进程环境纯净
        import qlib
        from qlib.model.trainer import TrainerR
        
        qlib.init(**qlib_config)
        
        logger.info(f"🔵 [子进程 PID: {os.getpid()}] 开始训练模型...")
        
        trainer = TrainerR(experiment_name=exp_name)
        recorders = trainer.train(task)
        
        if isinstance(recorders, list):
            recorder = recorders[0]
        else:
            recorder = recorders
            
        # 将 rid 放入队列
        result_queue.put(recorder.id)
        
        logger.info(f"🟢 [子进程 PID: {os.getpid()}] 训练完成，Recorder ID: {recorder.id}")
        
        # 强制退出
        os._exit(0)  
    except Exception as e:
        logger.error(f"🔴 [子进程 PID: {os.getpid()}] 训练出错: {e}")
        os._exit(1)

def run_train_process(task: Dict[str, Any], exp_name: str, qlib_config: Dict[str, Any]) -> Optional[str]:
    """
    [回退测试版本] 使用 Queue 传递 RID。
    """
    result_queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=_train_worker, args=(task, exp_name, qlib_config, result_queue))
    p.start()
    p.join()
    
    if p.exitcode == 0:
        if not result_queue.empty():
            return result_queue.get()
    else:
        logger.warning(f"⚠️ 训练子进程失败，退出代码: {p.exitcode}")
        return None
