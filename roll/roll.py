#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import yaml
import fire
from loguru import logger
from typing import Dict, Any, Optional

# 内部模块导入
from utils import get_local_data_date, fix_mlflow_paths
from datacli import DataCLI
from traincli import TrainCLI
from modelcli import ModelCLI

class RollingTrader:
    def __init__(self, config_path: str = "./config.yaml", **kwargs):
        # 1. 初始化基础参数
        self.config_path = config_path
        self.params: Dict[str, Any] = {
            "region": "cn",
            "predict_dates": None,
            "provider_uri": None
        }

        # 2. 加载并合并配置
        self._load_and_merge_config(kwargs)

        # 3. 自动补全缺失的关键参数
        self._ensure_predict_dates()

        # 4. 属性绑定 (解决 VALUE 注释映射问题)
        for key, value in self.params.items():
            setattr(self, key, value)

        self.show_config()
        # 5. 子命令装载
        self.data = DataCLI(**self.params)
        self.train = TrainCLI(**self.params)
        self.model = ModelCLI(**self.params)

        # 6. 环境修复
        fix_mlflow_paths(self.params.get("mlruns_dir"))

    def _load_and_merge_config(self, cli_args: Dict[str, Any]):
        """加载文件配置并与命令行参数合并，CLI 优先级最高"""
        if not os.path.exists(self.config_path):
            logger.error(f"配置文件未找到: {self.config_path}")
            # 不直接 exit，允许完全通过 CLI 驱动
            self.params.update(cli_args)
            return

        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                file_config = yaml.safe_load(f) or {}
                self.params.update(file_config)
            logger.info(f"成功加载配置: {self.config_path}")
        except Exception as e:
            logger.warning(f"解析配置文件失败: {e}，将使用默认参数。")

        # 命令行参数覆盖文件配置
        self.params.update(cli_args)

    def _ensure_predict_dates(self):
        """如果未指定预测日期，自动获取数据集中最新的日期"""
        if self.params.get('predict_dates') is None and self.params.get('provider_uri'):
            try:
                latest_date = get_local_data_date(self.params["provider_uri"]).strip()
                self.params['predict_dates'] = [{"start": latest_date, "end": latest_date}]
                logger.info(f"自动补全预测日期 (数据集最新): {latest_date}")
            except Exception as e:
                logger.error(f"无法自动获取最新日期: {e}")

    def show_config(self):
        """显示当前生效的最终配置参数"""
        from pprint import pprint
        print("\n=== Current Effective Configuration ===")
        pprint(self.params)
        print("=======================================\n")

if __name__ == "__main__":
    fire.Fire(RollingTrader)
