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
        qlib.init(**self.qlib_config)

    def get_training_metrics(self) -> pd.DataFrame:
        """提取训练阶段指标"""
        rows = []
        from qlib.workflow import R
        for event in self.history:
            date = event["retrain_date"]
            for task_name, rid in event["tasks"].items():
                try:
                    exp_name = f"WF_{task_name}"
                    exp = R.get_exp(experiment_name=exp_name)
                    rec = exp.get_recorder(recorder_id=rid)
                    ic_pkl = rec.load_object("sig_analysis/ic.pkl")
                    rows.append({"RetrainDate": date, "Task": task_name, "Train_IC": ic_pkl.mean(), "Train_RankIC": ic_pkl.mean()})
                except:
                    rows.append({"RetrainDate": date, "Task": task_name, "Note": "Metrics Missing"})
        return pd.DataFrame(rows)

    def analyze_test_performance(self, prediction_file: str, stock_pool: str = "csi300") -> Dict[str, Any]:
        """分析测试集表现，对比理论收益与 Qlib 实盘模拟收益"""
        from qlib.backtest import backtest as qlib_backtest
        from qlib.backtest.executor import SimulatorExecutor
        from qlib.contrib.strategy import TopkDropoutStrategy

        if not Path(prediction_file).exists():
            return {"error": f"预测文件不存在: {prediction_file}"}

        df_pred = pd.read_csv(prediction_file, parse_dates=['datetime']).set_index(['datetime', 'instrument'])
        start_date = df_pred.index.get_level_values('datetime').min()
        end_date = df_pred.index.get_level_values('datetime').max()

        # 1. 计算 IC (标准未来收益)
        logger.info(f"正在获取真实行情用于 IC 计算...")
        df_label = D.features(D.instruments(stock_pool), ['Ref($close, -2) / Ref($close, -1) - 1'], 
                             start_time=start_date, end_time=end_date, freq='day')
        df_label.columns = ['label']
        df_combined = df_pred.merge(df_label, left_index=True, right_index=True, how='inner').dropna()
        daily_ic = df_combined.groupby('datetime').apply(lambda g: g['score'].corr(g['label']), include_groups=False)
        daily_ric = df_combined.groupby('datetime').apply(lambda g: g['score'].corr(g['label'], method='spearman'), include_groups=False)

        # 2. 理论模拟回测 (Theoretical: 无成本、无涨跌停限制)
        logger.info("执行理论等权回测模拟...")
        def calc_theoretical_ret(group):
            return group.nlargest(30, 'score')['label'].mean()
        theo_daily_ret = df_combined.groupby('datetime').apply(calc_theoretical_ret, include_groups=False).dropna()
        theo_cum_ret = (1 + theo_daily_ret).cumprod()

        # 3. Qlib 官方实盘模拟回测 (Realistic: 含成本、含涨跌停限制)
        logger.info("启动 Qlib 官方回测模块 (A股实盘规则)...")
        strategy = TopkDropoutStrategy(topk=30, n_drop=5, signal=df_pred)
        
        # A股标准回测配置
        exchange_kwargs = {
            "freq": "day",
            "limit_threshold": 0.1,    # 10% 涨跌停限制
            "deal_price": "close",     # 收盘价成交
            "open_cost": 0.0005,       # 买入万五
            "close_cost": 0.0015,      # 卖出万十五 (含印花税)
            "min_cost": 5,             # 最低5元
        }
        executor = SimulatorExecutor(time_per_step="day", exchange_kwargs=exchange_kwargs, generate_report=True)
        
        res = qlib_backtest(
            strategy=strategy, 
            executor=executor,
            start_time=start_date.strftime("%Y-%m-%d"),
            end_time=end_date.strftime("%Y-%m-%d"),
            account=100000000,
            benchmark="SH000300",
        )
        
        # 结果解包与清洗
        real_report = pd.DataFrame()
        def find_df(obj):
            if isinstance(obj, pd.DataFrame): return obj
            if isinstance(obj, dict):
                for v in obj.values():
                    r = find_df(v)
                    if r is not None and not r.empty: return r
            if isinstance(obj, (list, tuple)):
                for item in obj:
                    r = find_df(item)
                    if r is not None and not r.empty: return r
            return None
        real_report = find_df(res)

        # 4. 指标汇总
        results = {
            "ic_stats": {
                "Test_RankIC": daily_ric.mean(),
                "Test_RankICIR": daily_ric.mean() / daily_ric.std() if daily_ric.std() != 0 else 0,
            },
            "theoretical_performance": {
                "Total_Return %": (theo_cum_ret.iloc[-1] - 1) * 100 if not theo_cum_ret.empty else 0,
                "Max_Drawdown %": (theo_cum_ret / theo_cum_ret.cummax() - 1).min() * 100 if not theo_cum_ret.empty else 0,
            },
            "realistic_performance": {}
        }

        if real_report is not None and not real_report.empty:
            # 兼容不同列名抓取收益
            ret_col = next((c for c in ['return', 'pa', 'portfolio_return'] if c in real_report.columns), real_report.columns[0])
            if ret_col == 'pa': # 如果是净值，转为收益率
                s_ret = real_report['pa'].pct_change().fillna(0)
            else:
                s_ret = real_report[ret_col]
            
            real_cum_ret = (1 + s_ret).cumprod()
            results["realistic_performance"] = {
                "Total_Return %": (real_cum_ret.iloc[-1] - 1) * 100,
                "Max_Drawdown %": (real_cum_ret / real_cum_ret.cummax() - 1).min() * 100,
                "Sharpe_Ratio": (s_ret.mean() / s_ret.std() * np.sqrt(250)) if s_ret.std() != 0 else 0
            }
        else:
            results["realistic_performance"] = {"Note": "Qlib Backtest Empty (Check Data/Thresholds)"}

        return results
