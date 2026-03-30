import pandas as pd
import numpy as np
import qlib
from qlib.data import D
from qlib.workflow import R
from loguru import logger
from pathlib import Path
from typing import Dict, Any, List

class WFAnalyzer:
    def __init__(self, qlib_config: Dict[str, Any], state_history: List[Dict[str, Any]]):
        self.qlib_config = qlib_config
        self.history = state_history
        # 仅在需要时初始化 Qlib
        qlib.init(**self.qlib_config)

    def get_training_metrics(self) -> pd.DataFrame:
        """从 Recorder 中提取训练/验证阶段的指标"""
        rows = []
        for event in self.history:
            date = event["retrain_date"]
            for task_name, rid in event["tasks"].items():
                try:
                    rec = R.get_recorder(recorder_id=rid)
                    ic_pkl = rec.load_object("sig_analysis/ic.pkl")
                    ric_pkl = rec.load_object("sig_analysis/ric.pkl")
                    
                    rows.append({
                        "RetrainDate": date,
                        "Task": task_name,
                        "Train_IC": ic_pkl.mean(),
                        "Train_ICIR": ic_pkl.mean() / ic_pkl.std() if ic_pkl.std() != 0 else 0,
                        "Train_RankIC": ric_pkl.mean(),
                        "Train_RankICIR": ric_pkl.mean() / ric_pkl.std() if ric_pkl.std() != 0 else 0,
                    })
                except Exception:
                    rows.append({"RetrainDate": date, "Task": task_name, "Note": "Metrics Missing"})
        return pd.DataFrame(rows)

    def analyze_test_performance(self, prediction_file: str, stock_pool: str = "csi300") -> Dict[str, Any]:
        """分析测试集表现，结合简单计算与 Qlib 官方回测"""
        # --- 局部延迟导入：防止 Windows Spawn 过程中的导入锁死 ---
        try:
            from qlib.backtest import backtest as qlib_backtest
            from qlib.contrib.strategy import TopkDropoutStrategy
        except ImportError:
            from qlib.contrib.evaluate import backtest as qlib_backtest
            from qlib.contrib.strategy import TopkDropoutStrategy

        if not Path(prediction_file).exists():
            return {"error": f"预测文件不存在: {prediction_file}"}

        df_pred = pd.read_csv(prediction_file, parse_dates=['datetime']).set_index(['datetime', 'instrument'])
        start_date = df_pred.index.get_level_values('datetime').min()
        end_date = df_pred.index.get_level_values('datetime').max()

        # 1. 计算 IC
        logger.info(f"正在获取真实标签用于 IC 计算...")
        df_label = D.features(D.instruments(stock_pool), ['$close/Ref($close, 1) - 1'], 
                             start_time=start_date, end_time=end_date, freq='day')
        df_label.columns = ['label']
        df_combined = df_pred.merge(df_label, left_index=True, right_index=True, how='inner')
        daily_ic = df_combined.groupby('datetime').apply(lambda g: g['score'].corr(g['label']))
        daily_ric = df_combined.groupby('datetime').apply(lambda g: g['score'].corr(g['label'], method='spearman'))

        # 2. Qlib 官方回测
        logger.info("启动 Qlib 官方回测模块...")
        STRATEGY_CONFIG = {
            "topk": 30,
            "n_drop": 5,
            "signal": df_pred,
        }
        BACKTEST_CONFIG = {
            "start_time": start_date.strftime("%Y-%m-%d"),
            "end_time": end_date.strftime("%Y-%m-%d"),
            "account": 100000000,
            "benchmark": "SH000300",
            "exchange_kwargs": {
                "freq": "day",
                "limit_threshold": 0.095,
                "deal_price": "close",
                "open_cost": 0.0005,
                "close_cost": 0.0015,
                "min_cost": 5,
            },
        }
        
        strategy = TopkDropoutStrategy(**STRATEGY_CONFIG)
        report_normal, positions_normal = qlib_backtest(server=strategy, **BACKTEST_CONFIG)
        
        # 3. 手动计算关键指标
        perf = report_normal
        perf['excess'] = perf['return'] - perf['bench']
        cum_ret = (1 + perf["return"]).cumprod()
        
        annual_ret = (cum_ret.iloc[-1]) ** (250/len(perf)) - 1 if len(perf)>0 else 0
        sharpe = (perf['excess'].mean() / perf['excess'].std()) * np.sqrt(250) if perf['excess'].std() != 0 else 0
        max_dd = (cum_ret / cum_ret.cummax() - 1).min()
        
        return {
            "ic_stats": {
                "Test_IC": daily_ic.mean(),
                "Test_ICIR": daily_ic.mean() / daily_ic.std() if daily_ic.std() != 0 else 0,
                "Test_RankIC": daily_ric.mean(),
                "Test_RankICIR": daily_ric.mean() / daily_ric.std() if daily_ric.std() != 0 else 0,
            },
            "backtest_stats": {
                "Total_Return": cum_ret.iloc[-1] - 1,
                "Annualized_Return": annual_ret,
                "Sharpe_Ratio": sharpe,
                "Max_Drawdown": max_dd
            },
            "report": report_normal
        }
