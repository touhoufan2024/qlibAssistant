import pytest
import sys
import os
import pandas as pd
from unittest.mock import patch, MagicMock
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
roll_dir = os.path.join(root_dir, "roll")
if roll_dir not in sys.path:
    sys.path.append(roll_dir)

from utils import (
    process_stock_code_v2,
    check_match,
    check_match_in_list,
    filter_csv,
    calculate_file_sha256
)

# 1. 测试基础逻辑函数 (最容易提升覆盖率)
def test_process_stock_code_v2():
    """测试股票代码标准化"""
    assert process_stock_code_v2("600000") == "SH600000"
    assert process_stock_code_v2("000001") == "SZ000001"
    assert process_stock_code_v2("300001") == "SZ300001"
    assert process_stock_code_v2("830000") == "BJ830000"
    assert process_stock_code_v2("999999") == "unknown999999"

def test_check_match():
    """测试正则匹配"""
    assert check_match("EXP_XGBoost", r"XGB") is True
    assert check_match("EXP_LGBM", r"XGB") is False

def test_check_match_in_list():
    """测试列表正则匹配"""
    regex_list = [r"XGB", r"LGB"]
    assert check_match_in_list("EXP_XGBoost", regex_list) is True
    assert check_match_in_list("EXP_Linear", regex_list) is False

# 2. 测试涉及文件的函数 (使用 tmp_path 避免污染本地)
def test_calculate_file_sha256(tmp_path):
    """测试文件哈希计算"""
    d = tmp_path / "test.txt"
    d.write_text("hello world")

    # 预计算好的 "hello world" sha256
    expected = "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
    assert calculate_file_sha256(d) == expected

    # 测试文件不存在的情况
    assert calculate_file_sha256("non_existent_file.txt") is None

# 3. 测试 Pandas 数据处理逻辑 (使用 Mock 模拟读取)
def test_filter_csv(tmp_path):
    """测试 CSV 过滤逻辑"""
    csv_file = tmp_path / "data.csv"
    # 构造测试数据：A符合条件，B score不符合，C pos_ratio不符合
    df = pd.DataFrame({
        'instrument': ['SH600000', 'SZ000001', 'BJ830000'],
        'avg_score': [1.5, -0.1, 1.2],
        'pos_ratio': [0.9, 0.9, 0.5]
    })
    df.to_csv(csv_file, index=False)

    result = filter_csv(csv_file)
    assert result == "600000"  # 只有第一行满足 avg_score > 0 且 pos_ratio > 0.8
    assert "000001" not in result

# 4. 测试网络请求相关 (必须使用 Mock)
@patch('requests.get')
def test_get_latest_url_success(mock_get):
    """模拟成功的 URL 追踪"""
    from utils import get_latest_url
    mock_response = MagicMock()
    mock_response.url = "https://final-link.com"
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    assert get_latest_url("https://base-link.com") == "https://final-link.com"

# 5. 测试异常处理
def test_filter_csv_exception():
    """测试 CSV 过滤遇到错误时的处理"""
    # 传入一个不存在的路径
    result = filter_csv("invalid_path.csv")
    assert result == ""
