import pytest
import yaml
import os
import sys
from unittest.mock import patch, MagicMock
from pathlib import Path

# 路径修复逻辑：确保测试能找到 roll 模块
root_dir = Path(__file__).resolve().parent.parent
roll_dir = os.path.join(root_dir, "roll")
if roll_dir not in sys.path:
    sys.path.insert(0, roll_dir)

# 延迟导入，防止路径未设置导致的失败
from roll import RollingTrader

# 1. 模拟子命令类，防止初始化时报错
@pytest.fixture(autouse=True)
def mock_sub_clis():
    with patch('roll.DataCLI'), \
         patch('roll.TrainCLI'), \
         patch('roll.ModelCLI'), \
         patch('roll.fix_mlflow_paths'):
        yield

# 2. 测试配置合并优先级 (CLI 覆盖文件覆盖默认)
def test_config_merging_priority(tmp_path):
    """验证参数优先级：CLI > YAML > Default"""
    # 准备一个模拟的配置文件
    config_file = tmp_path / "config.yaml"
    config_data = {
        "region": "us",           # 将被 CLI 覆盖
        "provider_uri": "path/to/data" # 将被保留
    }
    config_file.write_text(yaml.dump(config_data), encoding='utf-8')

    # 模拟初始化：传入 CLI 参数 region='cn'
    trader = RollingTrader(config_path=str(config_file), region="cn")

    # 断言结果
    assert trader.region == "cn"               # CLI 胜出
    assert trader.provider_uri == "path/to/data" # YAML 胜出
    assert trader.params["region"] == "cn"     # 内部参数字典同步更新

# 3. 测试配置文件缺失时的处理
def test_missing_config_file(capsys):
    """验证配置文件不存在时是否输出 error 并继续运行"""
    # 初始化一个不存在的路径
    trader = RollingTrader(config_path="missing.yaml", region="hk")

    trader.show_config()

    # 断言：参数依然可以从 kwargs 加载
    assert trader.region == "hk"

    # 检查日志或控制台输出 (重构后的 roll.py 不再 exit，而是记录 error)
    captured = capsys.readouterr()
    # 虽然 logger 输出在 stderr，但 show_config 会输出到 stdout
    assert "Current Effective Configuration" in captured.out

# 4. 测试属性绑定功能 (setattr)
def test_attribute_binding():
    """验证动态参数是否成功绑定到实例属性"""
    custom_val = "custom_test_value"
    trader = RollingTrader(config_path="none", custom_key=custom_val)

    # 验证 getattr
    assert getattr(trader, "custom_key") == custom_val
    assert trader.custom_key == custom_val
