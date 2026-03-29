from typing import Dict, Any, List
import copy

# --- 借用并整合自 myconfig.py 的模型定义 ---

MODEL_CONFIGS = {
    "XGBoost": {
        "class": "XGBModel",
        "module_path": "qlib.contrib.model.xgboost",
        "kwargs": {
            "eval_metric": "rmse",
            "colsample_bytree": 0.8879,
            "eta": 0.0421,
            "max_depth": 8,
            "n_estimators": 647,
            "subsample": 0.8789,
            "nthread": 16
        }
    },
    "LightGBM": {
        "class": "LGBModel",
        "module_path": "qlib.contrib.model.gbdt",
        "kwargs": {
            "loss": "mse",
            "colsample_bytree": 0.8879,
            "learning_rate": 0.0421,
            "subsample": 0.8789,
            "lambda_l1": 205.6999,
            "lambda_l2": 580.9768,
            "max_depth": 8,
            "num_leaves": 210,
            "num_threads": 16,
        }
    },
    "Linear": {
        "class": "LinearModel",
        "module_path": "qlib.contrib.model.linear",
        "kwargs": {
            "estimator": "ridge",
            "alpha": 0.05
        }
    }
}

RECORD_CONFIG = [
    {
        "class": "SignalRecord",
        "module_path": "qlib.workflow.record_temp",
        "kwargs": {
            "dataset": "<DATASET>",
            "model": "<MODEL>",
        },
    },
    {
        "class": "SigAnaRecord",
        "module_path": "qlib.workflow.record_temp",
    }
]

class WFTaskBuilder:
    """负责组装 Qlib 任务字典"""
    
    @staticmethod
    def build_task(model_name: str, dataset_name: str, stock_pool: str, segments: Dict[str, Any], end_time: str = None) -> Dict[str, Any]:
        model_config = copy.deepcopy(MODEL_CONFIGS.get(model_name))
        if not model_config:
            raise ValueError(f"暂不支持模型: {model_name}")

        train_seg = segments["train"]
        # 如果未指定 end_time，则默认使用训练集的结束时间
        actual_end_time = end_time if end_time else train_seg[1]
        
        # 组装 Dataset 配置
        dataset_config = {
            "class": "DatasetH",
            "module_path": "qlib.data.dataset",
            "kwargs": {
                "handler": {
                    "class": dataset_name,
                    "module_path": "qlib.contrib.data.handler",
                    "kwargs": {
                        # 【关键修复】使用与 roll 模块一致的全局起止时间，确保复用 Qlib 硬盘缓存！
                        # 否则 Qlib 检测到时间不一致会启动多进程从头重算 Alpha158，瞬间撑爆内存导致死机。
                        "start_time": "2018-01-01",
                        "end_time": "2066-08-01", 
                        "fit_start_time": train_seg[0],
                        "fit_end_time": train_seg[1],
                        "instruments": stock_pool,
                    },
                },
                "segments": segments,
            },
        }

        return {
            "model": model_config,
            "dataset": dataset_config,
            "record": RECORD_CONFIG,
        }
