import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from pathlib import Path
import os
import sys
import qlib

# 1. 路径修复
root_dir = Path(__file__).resolve().parent.parent
roll_dir = os.path.join(root_dir, "roll")
if roll_dir not in sys.path:
    sys.path.insert(0, roll_dir)

# 2. 【关键】在测试开始前强制初始化 Qlib，防止物理路径检查
@pytest.fixture(scope="session", autouse=True)
def init_qlib_env():
    qlib.init(provider_uri="~/fake_data", region="cn")

from modelcli import ModelCLI, ModelContext

@pytest.fixture
def mock_cli_params():
    return {
        "uri_folder": "~/mlruns",
        "provider_uri": "~/fake_data", # 补全此项防止 Qlib 报错
        "analysis_folder": "~/analysis",
        "model_filter": ["LGBM"],
        "rec_filter": [{"IC": 0.02}],
        "predict_dates": [{"start": "2023-01-01", "end": "2023-01-05"}],
        "model_name": None # 显式提供，防止 KeyError
    }

# 3. 修复 test_model_cli_init
@patch('modelcli.qlib.init')
def test_model_cli_init(mock_qlib_init, mock_cli_params):
    # 使用 patch.dict 修改全局配置对象 C，而不是直接 patch C
    with patch('modelcli.C', dict(exp_manager={"kwargs": {"uri": ""}})):
        cli = ModelCLI(region="cn", **mock_cli_params)
        assert cli.kwargs["model_name"] is None # 现在不会 KeyError 了

# 4. 修复过滤逻辑测试 (手动提供 provider_uri)
def test_filter_rec_logic(mock_cli_params):
    cli = ModelCLI(**mock_cli_params)
    with patch.object(cli, 'get_ic_info') as mock_ic:
        mock_ic.return_value = ({}, [0.05, 0.1])
        assert cli.filter_rec(MagicMock()) is True

# 5. 【重要修复】针对 R.get_exp 的 AttributeError
# 建议 patch 'qlib.workflow.R' 这种完整路径
@patch('qlib.workflow.R.list_experiments')
@patch('qlib.workflow.R.get_exp')
def test_get_model_list(mock_get_exp, mock_list_exps, mock_cli_params):
    cli = ModelCLI(**mock_cli_params)
    mock_list_exps.return_value = ["Default", "LGBM_Task"]

    mock_exp = MagicMock()
    mock_exp.list_recorders.return_value = ["rid_1"]
    mock_get_exp.return_value = mock_exp

    with patch.object(cli, '_is_valid_recorder', return_value=True):
        model_list = cli.get_model_list()
        assert len(model_list) == 1
        assert model_list[0].exp_name == "LGBM_Task"

def test_filter_ret_df_logic(mock_cli_params):
    cli = ModelCLI(**mock_cli_params)
    df = pd.DataFrame({
        'STD5': [0.02, 0.5], 'STD20': [0.02, 0.02], 'STD60': [0.02, 0.02],
        'ROC10': [1.0, 1.0], 'ROC20': [1.0, 1.0], 'ROC60': [1.0, 1.0]
    })
    filtered = cli.filter_ret_df(df)
    assert len(filtered) == 1
