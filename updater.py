from abc import ABC, abstractmethod
from utils import get_config
import os
from loguru import logger

class DataUpdater(ABC):
    def __init__(self, config, update_needed=True):
        self.config = config
        self.update_needed = update_needed

    @abstractmethod
    def update_data(self):
        pass

class DataUpdaterFromGithub(DataUpdater):
    def __init__(self, config, update_needed=True):
        super().__init__(config, update_needed)

    def update_data(self):
        logger.info("Updating data for Qlib...")
        pass

if __name__ == "__main__":
    dataupdatater = DataUpdaterFromGithub(get_config())
    dataupdatater.update_data()