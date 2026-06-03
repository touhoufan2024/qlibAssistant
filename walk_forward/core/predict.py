import pandas as pd
import os
import multiprocessing
from loguru import logger
from typing import Dict, Any, Optional
import copy
import pickle
from pathlib import Path

def _predict_worker(task: Dict[str, Any], exp_name: str, rid: str, 
                    test_start: str, test_end: str, qlib_config: Dict[str, Any], 
                    output_path: str):
    """
    推理子进程：加载模型，执行预测，将结果保存到临时文件后退出。
    """
    try:
        import qlib
        from qlib.workflow import R
        from qlib.utils import init_instance_by_config
        
        qlib.init(**qlib_config)
        
        # 获取实验和记录
        exp = R.get_exp(experiment_name=exp_name)
        recorder = exp.get_recorder(recorder_id=rid)
        
        # 加载模型
        model = recorder.load_object("params.pkl")
        
        # 修改任务字典中的测试区间
        test_task = copy.deepcopy(task)
        test_task["dataset"]["kwargs"]["segments"]["test"] = (test_start, test_end)
        
        # 初始化数据集
        dataset = init_instance_by_config(test_task["dataset"])
        
        # 执行预测
        pred_score = model.predict(dataset, segment="test")
        
        # 保存结果到临时文件
        with open(output_path, 'wb') as f:
            pickle.dump(pred_score, f)
            
        logger.info(f"🟢 [推理进程 PID: {os.getpid()}] 完成区间 {test_start} ~ {test_end}，结果已暂存。")
        os._exit(0)
    except Exception as e:
        logger.error(f"🔴 [推理进程 PID: {os.getpid()}] 出错: {e}")
        import traceback
        logger.debug(traceback.format_exc())
        os._exit(1)

def run_predict_process(task: Dict[str, Any], exp_name: str, rid: str, 
                        test_start: str, test_end: str, qlib_config: Dict[str, Any]) -> pd.Series:
    """
    主进程调用的包装函数：启动子进程执行推理，并读取结果。
    """
    import tempfile
    # 创建临时文件
    fd, temp_path = tempfile.mkstemp(suffix=".pkl")
    os.close(fd)
    
    try:
        p = multiprocessing.Process(
            target=_predict_worker, 
            args=(task, exp_name, rid, test_start, test_end, qlib_config, temp_path)
        )
        p.start()
        p.join()
        
        if p.exitcode == 0 and os.path.exists(temp_path):
            with open(temp_path, 'rb') as f:
                result = pickle.load(f)
            return result
        else:
            logger.warning(f"⚠️ 推理子进程失败，退出码: {p.exitcode}")
            return pd.Series()
    finally:
        # 清理临时文件
        if os.path.exists(temp_path):
            os.remove(temp_path)

class WFPredictor:
    """保持接口兼容的包装类"""
    def __init__(self, qlib_config: Dict[str, Any]):
        self.qlib_config = qlib_config

    def predict_segment(self, task: Dict[str, Any], exp_name: str, rid: str, test_start: str, test_end: str) -> pd.Series:
        return run_predict_process(task, exp_name, rid, test_start, test_end, self.qlib_config)
