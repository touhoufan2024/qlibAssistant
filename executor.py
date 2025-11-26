from abc import ABC, abstractmethod
from utils import get_config
import os
from loguru import logger
import requests
import subprocess
import utils
from utils import ConfigLoader

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

    def runTask(self, cmd):
        logger.info(f"Executing command: {cmd}")
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
            logger.info("命令输出:")
            logger.info(result.stdout)
            return result.stdout  # 返回命令输出字符串
        except subprocess.CalledProcessError as e:
            logger.info("命令执行失败！")
            logger.info(f"命令: {e.cmd}")
            logger.info(f"退出状态码: {e.returncode}")
            logger.info(f"标准错误输出: {e.stderr}")
            return None
        except FileNotFoundError as e:
            logger.info("未找到命令！")
            logger.info(f"错误信息: {e}")
            return None
        except Exception as e:
            logger.info("发生未知错误！")
            logger.info(f"错误信息: {e}")
            return None


    def runTasks(self):
        self.config.mkdir_output_folder()
        if self.config.output_folder_is_exists():
            logger.info("Output folder already exists, skipping execution.")
            return None
        for cmd in self.config.get_qrun_cmd_list():
            self.runTask(cmd)


if __name__ == "__main__":
    cfig = utils.ConfigLoader()
    exec = ExecuteYamls(cfig)
    print(exec.config.get_qrun_cmd_list())
    exec.runTasks()