import os
import fire
from loguru import logger
from pathlib import Path
from typing import Dict, Any, List

# 核心导入改为延迟加载，防止 Windows 子进程启动时反复触发 import 警告
from .utils.calendar import WFCalendar
from .core.config import load_wf_config
from .core.state import WFStateManager
from .core.task_builder import WFTaskBuilder
from .core.train import run_train_process

class WalkForwardCLI:
    def __init__(self, config_path: str = "./walk_forward_config.yaml"):
        self.config = load_wf_config(config_path)
        self.calendar = WFCalendar(self.config.provider_uri)
        self.state_manager = WFStateManager("./wf_state.json", self.config.mlruns_uri)
        
        # 不再在 __init__ 提前调用 qlib.init()。
        # 直接构建配置字典，这样主进程在启动子进程前是“干净”的。
        self.qlib_config = {
            "provider_uri": self.config.provider_uri,
            "region": "cn",
            "exp_manager": {
                "class": "MLflowExpManager",
                "module_path": "qlib.workflow.expm",
                "kwargs": {
                    "uri": "file:" + str(Path(self.config.mlruns_uri).expanduser()),
                    "default_exp_name": "WF_Experiment"
                }
            }
        }
        
    def analyze(self):
        """查看并打印训练指标、步进测试集 IC 及回测表现"""
        # 仅在分析时导入重量级组件
        import pandas as pd
        from .core.analyzer import WFAnalyzer
        from tabulate import tabulate

        analyzer = WFAnalyzer(self.qlib_config, self.state_manager.history)
        
        # 1. 打印训练阶段指标
        print("\n" + "="*30 + " 1. 训练阶段模型指标 (Training Metrics) " + "="*30)
        train_metrics = analyzer.get_training_metrics()
        if not train_metrics.empty:
            print(tabulate(train_metrics, headers='keys', tablefmt='psql', floatfmt=".4f"))
        else:
            print("暂无训练记录。")

        # 2. 自动寻找最新的预测结果文件进行分析
        output_dir = Path("./walk_forward_output")
        pred_files = list(output_dir.glob("wf_predictions_*.csv"))
        if not pred_files:
            print("\n未找到预测结果文件，请先运行 run 命令。")
            return
        
        latest_pred = max(pred_files, key=lambda x: x.stat().st_mtime)
        print(f"\n" + "="*30 + f" 2. 测试集真实表现分析 (File: {latest_pred.name}) " + "="*30)
        
        results = analyzer.analyze_test_performance(str(latest_pred), self.config.stock_pool)
        
        # 打印测试集 IC
        ic_df = pd.DataFrame([results["ic_stats"]])
        print("\n[ 测试集真实 IC/ICIR (Out-of-Sample) ]")
        print(tabulate(ic_df, headers='keys', tablefmt='psql', floatfmt=".4f"))
        
        # 打印回测统计
        bt_df = pd.DataFrame([results["backtest_stats"]])
        print("\n[ 模拟回测表现 (Top 30 等权) ]")
        print(tabulate(bt_df, headers='keys', tablefmt='psql', floatfmt=".4f"))
        print("\n" + "="*100 + "\n")

    def run(self):
        """核心运行入口"""
        # 状态自检
        self.state_manager.verify_consistency()
        
        # 计算所有重训触发点 T_i
        start_date = self.config.start_date
        end_date = self.config.end_date or self.calendar.trade_dates[-1]
        
        triggers = self.calendar.generate_retrain_dates(
            start_date, end_date, 
            self.config.trigger_unit, self.config.trigger_interval
        )
        logger.info(f"生成重训计划点: {len(triggers)} 个")

        # --- 阶段 A: 步进处理 ---
        for i, ti in enumerate(triggers):
            logger.info(f"--- 步进处理第 {i+1}/{len(triggers)} 个区间 [T_i: {ti}] ---")
            
            # 找到下个重训点作为区间边界
            next_ti = triggers[i+1] if i + 1 < len(triggers) else end_date
            
            # A-1: 训练环节 (检查状态，避免重复训练)
            event = next((e for e in self.state_manager.history if e["retrain_date"] == ti), None)
            
            if not event:
                logger.info(f"点 {ti} 未训练，开始派发任务...")
                ti_rids = {}
                for task_cfg in self.config.tasks:
                    segments = self.calendar.generate_split_segments(
                        ti, task_cfg.lookback_unit, task_cfg.lookback_length, 
                        task_cfg.split.method, task_cfg.split.train, task_cfg.split.valid
                    )
                    task = WFTaskBuilder.build_task(
                        task_cfg.model_name, task_cfg.dataset_name, 
                        self.config.stock_pool, segments
                    )
                    
                    exp_name = f"WF_{task_cfg.name}"
                    
                    # 派发训练 (注意：这里现在返回的是 rid 或 None)
                    rid = run_train_process(task, exp_name, self.qlib_config)
                    
                    if rid:
                        ti_rids[task_cfg.name] = rid
                    else:
                        logger.error(f"任务 {task_cfg.name} 训练失败！")
                
                if ti_rids:
                    self.state_manager.save_retrain_event(ti, ti_rids)
                    event = {"retrain_date": ti, "tasks": ti_rids}
            else:
                logger.info(f"点 {ti} 已有有效训练记录。")

            # --- 阶段 B: 推理 (暂且保持注释) ---
            """
            if event:
                logger.info(f"推理步骤待后续整合...")
            """

        logger.info("✨ Walk-Forward 流程执行结束。")

if __name__ == "__main__":
    fire.Fire(WalkForwardCLI)
