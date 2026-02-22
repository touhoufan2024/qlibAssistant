import sys
from pathlib import Path

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
        wget_cmd = f"wget --no-proxy {use_proxy}{url} -O ~/tmp/qlib_bin.tar.gz"
        logger.info(f"使用代理 [{proxy}] 下载数据包...")

        run_command(wget_cmd)
        run_command("tar -zxvf ~/tmp/qlib_bin.tar.gz -C ~/.qlib/qlib_data/cn_data --strip-components=1")
        logger.info("数据更新完成。")
        self.status()

    def status(self) -> None:
        """Check local data update status"""
        logger.info(f"Checking local data status... {get_local_data_date(self.kwargs['provider_uri'])}")
