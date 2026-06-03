import pandas as pd
import qlib
from qlib.data import D

qlib.init(provider_uri='C:/Users/mahq/.qlib/qlib_data/cn_data')

df_pred = pd.read_csv('./walk_forward_output/wf_predictions_2026-01-01_2026-03-27.csv', parse_dates=['datetime'])
df_pred['instrument'] = df_pred['instrument'].str.upper()
df_pred = df_pred.set_index(['datetime', 'instrument'])

# 找到第一个有预测数据的日期之后的交易日
dates = df_pred.index.get_level_values('datetime').unique().sort_values()
date = dates[1].strftime('%Y-%m-%d') if len(dates) > 1 else dates[0].strftime('%Y-%m-%d')

top5 = df_pred.xs(dates[0], level='datetime').nlargest(5, 'score').index.tolist()
print(f"Top 5 stocks scored on {dates[0].strftime('%Y-%m-%d')}, expected to trade on {date}: {top5}")

fields = ['$open', '$close', '$high', '$low', '$volume', '$factor', '$vwap']
df_data = D.features(top5, fields, start_time=dates[0].strftime('%Y-%m-%d'), end_time=date)
print("\n--- Qlib Database Features ---")
print(df_data)
