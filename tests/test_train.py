import pytest
import os
import sys
from unittest.mock import patch, MagicMock
from pathlib import Path
import qlib

# === 1. 环境准备：路径修复 ===
root_dir = Path(__file__).resolve().parent.parent
roll_dir = os.path.join(root_dir, "roll")
if roll_dir not in sys.path:
    sys.path.insert(0, roll_dir)

# === 2. 核心补丁：修复 ExpManager 初始化错误 ===
# 解决 TypeError: ExpManager.__init__() missing 'default_exp_name'
@pytest.fixture(scope="session", autouse=True)
def global_qlib_init():
    """在整个测试会话开始前，初始化一个虚假的 Qlib 环境"""
    qlib.init(
        provider_uri="~/.qlib/qlib_data/cn",
        region="cn",
        exp_manager={
            "class": "MLflowExpManager",
            "module_path": "qlib.workflow.expm",
            "kwargs": {
                "uri": "file:./mlruns",
                "default_exp_name": "test_default"
            }
        }
    )

# 延迟导入，确保初始化完成
from traincli import TrainCLI, run_train_blocking, my_enhanced_handler_mod

# === 3. 测试用例 ===

def test_handler_mod_logic():
    """验证自定义处理器是否正确修复了时间占位符"""
    task = {
        "dataset": {
            "kwargs": {
                "segments": {"train": ("2020-01-01", "2020-12-31")},
                "handler": {"kwargs": {"fit_start_time": None, "fit_end_time": None}}
            }
        }
    }
    with patch('traincli.default_handler_mod'):
        my_enhanced_handler_mod(task, MagicMock())

    h_kwargs = task["dataset"]["kwargs"]["handler"]["kwargs"]
    assert h_kwargs["fit_start_time"] == "2020-01-01"
    assert h_kwargs["fit_end_time"] == "2020-12-31"

@patch('multiprocessing.Process')
def test_run_train_blocking_process_flow(mock_process):
    """测试多进程启动、阻塞与退出码判断"""
    instance = mock_process.return_value
    instance.exitcode = 0
    assert run_train_blocking({"task": 1}, "exp") is True

    instance.exitcode = 1
    assert run_train_blocking({"task": 1}, "exp") is False

@patch('traincli.get_my_config')
@patch('traincli.RollingGen')
def test_train_cli_initialization(mock_gen, mock_config):
    """测试 TrainCLI 初始化及参数流转"""
    mock_config.return_value = [{"model": "test"}]

    kwargs = {
        "uri_folder": "./mlruns",
        "provider_uri": "./data",
        "model_name": "LGBM",
        "dataset_name": "Alpha",
        "stock_pool": "CSI300",
        "rolling_type": "step",
        "pfx_name": "pfx",
        "sfx_name": "sfx"
    }

    # 彻底隔离真实 qlib.init
    with patch('traincli.qlib.init'):
        cli = TrainCLI(step=20, **kwargs)

    assert cli.step == 20
    mock_gen.assert_called_once()


@patch('traincli.task_generator')
@patch('traincli.RollingGen')  # 关键点：Mock 掉 RollingGen 的构造函数
@patch('traincli.get_my_config')
@patch('traincli.qlib.init')
def test_train_cli_gen_output(mock_qlib_init, mock_get_config, mock_rolling_gen, mock_task_gen):
    """
    专门测试 gen() 函数生成的 task 是否正确
    """
    # 1. 模拟 get_my_config 返回的原始任务模板
    mock_template = [{"model": {"class": "DummyModel"}, "dataset": {"class": "DummyDataset"}}]
    mock_get_config.return_value = mock_template

    # 2. 模拟 task_generator 产生的滚动任务列表
    # 假设我们期望生成两个不同时间段的任务
    expected_tasks = [
        {"model": "M", "dataset": {"kwargs": {"segments": {"train": ("2020-01-01", "2020-02-01")}}}},
        {"model": "M", "dataset": {"kwargs": {"segments": {"train": ("2020-02-01", "2020-03-01")}}}}
    ]
    mock_task_gen.return_value = expected_tasks

    # 3. 初始化 TrainCLI
    # 这里的参数只需符合格式，因为底层的 qlib.init 已被 Mock
    cli = TrainCLI(
        step=40,
        uri_folder="./mlruns",
        provider_uri="./data",
        model_name="LGBM",
        dataset_name="Alpha158",
        stock_pool="CSI300",
        rolling_type="step"
    )

    # 4. 执行被测函数
    tasks = cli.gen()

    from pprint import pprint
    pprint(tasks)
    # 5. 验证逻辑
    # 验证 RollingGen 是否被正确参数化初始化
    mock_rolling_gen.assert_called_once()
    args, kwargs = mock_rolling_gen.call_args
    assert kwargs['step'] == 40
    assert kwargs['rtype'] == "step"

    # 验证 task_generator 是否接收到了模板和生成器
    mock_task_gen.assert_called_once()

    # 验证最终输出的 tasks 内容是否符合 mock 的预期
    assert len(tasks) == 2
    assert tasks[0]["dataset"]["kwargs"]["segments"]["train"][0] == "2020-01-01"
    assert tasks == expected_tasks
