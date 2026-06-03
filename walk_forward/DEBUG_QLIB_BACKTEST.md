# Qlib SimulatorExecutor 实盘回测 Debug 经验记录

**日期**: 2026-04-07
**模块**: `walk_forward/core/analyzer.py`
**问题描述**: 
在使用 Qlib 的 `SimulatorExecutor` 进行实盘模拟回测时，模型具有正向的 IC 预测能力，但回测生成的收益率、最大回撤等指标全部为 0。

## 排查过程与避坑指南

### 1. 现象分析
在执行 `qlib_backtest` 后，返回的结果中没有产生任何交易，每日持仓始终为空（或者资金净值毫无波动）。
起初怀疑是本地行情数据缺失（例如缺少 `$vwap` 或 `$factor` 字段）导致无法撮合成交。

### 2. 核心大坑一：缺失 `generate_portfolio_metrics` 参数
**问题**: 
Qlib 较新版本的 `SimulatorExecutor` 出于性能考虑，默认**不生成**详细的账户流水指标字典。如果不显式开启，回测结束后尝试从返回值 `res[0]` (即 `portfolio_dict`) 中提取每日账户净值 (`account` 列) 时，会得到一个空字典或无法提取到有效的 DataFrame。

**解决方案**:
在初始化 `SimulatorExecutor` 时，必须显式传入 `generate_portfolio_metrics=True`：
```python
executor = SimulatorExecutor(
    time_per_step="day", 
    exchange_kwargs=exchange_kwargs, 
    generate_portfolio_metrics=True  # 关键修复点
)
```

### 3. 核心大坑二：被文件系统误导的大小写对齐
**问题**: 
观察本地 Qlib 数据库目录 `~/.qlib/qlib_data/cn_data/features` 时，发现所有股票文件夹均是小写格式（如 `sh600000`）。这容易让人误以为在构造 `TopkDropoutStrategy` 的 `signal` DataFrame 时，也必须将 index 里的 `instrument` 转换为小写。
**真相是**：Qlib 在内部构建 `Exchange` 和 `TradeCalendar` 时，**强制要求传入大写的股票代码**（如 `SH600000`）。如果传入小写信号，撮合引擎在校验可交易标的时会认为“该股票不在可用列表中”，从而直接拒绝所有订单。这就是导致每日交易额为 0 的根本原因。

**解决方案**:
确保预测数据 DataFrame (`df_pred`) 在传入回测引擎前，其 `instrument` 索引层级被统一转换为**大写**：
```python
# 确保信号数据为大写，匹配 Qlib 内部 Exchange 的校验标准
df_pred.index = df_pred.index.set_levels(df_pred.index.levels[1].astype(str).str.upper(), level=1)
strategy = TopkDropoutStrategy(topk=30, n_drop=5, signal=df_pred)
```

## 最终正确的解析提取范式

结合上述两点修复后，可以稳定地从 `qlib_backtest` 中提取出真实的每日账户净资产，并计算累计净值（Equity）、最大回撤和夏普比率：

```python
res = qlib_backtest(
    strategy=strategy, 
    executor=executor,
    start_time=start_date,
    end_time=end_date,
    account=100000000,
    benchmark="SH000300",
)

# res 是一个 Tuple: (portfolio_dict, indicator_dict)
if isinstance(res, tuple) and len(res) > 0:
    portfolio_dict = res[0]
    if isinstance(portfolio_dict, dict) and '1day' in portfolio_dict:
        # portfolio_dict['1day'] 也是一个 Tuple，第一个元素才是包含 account 的 DataFrame
        real_report = portfolio_dict['1day'][0]
        
        # 提取每日真实账户净资产 (扣除手续费、滑点并考虑涨跌停后的结果)
        real_equity = real_report['account'] / 100000000.0  # 归一化为净值曲线
        s_ret = real_equity.pct_change().fillna(0)
```

## 总结
**不要盲目替换 Qlib 的原生引擎。** 原生引擎包含了极其严苛和真实的 A 股交易规则（如 10% 涨跌停限制拦截）。当遇到回测无结果时，优先通过打印底层返回的数据结构（字典的 keys 和 tuple 的层级）来定位问题，同时严守大写股票代码规范。