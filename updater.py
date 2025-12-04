from abc import ABC, abstractmethod
from utils import get_config
import os
from loguru import logger
import requests
import subprocess

# 更新并解压A股数据, 数据来源于github release
# TODO: 如果 数据不需要更新, 就不更新数据

from bs4 import BeautifulSoup
import re

import hashlib

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


def get_latest_url(base_url):
    response = requests.get(base_url, allow_redirects=True)
    response.raise_for_status()
    return response.url

class DataUpdater(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def update_data(self):
        pass

    @abstractmethod
    def checkout_data(self):
        pass

class DataUpdaterFromGithub(DataUpdater):
    def __init__(self, config):
        super().__init__(config)
        self.url = "https://github.com/chenditc/investment_data/releases/latest/download/qlib_bin.tar.gz"
        self.url0 = get_latest_url("https://github.com/chenditc/investment_data/releases/latest")
        self.proxyA = "https://gh-proxy.org/"
        self.proxyB = "https://hk.gh-proxy.org/"
        self.proxyC = "https://cdn.gh-proxy.org/"
        self.proxyD = "https://edgeone.gh-proxy.org/"
        self.wget_cmd = f"wget --no-proxy {self.proxyA}{self.url} -O /tmp/qlib_bin.tar.gz"

    def need_update(self):
        target_filename = "qlib_bin.tar.gz"
        github_hash = get_real_github_hash(self.url0, target_filename)
        logger.info(f"get github hash: {github_hash}")
        local_hash = calculate_file_sha256("/tmp/qlib_bin.tar.gz")
        logger.info(f"get local hash: {local_hash}")
        if github_hash == local_hash:
            return False
        return True

    def update_data(self):
        logger.info(f"Updating data for Qlib...{self.url}")
        if self.need_update():
            logger.info(f"need updata data for Qlib...{self.url}")
        else:
            logger.info(f"no need updata data for Qlib...{self.url}")
            return
        subprocess.run(self.wget_cmd, shell=True)
        subprocess.run("tar -zxvf /tmp/qlib_bin.tar.gz -C ~/.qlib/qlib_data/cn_data --strip-components=1", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def checkout_data(self):
        pass

if __name__ == "__main__":
    dataupdatater = DataUpdaterFromGithub(get_config())
    dataupdatater.update_data()