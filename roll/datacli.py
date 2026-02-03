import sys
from pathlib import Path

from loguru import logger
from utils import (
    run_command,
    get_latest_trade_date_ak,
    get_local_data_date
)

# Configure logger
logger.remove()
logger.add(sys.stderr, format="{time:HH:mm:ss} | {level: <8} | {message}")

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

    def update(self):
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
        run_command("cd ~/investment_data && bash ./dump_qlib_bin.sh")
        self.status()

    def status(self) -> None:
        """Check local data update status"""
        logger.info(f"Checking local data status... {get_local_data_date()}")