from loguru import logger
from utils import run_command, get_latest_url, get_real_github_hash, calculate_file_sha256, get_latest_trade_date_ak, get_local_data_date
import sys
import subprocess
from pathlib import Path
logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>"
)

class DataCLI:
    """
    [子模块] 数据管理: 负责行情数据的下载、更新与检查
    """
    def __init__(self, region, **kwargs):
        self.region = region

    def need_update(self):
        latest_data = get_latest_trade_date_ak()
        local_data = get_local_data_date()
        logger.info(f"最新数据日期: {latest_data}, 本地数据日期: {local_data}")
        if str(latest_data) == str(local_data):
            return False
        return True

    def update(self, proxy = "A"):
        """
        更新 A 股数据
        """
        logger.info(f"正在更新 [{self.region}] 市场数据")
        if self.need_update():
            logger.info(f"need updata data for Qlib...")
        else:
            logger.info(f"no need updata data for Qlib...")
            self.status()
            return
        run_command("cd ~/investment_data && bash ./dump_qlib_bin.sh")
        self.status()

    def status(self):
        """检查本地数据最新日期"""
        logger.info(f"正在检查本地数据日历... {get_local_data_date()}")