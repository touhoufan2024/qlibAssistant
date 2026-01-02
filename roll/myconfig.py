#  Copyright (c) Microsoft Corporation.
#  Licensed under the MIT License.

CSI300_MARKET = "csi300"
CSI100_MARKET = "csi100"

CSI300_BENCH = "SH000300"

DATASET_ALPHA158_CLASS = "Alpha158"
DATASET_ALPHA360_CLASS = "Alpha360"

###################################
# config
###################################

# Supported Models:
model_list = ["CatBoost", "KRNN","Sandwich","Linear","XGBoost","TFT","DoubleEnsemble","LightGBM"]


CATBOOST_MODEL = {
    "class": "CatBoostModel",
    "module_path": "qlib.contrib.model.catboost_model",
    "kwargs": {
        "loss": "RMSE",
        "learning_rate": 0.0421,
        "subsample": 0.8789,
        "max_depth": 6,
        "num_leaves": 100,
        "thread_count": 20, 
        "grow_policy": "Lossguide",
        "bootstrap_type": "Poisson"
    }
}

KRNN_MODEL = {
   "class": "KRNN",
    "module_path": "qlib.contrib.model.pytorch_krnn",
    "kwargs": {
        "fea_dim": 6,
        "cnn_dim": 8,
        "cnn_kernel_size": 3,
        "rnn_dim": 8,
        "rnn_dups": 2,
        "rnn_layers": 2,
        "n_epochs": 200,
        "lr": 0.001,
        "early_stop": 20,
        "batch_size": 2000,
        "metric": "loss",
        "GPU": 0
    }
}

SANDWICH_MODEL = {
  "class": "Sandwich",
    "module_path": "qlib.contrib.model.pytorch_sandwich",
    "kwargs": {
        "fea_dim": 6,          # ⚠️ 注意：需修改为实际因子数量 (如 Alpha158 为 158)
        "cnn_dim_1": 16,
        "cnn_dim_2": 16,
        "cnn_kernel_size": 3,
        "rnn_dim_1": 8,
        "rnn_dim_2": 8,
        "rnn_dups": 2,
        "rnn_layers": 2,
        "n_epochs": 200,
        "lr": 0.001,
        "early_stop": 20,
        "batch_size": 2000,
        "metric": "loss",
        "GPU": 0               # GPU 索引，无显卡改为 -1
    }
}

LINEAR_MODEL = {
  "class": "LinearModel",
    "module_path": "qlib.contrib.model.linear",
    "kwargs": {
        "estimator": "ols"  # 也可以改为 'ridge' (岭回归)
    }
}

XGBOOST_MODEL = {
 "class": "XGBModel",
    "module_path": "qlib.contrib.model.xgboost",
    "kwargs": {
        "eval_metric": "rmse",
        "colsample_bytree": 0.8879,
        "eta": 0.0421,
        "max_depth": 8,
        "n_estimators": 647,
        "subsample": 0.8789,
        "nthread": 20  # 建议根据你的 16 核硬件改为 16
    }
}

# TFT_MODEL = {
# }

DOUBLE_ENSEMBLE_MODEL = {
 "class": "DEnsembleModel",
    "module_path": "qlib.contrib.model.double_ensemble",
    "kwargs": {
        # --- DoubleEnsemble 自身参数 ---
        "base_model": "gbm",      # 内部使用的基础模型类型
        "loss": "mse",            # 损失函数
        "num_models": 6,          # 集成中包含 6 个子模型
        "enable_sr": True,        # 启用子采样 (Sample Reuse)
        "enable_fs": True,        # 启用特征选择 (Feature Selection)
        "alpha1": 1,
        "alpha2": 1,
        "bins_sr": 10,
        "bins_fs": 5,
        "decay": 0.5,
        
        # ⚠️ 注意: sample_ratios 有5个, sub_weights 有6个
        "sample_ratios": [
            0.8,
            0.7,
            0.6,
            0.5,
            0.4
        ],
        "sub_weights": [
            1,
            0.2,
            0.2,
            0.2,
            0.2,
            0.2
        ],
        
        # --- 传递给内部 base_model (gbm) 的参数 ---
        "epochs": 136,
        "colsample_bytree": 0.8879,
        "learning_rate": 0.0421,
        "subsample": 0.8789,
        "lambda_l1": 205.6999,
        "lambda_l2": 580.9768,
        "max_depth": 8,
        "num_leaves": 210,
        "num_threads": 20, # 建议改为 16，匹配你的硬件
        "verbosity": -1
    }
}

GBDT_MODEL = {
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
        "num_threads": 20,
    },
}


SA_RC = {
    "class": "SigAnaRecord",
    "module_path": "qlib.workflow.record_temp",
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
    SA_RC,
]


def get_data_handler_config(
    start_time="2008-01-01",
    end_time="2026-08-01",
    fit_start_time="<dataset.kwargs.segments.train.0>",
    fit_end_time="<dataset.kwargs.segments.train.1>",
    instruments=CSI300_MARKET,
):
    return {
        "start_time": start_time,
        "end_time": end_time,
        "fit_start_time": fit_start_time,
        "fit_end_time": fit_end_time,
        "instruments": instruments,
    }


def get_dataset_config(
    dataset_class=DATASET_ALPHA158_CLASS,
    train=("2010-01-01", "2019-12-31"),
    valid=("2020-01-01", "2021-12-31"),
    test=("2022-01-01", "2025-12-10"),
    handler_kwargs={"instruments": CSI300_MARKET},
):
    return {
        "class": "DatasetH",
        "module_path": "qlib.data.dataset",
        "kwargs": {
            "handler": {
                "class": dataset_class,
                "module_path": "qlib.contrib.data.handler",
                "kwargs": get_data_handler_config(**handler_kwargs),
            },
            "segments": {
                "train": train,
                "valid": valid,
                "test": test,
            },
        },
    }


def get_gbdt_task(dataset_kwargs={}, handler_kwargs={"instruments": CSI300_MARKET}):
    return {
        "model": GBDT_MODEL,
        "dataset": get_dataset_config(**dataset_kwargs, handler_kwargs=handler_kwargs),
        "record": RECORD_CONFIG,
    }


def get_record_lgb_config(dataset_kwargs={}, handler_kwargs={"instruments": CSI300_MARKET}):
    return {
        "model": {
            "class": "LGBModel",
            "module_path": "qlib.contrib.model.gbdt",
        },
        "dataset": get_dataset_config(**dataset_kwargs, handler_kwargs=handler_kwargs),
        "record": RECORD_CONFIG,
    }


def get_record_xgboost_config(dataset_kwargs={}, handler_kwargs={"instruments": CSI300_MARKET}):
    return {
        "model": {
            "class": "XGBModel",
            "module_path": "qlib.contrib.model.xgboost",
        },
        "dataset": get_dataset_config(**dataset_kwargs, handler_kwargs=handler_kwargs),
        "record": RECORD_CONFIG,
    }


CSI300_DATASET_CONFIG = get_dataset_config(handler_kwargs={"instruments": CSI300_MARKET})
CSI300_GBDT_TASK = get_gbdt_task(handler_kwargs={"instruments": CSI300_MARKET})

CSI100_RECORD_XGBOOST_TASK_CONFIG = get_record_xgboost_config(handler_kwargs={"instruments": CSI100_MARKET})
CSI100_RECORD_LGB_TASK_CONFIG = get_record_lgb_config(handler_kwargs={"instruments": CSI100_MARKET})
CSI300_RECORD_LGB_TASK_CONFIG = get_record_lgb_config(handler_kwargs={"instruments": CSI300_MARKET})


def get_model_config(model_name: str):
    match model_name:
        case "LightGBM":
            return GBDT_MODEL
        case _:
            raise ValueError(f"Model {model_name} is not supported.")

def get_my_config(model_name: str, dataset_name: str, stock_pool: str):
    handler_kwargs = {"instruments": stock_pool}
    return {
        "model": get_model_config(model_name),
        "dataset": get_dataset_config(dataset_class=dataset_name, handler_kwargs=handler_kwargs),
        "record": RECORD_CONFIG,
    }