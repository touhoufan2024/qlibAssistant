a = {
    "dataset": {
        "class": "DatasetH",
        "kwargs": {
            "handler": {
                "class": "Alpha158",
                "kwargs": {
                    "end_time": "2066-08-01",
                    "fit_end_time": "2016-12-31",
                    "fit_start_time": "2015-01-01",
                    "instruments": "csi300",
                    "start_time": "2018-01-01",
                },
                "module_path": "qlib.contrib.data.handler",
            },
            "segments": {
                "test": ("2026-02-28", "2026-03-29"),
                "train": ("2025-03-28", "2025-12-27"),
                "valid": ("2025-12-28", "2026-02-27"),
            },
        },
        "module_path": "qlib.data.dataset",
    },
    "model": {
        "class": "LGBModel",
        "kwargs": {
            "colsample_bytree": 0.8879,
            "lambda_l1": 205.6999,
            "lambda_l2": 580.9768,
            "learning_rate": 0.0421,
            "loss": "mse",
            "max_depth": 8,
            "num_leaves": 210,
            "num_threads": 20,
            "subsample": 0.8789,
        },
        "module_path": "qlib.contrib.model.gbdt",
    },
    "record": [
        {
            "class": "SignalRecord",
            "kwargs": {"dataset": "<DATASET>", "model": "<MODEL>"},
            "module_path": "qlib.workflow.record_temp",
        },
        {"class": "SigAnaRecord", "module_path": "qlib.workflow.record_temp"},
    ],
}

b = {
    "dataset": {
        "class": "DatasetH",
        "kwargs": {
            "handler": {
                "class": "Alpha158",
                "kwargs": {
                    "end_time": "2025-10-22",
                    "fit_end_time": "2025-10-22",
                    "fit_start_time": "2025-01-03",
                    "instruments": "csi300",
                    "start_time": "2025-01-03",
                },
                "module_path": "qlib.contrib.data.handler",
            },
            "segments": {
                "test": ("2026-01-05", "2026-01-05"),
                "train": ("2025-01-03", "2025-10-22"),
                "valid": ("2025-10-23", "2025-12-29"),
            },
        },
        "module_path": "qlib.data.dataset",
    },
    "model": {
        "class": "LinearModel",
        "kwargs": {"alpha": 0.05, "estimator": "ridge"},
        "module_path": "qlib.contrib.model.linear",
    },
    "record": [
        {
            "class": "SignalRecord",
            "kwargs": {"dataset": "<DATASET>", "model": "<MODEL>"},
            "module_path": "qlib.workflow.record_temp",
        },
        {"class": "SigAnaRecord", "module_path": "qlib.workflow.record_temp"},
    ],
}
