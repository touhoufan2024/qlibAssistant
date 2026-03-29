import pandas as pd
import qlib
from qlib.workflow import R
from qlib.utils import init_instance_by_config
from loguru import logger
from typing import Dict, Any, List, Tuple
import copy

class WFPredictor:
    """负责加载模型并在指定区间执行推理"""
    
    def __init__(self, qlib_config: Dict[str, Any]):
        self.qlib_config = qlib_config
        # 直接初始化，qlib.init 具有幂等性
        qlib.init(**self.qlib_config)

    def predict_segment(self, task: Dict[str, Any], exp_name: str, rid: str, test_start: str, test_end: str) -> pd.Series:
        """
        在特定的测试区间执行推理
        """
        try:
            # 使用 R.get_exp 获取指定实验，不依赖全局 set_exp
            exp = R.get_exp(experiment_name=exp_name)
            recorder = exp.get_recorder(recorder_id=rid)
            
            # 加载模型
            model = recorder.load_object("params.pkl")
            
            # 修改任务字典中的测试区间
            test_task = copy.deepcopy(task)
            test_task["dataset"]["kwargs"]["segments"]["test"] = (test_start, test_end)
            
            # 初始化数据集 (Dataset)
            dataset = init_instance_by_config(test_task["dataset"])
            
            # 执行预测
            pred_score = model.predict(dataset, segment="test")
            return pred_score
            
        except Exception as e:
            logger.error(f"推理失败 (Exp: {exp_name}, RID: {rid}, 区间: {test_start} ~ {test_end}): {e}")
            import traceback
            logger.debug(traceback.format_exc())
            return pd.Series()
