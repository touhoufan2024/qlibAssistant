import pandas as pd
import qlib
from qlib.backtest import backtest as qlib_backtest
from qlib.backtest.executor import SimulatorExecutor
from qlib.contrib.strategy import TopkDropoutStrategy

if __name__ == '__main__':
    qlib.init(provider_uri='C:/Users/mahq/.qlib/qlib_data/cn_data')

    df_pred = pd.read_csv('./walk_forward_output/wf_predictions_2026-01-01_2026-03-27.csv', parse_dates=['datetime'])
    df_pred['instrument'] = df_pred['instrument'].str.upper()
    df_pred = df_pred.set_index(['datetime', 'instrument'])

    start_date = df_pred.index.get_level_values('datetime').min().strftime('%Y-%m-%d')
    end_date = df_pred.index.get_level_values('datetime').max().strftime('%Y-%m-%d')

    strategy = TopkDropoutStrategy(topk=30, n_drop=5, signal=df_pred)
    exchange_kwargs = {
        "freq": "day",
        "limit_threshold": 0.1,
        "deal_price": "close",
        "open_cost": 0.0005,
        "close_cost": 0.0015,
        "min_cost": 5,
    }
    executor = SimulatorExecutor(time_per_step="day", exchange_kwargs=exchange_kwargs, generate_portfolio_metrics=True)
    
    print("Running backtest...")
    res = qlib_backtest(
        strategy=strategy, 
        executor=executor,
        start_time=start_date,
        end_time=end_date,
        account=100000000,
        benchmark="SH000300",
    )
    
    print(f"Type of res: {type(res)}")
    if isinstance(res, tuple):
        print(f"Length of tuple: {len(res)}")
        for i, item in enumerate(res):
            print(f"Item {i} type: {type(item)}")
            if isinstance(item, pd.DataFrame):
                print(f"Item {i} columns: {item.columns.tolist()}")
                print(item.head(2))
            elif isinstance(item, dict):
                print(f"Item {i} is a dict with keys: {item.keys()}")
                for k, v in item.items():
                    print(f"  Key '{k}' type: {type(v)}")
                    if isinstance(v, pd.DataFrame):
                        print(f"  Key '{k}' columns: {v.columns.tolist()}")
                        print(v.head(2))
                    elif isinstance(v, tuple):
                        for j, t_item in enumerate(v):
                            print(f"    Tuple item {j} type: {type(t_item)}")
                            if isinstance(t_item, pd.DataFrame):
                                print(f"    Tuple item {j} columns: {t_item.columns.tolist()}")
                                print(t_item.head(2))
