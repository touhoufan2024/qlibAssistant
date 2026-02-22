import pytest
from unittest.mock import patch, MagicMock
from loguru import logger
from pathlib import Path
import os
import sys

# 1. 路径修复
root_dir = Path(__file__).resolve().parent.parent
roll_dir = os.path.join(root_dir, "roll")
if roll_dir not in sys.path:
    sys.path.insert(0, roll_dir)
from datacli import DataCLI

# --- 1. 核心固件：桥接 Loguru 与 Pytest ---
@pytest.fixture
def caplog_loguru(caplog):
    """
    由于 datacli.py 使用 loguru 记录日志，标准 caplog 无法捕获。
    此 fixture 将 loguru 的输出重定向到 pytest 的 handler。
    """
    handler_id = logger.add(caplog.handler, format="{message}")
    yield caplog
    logger.remove(handler_id)

@pytest.fixture
def mock_kwargs():
    """模拟 DataCLI 初始化参数"""
    return {
        "provider_uri": "~/.qlib/qlib_data/cn_data"
    }

# --- 2. 测试用例 ---

def test_need_update_logic(mock_kwargs):
    """验证当本地日期与线上日期不一致时，触发更新"""
    cli = DataCLI(region="cn", **mock_kwargs)

    # 场景 A: 日期一致，无需更新
    with patch("datacli.get_latest_trade_date_ak", return_value="2024-01-01"), \
         patch("datacli.get_local_data_date", return_value="2024-01-01"):
        assert cli.need_update() is False

    # 场景 B: 本地数据落后，需要更新
    with patch("datacli.get_latest_trade_date_ak", return_value="2024-01-02"), \
         patch("datacli.get_local_data_date", return_value="2024-01-01"):
        assert cli.need_update() is True

@patch("datacli.run_command")
def test_update_command_generation(mock_run, mock_kwargs):
    """验证 update 方法是否正确生成了带代理的 wget 命令"""
    cli = DataCLI(region="cn", **mock_kwargs)

    with patch.object(cli, 'need_update', return_value=True), \
         patch.object(cli, 'status'):

        cli.update(proxy="B")

        # 验证命令调用
        calls = [call[0][0] for call in mock_run.call_args_list]
        assert any("https://hk.gh-proxy.org/" in cmd for cmd in calls)
        assert any("wget" in cmd for cmd in calls)

@patch("datacli.get_local_data_date")
def test_status_logging(mock_get_local, mock_kwargs, caplog_loguru):
    """
    【已修复】使用 caplog_loguru 验证 status 方法的日志输出
    """
    mock_get_local.return_value = "2023-12-31"
    cli = DataCLI(region="cn", **mock_kwargs)

    cli.status()

    # 现在 caplog_loguru.text 能够正确获取 loguru 的输出了
    assert "Checking local data status... 2023-12-31" in caplog_loguru.text
