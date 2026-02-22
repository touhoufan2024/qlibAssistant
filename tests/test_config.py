import pytest
from pathlib import Path
import os
import sys
import qlib

# 1. 路径修复
root_dir = Path(__file__).resolve().parent.parent
roll_dir = os.path.join(root_dir, "roll")
if roll_dir not in sys.path:
    sys.path.insert(0, roll_dir)
from pathlib import Path
import os
import sys
import qlib

# 1. 路径修复
root_dir = Path(__file__).resolve().parent.parent
roll_dir = os.path.join(root_dir, "roll")
if roll_dir not in sys.path:
    sys.path.insert(0, roll_dir)
from myconfig import (
    get_model_config,
    get_dataset_config,
    get_my_config,
    CSI300_MARKET,
    XGBOOST_MODEL
)

# 1. 验证模型配置获取逻辑
def test_get_model_config():
    # 验证已知模型
    lgb_config = get_model_config("LightGBM")
    assert lgb_config["class"] == "LGBModel"

    xgb_config = get_model_config("XGBoost")
    assert xgb_config == XGBOOST_MODEL

    # 验证不支持的模型抛出异常
    with pytest.raises(ValueError, match="is not supported"):
        get_model_config("UnknownModel")

# 2. 验证数据集配置生成逻辑
def test_get_dataset_config():
    custom_train = ("2020-01-01", "2020-12-31")
    config = get_dataset_config(train=custom_train)

    # 验证时间段是否正确注入
    assert config["kwargs"]["segments"]["train"] == custom_train

    # 验证关键的 fit_start_time 自动填充逻辑 (解决占位符问题)
    handler_kwargs = config["kwargs"]["handler"]["kwargs"]
    assert handler_kwargs["fit_start_time"] == "2020-01-01"
    assert handler_kwargs["fit_end_time"] == "2020-12-31"

# 3. 验证综合配置生成 (get_my_config)
def test_get_my_config_structure():
    model_name = "Linear"
    dataset_name = "Alpha158"
    stock_pool = "csi100"

    cfg = get_my_config(model_name, dataset_name, stock_pool)

    # 验证顶层结构
    assert "model" in cfg
    assert "dataset" in cfg
    assert "record" in cfg

    # 验证股票池是否正确渗透到 handler
    handler_cfg = cfg["dataset"]["kwargs"]["handler"]["kwargs"]
    assert handler_cfg["instruments"] == "csi100"

# 4. 验证模型参数的数值正确性
def test_model_params_consistency():
    # 针对你硬件优化的参数校验
    de_config = get_model_config("DoubleEnsemble")
    # 验证 sample_ratios 和 sub_weights 的数量匹配逻辑
    assert len(de_config["kwargs"]["sample_ratios"]) == 5
    assert len(de_config["kwargs"]["sub_weights"]) == 6
