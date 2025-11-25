import os
from dataclasses import dataclass

from utils import ConfigLoader
from executor import Execute, ExecuteYamls
from updater import DataUpdater, DataUpdaterFromGithub
from collector import Collector, CollectorMlrunDir

from loguru import logger




@dataclass
class AggrTasks:
    def __init__(self, config: ConfigLoader, exec: Execute, data_updater: DataUpdater, collector: Collector):
        self.config = config
        self.data_updater = data_updater
        self.exec = exec
        self.collector = collector

    def run_aggr(self):
        logger.info("Starting aggregated tasks...")
        self.data_updater.update_data()
        self.exec.runTasks()
        self.collector.analysis()


if __name__ == "__main__":
    config = ConfigLoader()
    data_updater = DataUpdaterFromGithub(config)
    executor = ExecuteYamls(config)
    collector = CollectorMlrunDir(config)
    aggr_tasks = AggrTasks(config, executor, data_updater, collector)
    aggr_tasks.run_aggr()