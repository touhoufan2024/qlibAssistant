
from abc import ABC, abstractmethod
from utils import get_config
import os
from loguru import logger
import requests
import subprocess


# 统计 某个mlrun目录内的结果
# 重点关注的内容有 label 的排序, 以及性能的排序

class Collector(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def analysis(self):
        pass




class CollectorMlrunDir(Collector):
    def __init__(self, config):
        super().__init__(config)
        self.config = config

    def analysis(self, mlrun_dir = "../mlruns"):
        pass


if __name__ == "__main__":
    pass