from abc import ABC, abstractmethod
from utils import get_config
import os
from loguru import logger
import requests
import subprocess

# 创建本日的目录, 用于存放今日执行的结果 
# 执行任务, 将 mlrun 路径放在 今日目录中, 将 pkl 等全部保存


class Execute(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def runTasks(self):
        pass




class ExecuteYamls(Execute):
    def __init__(self, config):
        super().__init__(config)
        self.config = config

    def runTasks(self):
        pass


if __name__ == "__main__":
    pass