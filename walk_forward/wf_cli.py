import os
import fire
from loguru import logger
from pathlib import Path
from typing import Dict, Any, List

# 核心导入改为轻量级组件，防止 Windows 子进程启动时反复触发 import 警告
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
        
        # 定义 qlib_config 模板
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
        """查看并打印训练指标、步进测试集 IC 及双轨回测表现"""
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

        # 2. 自动寻找预测文件
        output_dir = Path("./walk_forward_output")
        pred_files = list(output_dir.glob("wf_predictions_*.csv"))
        if not pred_files:
            print("\n未找到预测结果文件，请先运行 run 命令。")
            return
        
        latest_pred = max(pred_files, key=lambda x: x.stat().st_mtime)
        print(f"\n" + "="*30 + f" 2. 测试集真实表现分析 (File: {latest_pred.name}) " + "="*30)
        
        results = analyzer.analyze_test_performance(str(latest_pred), self.config.stock_pool)
        
        # A. 打印 IC
        ic_df = pd.DataFrame([results["ic_stats"]])
        print("\n[ 样本外预测力 (Out-of-Sample) ]")
        print(tabulate(ic_df, headers='keys', tablefmt='psql', floatfmt=".4f"))
        
        # B. 打印理论回测 (Theoretical)
        theo_df = pd.DataFrame([results["theoretical_performance"]])
        print("\n[ 理论回测表现 (Top 30 等权 / 无成本 / 无限制) ]")
        print(tabulate(theo_df, headers='keys', tablefmt='psql', floatfmt=".4f"))

        # C. 打印实盘回测 (Realistic)
        real_perf = results.get("realistic_performance", {})
        if real_perf:
            real_df = pd.DataFrame([real_perf])
            print("\n[ Qlib 官方实盘模拟 (含手续费 / 涨跌停限制) ]")
            print(tabulate(real_df, headers='keys', tablefmt='psql', floatfmt=".4f"))
        
        print("\n" + "="*100 + "\n")

        # 3. 绘制分析图表
        series_data = results.get("series", {})
        if series_data:
            self._plot_analysis(latest_pred.name, series_data)

    def _plot_analysis(self, pred_filename: str, series_data: Dict[str, Any]):
        import matplotlib.pyplot as plt
        
        # 兼容 Windows 中文显示
        plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial']
        plt.rcParams['axes.unicode_minus'] = False
        
        daily_ric = series_data.get("daily_ric")
        theo_equity = series_data.get("theo_equity")
        real_equity = series_data.get("real_equity")
        
        if daily_ric is None or daily_ric.empty:
            logger.warning("没有足够的数据来绘制图表。")
            return
            
        fig, axes = plt.subplots(2, 1, figsize=(14, 10), sharex=True)
        
        # Subplot 1: Daily RankIC & Cumulative RankIC
        ax1 = axes[0]
        ax1.bar(daily_ric.index, daily_ric.values, color='skyblue', alpha=0.7, label='每日 RankIC')
        ax1.set_ylabel('RankIC', color='tab:blue')
        ax1.tick_params(axis='y', labelcolor='tab:blue')
        
        ax2 = ax1.twinx()
        cum_ric = daily_ric.cumsum()
        ax2.plot(cum_ric.index, cum_ric.values, color='darkorange', linewidth=2, label='累计 RankIC')
        ax2.set_ylabel('累计 RankIC', color='darkorange')
        ax2.tick_params(axis='y', labelcolor='darkorange')
        
        ax1.set_title("样本外 RankIC 表现", fontsize=14)
        ax1.grid(True, linestyle='--', alpha=0.4)
        
        # 合并图例
        lines_1, labels_1 = ax1.get_legend_handles_labels()
        lines_2, labels_2 = ax2.get_legend_handles_labels()
        ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')
        
        # Subplot 2: Cumulative Returns (Equity)
        ax3 = axes[1]
        if theo_equity is not None and not theo_equity.empty:
            ax3.plot(theo_equity.index, theo_equity.values, label='理论净值 (Top 30 等权 无摩擦)', linestyle='--', color='tab:green', linewidth=2)
        if real_equity is not None and not real_equity.empty:
            ax3.plot(real_equity.index, real_equity.values, label='Qlib 实盘模拟净值 (含万20双边摩擦及涨跌停限制)', color='tab:red', linewidth=2)
            
        ax3.set_title("策略净值曲线对比 (初始净值=1.0)", fontsize=14)
        ax3.set_ylabel('净值 (Equity)')
        ax3.legend(loc='upper left')
        ax3.grid(True, linestyle='--', alpha=0.6)
        
        plt.tight_layout()
        
        output_dir = Path("./walk_forward_output")
        output_dir.mkdir(parents=True, exist_ok=True)
        plot_name = pred_filename.replace('.csv', '.png').replace('wf_predictions', 'wf_analysis')
        plot_path = output_dir / plot_name
        
        plt.savefig(plot_path, dpi=150)
        plt.close()
        logger.info(f"✨ 每日 IC 及回测净值图表已生成并保存至: {plot_path}")

    def run(self):
        """核心运行入口"""
        import pandas as pd
        from .core.predict import WFPredictor

        self.state_manager.verify_consistency()
        
        start_date = self.config.start_date
        end_date = self.config.end_date or self.calendar.trade_dates[-1]
        
        triggers = self.calendar.generate_retrain_dates(
            start_date, end_date, 
            self.config.trigger_unit, self.config.trigger_interval
        )
        logger.info(f"生成重训计划点: {len(triggers)} 个")

        all_predictions = []
        predictor = WFPredictor(self.qlib_config)

        # --- 步进处理 ---
        for i, ti in enumerate(triggers):
            logger.info(f"--- 步进处理第 {i+1}/{len(triggers)} 个区间 [T_i: {ti}] ---")
            
            next_ti = triggers[i+1] if i + 1 < len(triggers) else end_date
            
            # --- 阶段 A: 训练 ---
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
                    success = run_train_process(task, exp_name, self.qlib_config)
                    
                    if success:
                        import qlib
                        import time
                        from qlib.workflow import R
                        qlib.init(**self.qlib_config)
                        exp = R.get_exp(experiment_name=exp_name)
                        
                        latest_rid = None
                        for _ in range(3):
                            rids = exp.list_recorders()
                            if rids:
                                recorders = [exp.get_recorder(recorder_id=rid) for rid in rids]
                                sorted_recs = sorted(recorders, key=lambda r: r.info['start_time'], reverse=True)
                                latest_rid = sorted_recs[0].id
                                break
                            time.sleep(1)
                        
                        if latest_rid:
                            ti_rids[task_cfg.name] = latest_rid
                            logger.info(f"成功记录 RID: {latest_rid}")
                        else:
                            logger.error(f"无法获取新生成的 RID")
                    else:
                        logger.error(f"任务 {task_cfg.name} 训练失败！")
                
                if ti_rids:
                    self.state_manager.save_retrain_event(ti, ti_rids)
                    event = {"retrain_date": ti, "tasks": ti_rids}
            else:
                logger.info(f"点 {ti} 已有有效记录。")

            # --- 阶段 B: 推理 (隔离执行) ---
            if event:
                logger.info(f"执行区间 [{ti} ~ {next_ti}) 的推理预测...")
                period_preds = []
                for task_cfg in self.config.tasks:
                    rid = event["tasks"].get(task_cfg.name)
                    if not rid: continue
                    
                    segments = self.calendar.generate_split_segments(
                        ti, task_cfg.lookback_unit, task_cfg.lookback_length, 
                        task_cfg.split.method, task_cfg.split.train, task_cfg.split.valid
                    )
                    task = WFTaskBuilder.build_task(
                        task_cfg.model_name, task_cfg.dataset_name, 
                        self.config.stock_pool, segments, end_time=next_ti
                    )
                    
                    exp_name = f"WF_{task_cfg.name}"
                    score = predictor.predict_segment(task, exp_name, rid, ti, next_ti)
                    
                    if not score.empty:
                        df_s = score.to_frame(name='score')
                        df_s['task'] = task_cfg.name
                        period_preds.append(df_s)
                
                if period_preds:
                    df_period = pd.concat(period_preds)
                    df_avg = df_period.groupby(['datetime', 'instrument'])['score'].mean().to_frame()
                    all_predictions.append(df_avg)

        # 4. 汇总结果
        if all_predictions:
            final_df = pd.concat(all_predictions).sort_index()
            output_dir = Path("./walk_forward_output")
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = output_dir / f"wf_predictions_{start_date}_{end_date}.csv"
            final_df.to_csv(output_file)
            logger.info(f"✨ Walk-Forward 推理完成！结果保存至: {output_file}")
        else:
            logger.warning("未生成任何预测结果。")

if __name__ == "__main__":
    fire.Fire(WalkForwardCLI)
