import sys
from pathlib import Path
import requests
import tarfile
import shutil
import time
from loguru import logger
from utils import (
    run_command,
    get_latest_trade_date_ak,
    get_local_data_date
)

class DataCLI:
    """
    Data management submodule: handles market data download, update and verification
    """
    def __init__(self, region: str, **kwargs):
        self.region = region
        self.kwargs = kwargs

    def need_update(self) -> bool:
        """Check if data needs to be updated"""
        latest_data = get_latest_trade_date_ak()
        local_data = get_local_data_date(self.kwargs["provider_uri"])
        logger.info(f"Latest data date: {latest_data}, Local data date: {local_data}")
        if str(latest_data) == str(local_data):
            return False
        return True

    def update(self, proxy = "A"):
        """
        Update market data for the specified region
        """
        logger.info(f"Updating [{self.region}] market data")
        if self.need_update():
            logger.info("Updating Qlib data...")
        else:
            logger.info("Qlib data is up to date")
            self.status()
            return

        proxy_a = "https://gh-proxy.org/"
        proxy_b = "https://hk.gh-proxy.org/"
        proxy_c = "https://cdn.gh-proxy.org/"
        proxy_d = "https://edgeone.gh-proxy.org/"
        url = "https://github.com/chenditc/investment_data/releases/latest/download/qlib_bin.tar.gz"

        proxy_map = {
            "A": proxy_a,
            "B": proxy_b,
            "C": proxy_c,
            "D": proxy_d
        }
        use_proxy = proxy_map.get(proxy.upper(), proxy)
        
        # 跨平台路径处理
        tmp_dir = Path.home() / "tmp"
        tmp_dir.mkdir(parents=True, exist_ok=True)
        target_file = tmp_dir / "qlib_bin.tar.gz"
        
        full_url = f"{use_proxy}{url}"
        logger.info(f"使用代理 [{proxy}] 下载数据包: {full_url}")
        
        # 使用 requests 实现跨平台下载
        try:
            with requests.get(full_url, stream=True, timeout=(10, 300)) as r:
                r.raise_for_status()
                with open(target_file, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
        except Exception as e:
            logger.error(f"数据下载失败: {e}")
            sys.exit(1)

        # 确保目标目录存在，再解压
        target_dir = Path(self.kwargs["provider_uri"]).expanduser()
        target_dir.mkdir(parents=True, exist_ok=True)

        try:
            with tarfile.open(target_file, "r:gz") as tar:
                    # 1. 自动安全地获取顶层目录名（以 / 结尾）
                    # 如果压缩包为空或格式不对，这里需要容错，通常第一个成员是根
                    members = tar.getmembers()
                    if not members:
                        raise Exception("压缩包为空")
                    
                    # 获取第一个成员的名字作为根目录名前缀，例如 "qlib_bin/"
                    root_name = members[0].name.split('/')[0] + '/'
                    
                    # 2. 遍历所有成员，计算去除根目录后的路径
                    for member in members:
                        if not member.name.startswith(root_name):
                            continue  # 忽略压缩包内不由根目录包裹的文件（通常没有）
                        
                        # 计算新的相对路径 (例如: qlib_bin/cn/day.txt -> cn/day.txt)
                        rel_path = member.name[len(root_name):]
                        
                        # 忽略原本的顶层文件夹本身，避免解压出空文件
                        if not rel_path:
                            continue
                        
                        # 计算最终的绝对路径
                        final_path = target_dir / rel_path
                        
                        if member.isdir():
                            # 如果是文件夹，只需确保目录存在
                            final_path.mkdir(parents=True, exist_ok=True)
                        elif member.isfile():
                            # 如果是文件，安全地解压其内容
                            # 确保其父目录存在
                            final_path.parent.mkdir(parents=True, exist_ok=True)
                            
                            # 读取原文件内容流并拷贝到新路径
                            with tar.extractfile(member) as f_source, open(final_path, "wb") as f_dest:
                                shutil.copyfileobj(f_source, f_dest)
        except Exception as e:
            logger.error(f"数据解压失败: {e}")
            sys.exit(1)

        logger.info("数据更新完成。")
        self.status()

    def status(self) -> None:
        """Check local data update status"""
        logger.info(f"Checking local data status... {get_local_data_date(self.kwargs['provider_uri'])}")
