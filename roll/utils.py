import os
import re
import sys
import subprocess
import hashlib
import datetime
from typing import Optional, Tuple, List, Union

# Third party imports
import requests
from bs4 import BeautifulSoup
import akshare as ak
import pandas as pd
from loguru import logger

def check_match(strA: str, strB: str) -> bool:
    """
    Check if strA contains any matches for regex pattern strB
    
    Args:
        strA: Target string to search
        strB: Regex pattern to match against
        
    Returns:
        bool: True if pattern matches, False otherwise
    """
    # re.search 扫描整个字符串并返回第一个成功的匹配，如果没有匹配则返回 None
    if re.search(strB, strA):
        return True
    else:
        return False

def filter_csv(file_path):
    df = pd.read_csv(file_path)

    df2 = df[df['avg_score'] > 0].copy()
    filtered_df = df2[df['pos_ratio'] > 0.8].copy()

    def clean_code(text):
        return "".join(re.findall(r'\d+', str(text)))

    stock_codes = filtered_df['instrument'].apply(clean_code).tolist()

    result_string = ",".join(stock_codes)

    return result_string

def check_match_in_list(strA, regex_list):
    """
    strA: 目标字符串
    regex_list: 正则表达式列表 (原 strB)
    返回: 如果 regex_list 中有任意一个正则能匹配到 strA，返回 True
    """
    # 只要有一个 pattern 能在 strA 中 search 到，就返回 True
    return any(re.search(pattern, strA) for pattern in regex_list)

def get_latest_url(base_url: str) -> str:
    """
    Follow URL redirects to get final download URL
    
    Args:
        base_url: Starting URL that may redirect
        
    Returns: 
        Final resolved URL after following all redirects
        
    Raises:
        requests.HTTPError: If request fails
    """
    response = requests.get(base_url, allow_redirects=True, timeout=(50, 100))
    response.raise_for_status()
    logger.info(f"Final download URL: {response.url}")
    return response.url

def run_command(cmd: str) -> Tuple[int, str, str]:
    """
    Execute shell command and return exit code and output
    
    Args:
        cmd: Shell command string to execute

    Returns:
        Tuple containing:
        - returncode: Exit code (0 = success)
        - stdout: Standard output text  
        - stderr: Standard error text

    Note:
        Uses subprocess.run() which is recommended for Python 3.5+
        shell=True enables shell features like ~ expansion and pipes
    """
    try:
        # subprocess.run 是 Python 3.5+ 推荐的方式
        # shell=True: 允许以字符串形式传入命令，并支持 Shell 特性（如 ~ 展开、管道 | 等）
        # capture_output=True: 捕获 stdout 和 stderr (Python 3.7+)
        # text=True: 将输出解码为字符串 (str)，而不是字节 (bytes)
        result = subprocess.run(
            cmd, 
            shell=True, 
            capture_output=True, 
            text=True
        )
        
        # 返回结果 (去除末尾多余的换行符通常是个好习惯，如果需要保留可去掉 .strip())
        return result.returncode, result.stdout.strip(), result.stderr.strip()
        
    except Exception as e:
        # 如果调用过程中出现 Python 层面的异常（非常少见，通常是环境问题）
        return -1, "", str(e)


def calculate_file_sha256(file_path: str) -> Optional[str]:
    """Calculate SHA256 hash of file content
    
    Args:
        file_path: Path to file to hash
        
    Returns:
        str: SHA256 hex digest 
        None: If file not found
        
    Note:
        Uses rb mode to properly handle binary files
    """
    sha256_hash = hashlib.sha256()
    
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        logger.warning(f"File not found: {file_path}")
        return None

def get_real_github_hash(repo_url: str, target_filename: str) -> Optional[str]:
    """Get SHA256 hash of GitHub release asset
    
    Args:
        repo_url: GitHub release page URL
        target_filename: Exact filename to lookup
        
    Returns:
        str: SHA256 hash string if found
        None: If unable to find hash
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    }

    try:
        session = requests.Session()
        response = session.get(repo_url, headers=headers)
        response.raise_for_status()
    except Exception as e:
        logger.error(f"Failed to fetch GitHub page: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # --- 关键步骤：处理 GitHub 的动态加载 (include-fragment) ---
    # GitHub 现在通常把 Assets 列表放在一个独立的 URL 里加载
    # 我们寻找包含 "expanded_assets" 的 include-fragment 标签
    fragment_tag = soup.find("include-fragment", src=re.compile("expanded_assets"))

    target_soup = soup # 默认在当前页面找

    if fragment_tag:
        assets_url = fragment_tag['src']
        # 如果是相对路径，补全为绝对路径
        if not assets_url.startswith("http"):
            assets_url = "https://github.com" + assets_url
        
        # print(f"2. 检测到动态加载，正在请求资源列表: {assets_url} ...")
        try:
            resp_assets = session.get(assets_url, headers=headers)
            target_soup = BeautifulSoup(resp_assets.text, 'html.parser')
        except Exception as e:
            print(f"❌ 获取资源列表失败: {e}")
            return
    else:
        print("ℹ️ 未检测到动态加载，尝试在主页面直接查找...")

    # --- 查找文件和哈希 ---
    # 查找 href 以文件名结尾的链接
    file_link = target_soup.find("a", href=re.compile(re.escape(target_filename) + r"$"))

    if not file_link:
        print(f"❌ 错误: 即使在加载资源列表后，仍未找到 '{target_filename}'。")
        return

    # print(f"✅ 已定位文件链接，正在提取哈希...")
    
    # 向上寻找包含 clipboard-copy 的容器
    current_element = file_link.parent
    found_hash = None

    for _ in range(5): # 向上找5层
        if not current_element: break
        
        # 查找 value 属性包含 sha256 的复制按钮
        clipboard = current_element.find("clipboard-copy")
        if clipboard and clipboard.get("value"):
            val = clipboard["value"]
            if "sha256" in val:
                found_hash = val[7:]
                break
        current_element = current_element.parent

    if found_hash:
        return found_hash
        print("\n" + "="*40)
        print(f"文件: {target_filename}")
        print(f"哈希: {found_hash}")
        print("="*40)
    else:
        print("⚠️ 找到了文件，但在旁边没有发现哈希值（可能该文件类型GitHub未计算显示哈希）。")
        exit(1)


def append_to_file(file_path, content):
    """
    向指定文件末尾追加字符串。
    
    :param file_path: 文件路径
    :param content: 要追加的字符串内容
    """
    try:
        # mode='a' 代表 append (追加模式)
        # encoding='utf-8' 防止中文乱码
        with open(file_path, mode='a', encoding='utf-8') as f:
            f.write(content)
        # print(f"成功追加内容到: {file_path}")
    except Exception as e:
        print(f"写入失败: {e}")

def process_stock_code_v2(code: str) -> str:
    """Process stock code to standardized format with exchange prefix
    
    Args:
        code: Raw stock code (e.g. '600000', '000001')
        
    Returns:
        str: Standardized code with exchange prefix (e.g. 'SH600000')
        
    Note:
        Supports SH/SZ/BJ exchanges and filters B-shares
    """
    code = str(code)
    
    if code.startswith("6"):  # Shanghai
        return f"SH{code}"
    elif code.startswith(("0", "3")):  # Shenzhen
        return f"SZ{code}"
    elif code.startswith(("8", "4", "920")):  # Beijing
        return f"BJ{code}"
    elif code.startswith("900"):  # Shanghai B-share (filter)
        return f"SH{code}"
    elif code.startswith("200"):  # Shenzhen B-share (filter)
        return f"SZ{code}"
    else:
        return f"unknown{code}"

def get_normalized_stock_list() -> pd.DataFrame:
    """Get normalized stock list from AkShare
    
    Returns:
        DataFrame with normalized stock codes
        
    Note:
        Automatically clears proxy settings before request
    """
    logger.info("Clearing proxy settings...")
    for key in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy']:
        if key in os.environ:
            logger.debug(f"Removing {key}")
            del os.environ[key]
    """
    获取 AkShare 数据并立刻标准化的完整流程
    """
    print("正在从 AkShare 拉取实时行情...")
    df = ak.stock_info_a_code_name()
    # df = ak.stock_zh_a_spot()
    data = df['code'].apply(process_stock_code_v2)
    df['code'] = data
    # print(df)
    return df

def get_latest_trade_date_ak():
    # 1. 获取新浪财经的交易日历
    # 这个接口返回的是历史上所有交易日（含今天）
    trade_calendar = ak.tool_trade_date_hist_sina()
    trade_days = trade_calendar['trade_date'].tolist()

    # 转换为 datetime.date 方便比较
    # trade_days 已经是 datetime.date 格式

    now = datetime.datetime.now()
    today = now.date()
    current_hour = now.hour

    # 2. 找到今天在日历中的位置（或今天之前的最后一个交易日）
    # 过滤掉未来的日期
    past_trade_days = [d for d in trade_days if d <= today]

    if not past_trade_days:
        return None

    last_trade_day = past_trade_days[-1]

    # 3. 判断逻辑
    if today == last_trade_day:
        # 如果今天是交易日，判断是否已经收盘 (A股15:00收盘)
        # 考虑到数据同步延迟，通常建议设为 15:05 或 15:10
        if current_hour < 15:
            # 尚未收盘，取上一个交易日
            return past_trade_days[-2]
        else:
            # 已经收盘，今天就是“上一个已收盘交易日”
            return last_trade_day
    else:
        # 今天不是交易日（周末或节假日），直接返回最近的一个
        return last_trade_day


def get_local_data_date():
    code, stdout, stderr = run_command("tail -n 1 ~/.qlib/qlib_data/cn_data/calendars/day.txt")
    return stdout
