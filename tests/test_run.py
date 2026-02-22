import pytest
import subprocess
from unittest.mock import patch, MagicMock
from loguru import logger
from pathlib import Path
import os
import sys

root_dir = Path(__file__).resolve().parent.parent
roll_dir = os.path.join(root_dir, "script")
if roll_dir not in sys.path:
    sys.path.insert(0, roll_dir)
import run  # 确保 run.py 在你的 roll 目录下或已加入 sys.path

# --- 1. 核心固件：桥接 Loguru 与 Pytest ---
@pytest.fixture
def caplog_loguru(caplog):
    """
    由于 run.py 使用 loguru 记录日志，标准 caplog 无法捕获。
    此 fixture 将 loguru 的输出重定向到 pytest 的 handler。
    """
    # 添加一个临时 handler 到 loguru
    handler_id = logger.add(caplog.handler, format="{message}")
    yield caplog
    # 测试完成后移除，防止干扰其他测试
    logger.remove(handler_id)

# --- 2. 测试用例 ---

@patch('run.subprocess.run')
def test_run_batch_experiments_logic(mock_subprocess):
    """
    验证实验组合生成逻辑
    预期：4(模型) * 1(数据集) * 1(股票池) * 2(滚动类型) = 8 次调用
    """
    run.run_batch_experiments()

    # 验证总调用次数
    assert mock_subprocess.call_count == 8

    # 验证第一个生成的命令字符串内容
    first_call_args = mock_subprocess.call_args_list[0][0][0]
    assert 'python ./roll.py' in first_call_args
    assert '--model_name="XGBoost"' in first_call_args
    assert 'train start' in first_call_args

@patch('run.subprocess.run')
def test_run_batch_error_handling(mock_subprocess, caplog_loguru):
    """
    验证异常处理：当某个任务失败时，脚本应记录错误并继续执行下一个
    """
    # 模拟第一次调用抛出 CalledProcessError，后续调用正常
    mock_subprocess.side_effect = [
        subprocess.CalledProcessError(returncode=1, cmd='test_cmd'),
        MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock()
    ]

    run.run_batch_experiments()

    # 验证错误日志是否被正确捕获
    assert "任务 [1/8] 失败!" in caplog_loguru.text
    assert "跳过此任务，继续下一个..." in caplog_loguru.text

    # 验证即使有失败，总调用次数依然是 8
    assert mock_subprocess.call_count == 8

@patch('run.subprocess.run')
def test_run_batch_keyboard_interrupt(mock_subprocess, caplog_loguru):
    """
    验证用户中断逻辑：当捕获到 Ctrl+C 时，应立即停止
    """
    # 模拟用户按下 Ctrl+C
    mock_subprocess.side_effect = KeyboardInterrupt()

    run.run_batch_experiments()

    # 验证终止日志
    assert "用户手动停止脚本" in caplog_loguru.text
    # 验证在第一次中断后就停止了，不再继续后续任务
    assert mock_subprocess.call_count == 1
