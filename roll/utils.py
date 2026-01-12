import subprocess
import requests
from bs4 import BeautifulSoup
import re
from loguru import logger
import os
import hashlib

import re
os.environ['http_proxy'] = 'http://127.0.0.1:10808'
os.environ['https_proxy'] = 'http://127.0.0.1:10808'

def check_match(strA, strB):
    """
    判断 strA 中是否存在符合正则表达式 strB 的内容
    :param strA: 目标字符串
    :param strB: 正则表达式 (Pattern)
    :return: Boolean
    """
    # re.search 扫描整个字符串并返回第一个成功的匹配，如果没有匹配则返回 None
    if re.search(strB, strA):
        return True
    else:
        return False


def check_match_in_list(strA, regex_list):
    """
    strA: 目标字符串
    regex_list: 正则表达式列表 (原 strB)
    返回: 如果 regex_list 中有任意一个正则能匹配到 strA，返回 True
    """
    # 只要有一个 pattern 能在 strA 中 search 到，就返回 True
    return any(re.search(pattern, strA) for pattern in regex_list)

def get_latest_url(base_url):
    response = requests.get(base_url, allow_redirects=True, timeout=(50, 100))
    response.raise_for_status()
    logger.info(f"最终下载链接: {response.url}")
    return response.url

def run_command(cmd):
    """
    执行 Shell 命令并返回返回码、标准输出和标准错误。
    
    Args:
        cmd (str): 要执行的命令字符串 (例如: "ls -la")
        
    Returns:
        tuple: (returncode, stdout, stderr)
            - returncode (int): 0 表示成功，非 0 表示出错
            - stdout (str): 标准输出内容
            - stderr (str): 标准错误内容
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


def calculate_file_sha256(file_path):
    # 创建一个 sha256 对象
    sha256_hash = hashlib.sha256()
    
    try:
        # 以二进制只读模式打开文件 ('rb')
        #这是计算哈希的关键，不能用 'r'，否则换行符会导致哈希值错误
        with open(file_path, "rb") as f:
            # 分块读取，每次读 4096 字节 (4KB) 或者是它的倍数
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        
        # 返回十六进制字符串
        return sha256_hash.hexdigest()
        
    except FileNotFoundError:
        return "文件未找到"

def get_real_github_hash(repo_url, target_filename):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    # print(f"1. 正在请求主页面: {repo_url} ...")
    try:
        session = requests.Session()
        response = session.get(repo_url, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ 请求失败: {e}")
        return

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