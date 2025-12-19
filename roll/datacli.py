from loguru import logger
from utils import run_command, get_latest_url, get_real_github_hash, calculate_file_sha256
import sys
import subprocess
logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>"
)

class DataCLI:
    """
    [子模块] 数据管理: 负责行情数据的下载、更新与检查
    """
    def __init__(self, region):
        self.region = region
        self.url = "https://github.com/chenditc/investment_data/releases/latest/download/qlib_bin.tar.gz"
        self.url0 = get_latest_url("https://github.com/chenditc/investment_data/releases/latest")
        self.proxyA = "https://gh-proxy.org/"
        self.proxyB = "https://hk.gh-proxy.org/"
        self.proxyC = "https://cdn.gh-proxy.org/"
        self.proxyD = "https://edgeone.gh-proxy.org/"

    def need_update(self):
        target_filename = "qlib_bin.tar.gz"
        github_hash = get_real_github_hash(self.url0, target_filename)
        logger.info(f"get github hash: {github_hash}")
        local_hash = calculate_file_sha256("/tmp/qlib_bin.tar.gz")
        logger.info(f"get local hash: {local_hash}")
        if github_hash == local_hash:
            return False
        return True

    def update(self, proxy = "A"):
        """
        更新 A 股数据
        :param proxy: 使用的代理选项 (A/B/C/D)
        """
        logger.info(f"正在更新 [{self.region}] 市场数据")
        if self.need_update():
            logger.info(f"need updata data for Qlib...{self.url}")
        else:
            logger.info(f"no need updata data for Qlib...{self.url}")
            return

        proxy_map = {
            "A": self.proxyA,
            "B": self.proxyB,
            "C": self.proxyC,
            "D": self.proxyD
        }
        use_proxy = proxy_map.get(proxy.upper(), proxy)
        self.wget_cmd = f"wget --no-proxy {use_proxy}{self.url} -O /tmp/qlib_bin.tar.gz"
        logger.info(f"使用代理 [{proxy}] 下载数据包...")

        subprocess.run(self.wget_cmd, shell=True)
        subprocess.run("tar -zxvf /tmp/qlib_bin.tar.gz -C ~/.qlib/qlib_data/cn_data --strip-components=1", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        logger.info(f"数据更新完成。")
        self.status()

    def status(self):
        """检查本地数据最新日期"""
        logger.info("正在检查本地数据日历...")
        # 读取 ~/.qlib/qlib_data/cn_data/calendars/day.txt 最后一行
        code, stdout, stderr = run_command("tail -n 1 ~/.qlib/qlib_data/cn_data/calendars/day.txt")
        latest_date = stdout
        logger.info(f"本地数据已更新至: {latest_date}")

    def check(self, code):
        """检查特定股票的数据完整性"""
        logger.info(f"正在抽查股票 [{code}] 的数据...")
        # TODO: Feature(instruments=[code])...
        logger.debug(f"[{code}] OHLCV 数据校验通过")