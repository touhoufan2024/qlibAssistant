from abc import ABC, abstractmethod
from utils import get_config
import os
from loguru import logger
import requests
import subprocess

# 更新并解压A股数据, 数据来源于github release
# TODO: 如果 数据不需要更新, 就不更新数据


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
        # self.url = get_latest_url("https://github.com/chenditc/investment_data/releases/latest") + "/qlib_bin.tar.gz"
        self.proxyA = "https://gh-proxy.org/"
        self.proxyB = "https://hk.gh-proxy.org/"
        self.proxyC = "https://cdn.gh-proxy.org/"
        self.proxyD = "https://edgeone.gh-proxy.org/"
        self.wget_cmd = f"wget --no-proxy {self.proxyB}{self.url} -O /tmp/qlib_bin.tar.gz"

    def need_update(self):
        # Implement logic to check if update is needed
        return True

    def update_data(self):
        logger.info(f"Updating data for Qlib...{self.url}")
        subprocess.run(self.wget_cmd, shell=True)
        subprocess.run("tar -zxvf /tmp/qlib_bin.tar.gz -C ~/.qlib/qlib_data/cn_data --strip-components=1", shell=True)

    def checkout_data(self):
        pass

if __name__ == "__main__":
    dataupdatater = DataUpdaterFromGithub(get_config())
    dataupdatater.update_data()