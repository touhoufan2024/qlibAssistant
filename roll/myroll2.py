# -*- coding: utf-8 -*-
import sys
import fire
from loguru import logger
import requests
import subprocess
from utils import run_command
from datacli import DataCLI
from traincli import TrainCLI
from modelcli import ModelCLI
from predcli import PredCLI
from collectcli import CollectCLI
# 假设这是你原本的 RollingTask 类 (保留引用以便调用)
# from original_rolling import RollingTaskExample 

# 配置 Loguru 样式
logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>"
)


class RollingTrader:
    """
    ================================================
    Qlib A股滚动交易指挥台 (RollingTrader)
    ================================================
    
    使用方法:
      python myroll.py data update        # 更新数据
      python myroll.py train update       # 增量训练
      python myroll.py model ls           # 查看模型
      python myroll.py pred today         # 生成买单
      python myroll.py pred stock SH600519 # 个股诊断
    """
    def __init__(self, exp_name="rolling_exp", region="cn", **kwargs):
        self.exp_name = exp_name
        self.region = region
        
        # 初始化 Qlib (建议Lazy Load，这里仅打印日志)
        logger.info(f"初始化系统 | 实验名: {exp_name} | 地区: {region}")

        # 装载子命令
        self.data = DataCLI(region, **kwargs)
        self.train = TrainCLI(exp_name, **kwargs)
        self.model = ModelCLI(exp_name, **kwargs)
        self.pred = PredCLI(exp_name, **kwargs)
        self.export = CollectCLI(exp_name, **kwargs)

if __name__ == "__main__":
    # Fire 会自动解析类结构并生成 CLI
    fire.Fire(RollingTrader)