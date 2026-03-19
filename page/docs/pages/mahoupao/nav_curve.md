# 净值曲线（Lightweight Charts）

该页面使用 `Lightweight Charts` 绘制回测策略净值曲线，并与 `CSI300` 同图对比。  
数据来源为项目根目录的 `backtest_csv/*.csv`，构建时会自动同步到站点的 `/backtest_csv/` 目录。

## 文件约定

- 文件名：`<topN>_<type>.csv`，例如 `10_ret.csv`、`20_filter_ret.csv`
- 关键字段：`date`、`strategy_equity`、`csi300_equity`
- 排序规则：先 `ret`，后 `filter_ret`；组内按 `topN` 从小到大

## Top10策略 ret

<NavCurveChart strategy="10_ret" />

## Top20策略 ret

<NavCurveChart strategy="20_ret" />

## Top30策略 ret

<NavCurveChart strategy="30_ret" />

## Top50策略 ret

<NavCurveChart strategy="50_ret" />

## Top80策略 ret

<NavCurveChart strategy="80_ret" />

## Top100策略 ret

<NavCurveChart strategy="100_ret" />

## Top10策略 filter_ret

<NavCurveChart strategy="10_filter_ret" />

## Top20策略 filter_ret

<NavCurveChart strategy="20_filter_ret" />

## Top30策略 filter_ret

<NavCurveChart strategy="30_filter_ret" />

## Top50策略 filter_ret

<NavCurveChart strategy="50_filter_ret" />

## Top80策略 filter_ret

<NavCurveChart strategy="80_filter_ret" />

## Top100策略 filter_ret

<NavCurveChart strategy="100_filter_ret" />

