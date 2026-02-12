#!/usr/bin/env python

# -*- coding: utf-8 -*-
from pprint import pprint
import sys
import yaml
import fire
import os
from loguru import logger
import requests
import subprocess
from utils import get_local_data_date, fix_mlflow_paths
from datacli import DataCLI
from traincli import TrainCLI
from modelcli import ModelCLI
from myconfig import get_my_config
# 假设这是你原本的 RollingTask 类 (保留引用以便调用)
# from original_rolling import RollingTaskExample 

class RollingTrader:
    """
    ================================================
    Qlib A股滚动交易指挥台 (RollingTrader)
    ================================================
        :param config_path: 配置文件路径 (yaml)
        :param kwargs: 命令行传递的最高优先级参数
    使用方法:
      python myroll.py data update        # 更新数据
    """
    def __init__(self, config_path="./config.yaml", **kwargs):
        # === 1. 定义默认参数 (底层兜底) ===
        final_params = {
            "exp_name": "rolling_exp",
            "region": "cn",
        }

        # === 2. 加载配置文件 (如果有) ===
        if config_path and os.path.exists(config_path):
            print(f"Loading config from: {config_path}")
            with open(config_path, 'r', encoding='utf-8') as f:
                file_params = yaml.safe_load(f)
                # 更新参数池
                if file_params:
                    final_params.update(file_params)
        else:
            logger.err(f"No config file found at: {config_path}, using defaults and CLI args only.")
            exit(0)

        if final_params['predict_dates'] is None:
            stdout = get_local_data_date(final_params["provider_uri"])
            logger.info(f"no predict_dates found in config, use lastest date in dataset: {stdout}")
            final_params['predict_dates'] = [{"start": stdout.strip(), "end": stdout.strip()}]

        # === 3. 合并命令行参数 (CLI 优先级最高，覆盖文件配置) ===
        # kwargs 包含例如 python myroll.py --region="us" 这种通过命令行强制指定的
        final_params.update(kwargs)

        # === 4. 赋值给实例变量 ===
        # 将合并后的字典变成对象的属性，方便 self.exp_name 调用
        for k, v in final_params.items():
            setattr(self, k, v)

        print(f"最终参数配置: {final_params}")

        self.final_params = final_params

        # 装载子命令
        self.data = DataCLI(**final_params)
        self.train = TrainCLI(**final_params)
        self.model = ModelCLI(**final_params)

        fix_mlflow_paths(self.final_params.get("mlruns_dir", None))


if __name__ == "__main__":
    # Fire 会自动解析类结构并生成 CLI
    fire.Fire(RollingTrader)