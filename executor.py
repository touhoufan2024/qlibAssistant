from abc import ABC, abstractmethod
from utils import get_config
import os
from loguru import logger
import requests
import subprocess




class Execute(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def runTasks(self):
        pass




class ExecuteYamls(Execute):
    def __init__(self, config):
        self.config = config

    def runTasks(self):
        pass


if __name__ == "__main__":
    pass