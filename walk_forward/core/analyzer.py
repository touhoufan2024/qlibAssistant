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

        # 1. 加载预测数据并标准化
        df_pred = pd.read_csv(prediction_file, parse_dates=['datetime'])
        df_pred['instrument'] = df_pred['instrument'].astype(str).str.upper() # 统一大写用于 IC 计算
        df_pred = df_pred.set_index(['datetime', 'instrument'])
        
        start_date = df_pred.index.get_level_values('datetime').min()
        end_date = df_pred.index.get_level_values('datetime').max()

        # 2. 获取真实行情并标准化
        logger.info(f"正在获取真实行情用于 IC 计算 (区间: {start_date} ~ {end_date})...")
        df_label = D.features(D.instruments(stock_pool), ['Ref($close, -2) / Ref($close, -1) - 1'], 
                             start_time=start_date, end_time=end_date, freq='day')
        df_label.columns = ['label']
        # 强制将行情数据的代码也转为大写，确保能与预测数据对齐
        df_label = df_label.reset_index()
        df_label['instrument'] = df_label['instrument'].astype(str).str.upper()
        df_label = df_label.set_index(['datetime', 'instrument'])

        # 3. 合并数据并计算指标
        df_combined = df_pred.merge(df_label, left_index=True, right_index=True, how='inner').dropna()
        logger.info(f"数据合并完成，有效样本数: {len(df_combined)}")
        
        if len(df_combined) == 0:
            logger.error("IC 计算失败：预测数据与行情数据没有重叠（请检查股票代码格式和日期范围）")
            return {"error": "No overlapping data between predictions and labels."}

        daily_ic = df_combined.groupby('datetime').apply(lambda g: g['score'].corr(g['label']), include_groups=False)
        daily_ric = df_combined.groupby('datetime').apply(lambda g: g['score'].corr(g['label'], method='spearman'), include_groups=False)

        # 4. 理论模拟回测 (Theoretical: 无成本、无限制)
        def calc_theoretical_ret(group):
            return group.nlargest(30, 'score')['label'].mean()
        theo_daily_ret_raw = df_combined.groupby('datetime').apply(calc_theoretical_ret, include_groups=False).dropna()
        
        # --- 时间轴对齐修正 (Alignment Fix) ---
        # 信号在 T 日产生，收益在 T+1 建立仓位并在 T+2 结束时实现。
        # 理论收益 theo_daily_ret_raw[T] 对应的是 T+1 到 T+2 的涨幅。
        # 为了与 Qlib 的 account 报告（结算日索引）对齐，我们需要将理论收益的日期向后平移 2 个交易日。
        trade_calendar = D.calendar(start_time=start_date, end_time=D.calendar()[-1])
        date_map = {trade_calendar[i]: trade_calendar[i+2] for i in range(len(trade_calendar)-2)}
        
        theo_daily_ret = theo_daily_ret_raw.copy()
        theo_daily_ret.index = theo_daily_ret.index.map(date_map)
        theo_daily_ret = theo_daily_ret.dropna()
        
        theo_cum_ret = (1 + theo_daily_ret).cumprod()

        # 5. Qlib 官方实盘模拟回测 (Realistic)
        logger.info("启动 Qlib 官方回测模块 (A股实盘规则)...")
        # 信号需要与 D.features 保持一致使用大写
        strategy = TopkDropoutStrategy(topk=30, n_drop=5, signal=df_pred)
        
        exchange_kwargs = {
            "freq": "day",
            "limit_threshold": 0.1,
            "deal_price": "close",
            "open_cost": 0.0005,
            "close_cost": 0.0015,
            "min_cost": 5,
        }
        # 关键修复：必须开启 generate_portfolio_metrics=True 才能返回真实的持仓和资金流水
        executor = SimulatorExecutor(time_per_step="day", exchange_kwargs=exchange_kwargs, generate_portfolio_metrics=True)
        
        res = qlib_backtest(
            strategy=strategy, 
            executor=executor,
            start_time=start_date.strftime("%Y-%m-%d"),
            end_time=end_date.strftime("%Y-%m-%d"),
            account=100000000,
            benchmark="SH000300",
        )
        
        # 解析回测报告：res 是 (portfolio_dict, indicator_dict)
        real_report = pd.DataFrame()
        if isinstance(res, tuple) and len(res) > 0:
            portfolio_dict = res[0]
            if isinstance(portfolio_dict, dict) and '1day' in portfolio_dict:
                # portfolio_dict['1day'] 是一个元组，第一个元素是 account dataframe
                real_report = portfolio_dict['1day'][0]
        
        # 指标汇总
        ric_values = daily_ric.values
        ric_mean_val = float(np.nanmean(ric_values)) if len(ric_values) > 0 else 0
        ric_std_val = float(np.nanstd(ric_values)) if len(ric_values) > 0 else 0
        
        results = {
            "ic_stats": {
                "Test_RankIC": ric_mean_val,
                "Test_RankICIR": (ric_mean_val / ric_std_val) if ric_std_val > 0 else 0,
            },
            "theoretical_performance": {
                "Total_Return %": float((theo_cum_ret.iloc[-1] - 1) * 100) if not theo_cum_ret.empty else 0,
                "Max_Drawdown %": float((theo_cum_ret / theo_cum_ret.cummax() - 1).min() * 100) if not theo_cum_ret.empty else 0,
            },
            "realistic_performance": {}
        }

        if isinstance(real_report, pd.DataFrame) and not real_report.empty:
            # account 列代表每日扣除手续费和考虑涨跌停后的真实账户净资产
            if 'account' in real_report.columns:
                real_equity = real_report['account'] / 100000000.0  # 归一化为净值
                s_ret = real_equity.pct_change().fillna(0)
            else:
                s_ret = real_report.iloc[:, 0].pct_change().fillna(0)
                real_equity = (1 + s_ret).cumprod()
            
            results["realistic_performance"] = {
                "Total_Return %": float((real_equity.iloc[-1] - 1) * 100),
                "Max_Drawdown %": float((real_equity / real_equity.cummax() - 1).min() * 100),
                "Sharpe_Ratio": float(s_ret.mean() / s_ret.std() * np.sqrt(250)) if s_ret.std() != 0 else 0
            }
        else:
            real_equity = pd.Series(dtype=float)
            results["realistic_performance"] = {"Note": "Qlib Backtest Empty (Check Data/Thresholds)"}

        # 附加上时间序列数据供画图使用
        results["series"] = {
            "daily_ric": daily_ric,
            "theo_equity": theo_cum_ret,
            "real_equity": real_equity
        }

        return results
