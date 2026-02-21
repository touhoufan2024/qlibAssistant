
# IMPORTANT
项目声明：本项目初衷为作者自用的量化脚本，目前正处于从“个人工具”向“开源项目”过渡的完善与规范阶段。

🚀 先看结果：如果你想直接查看工具的实战表现，可以访问由 GitHub Action 每日自动生成的预测报告： 👉 查看每日预测结果预览
https://touhoufan2024.github.io/qlibAssistant/

风险提示：量化模型预测仅供参考，不构成任何投资建议。股市有风险，入市需谨慎。

---

# QlibAssistant

**QlibAssistant** 是一个基于微软开源量化框架 [Qlib](https://github.com/microsoft/qlib) 构建的辅助工具。它旨在解决 Qlib 使用门槛高、需要大量编写样板代码的问题，让你能够通过简单的命令行操作，实现 A 股量化模型的**数据准备、模型训练、自动预测与模型管理**。

本项目最初为个人实盘脚本，现已开源，并支持通过 GitHub Actions 实现每日自动预测。

---

## 🌟 核心特性

* **开箱即用**：无需编写复杂的 Python 脚本，通过命令行（基于 `fire` 库）即可完成数据获取、模型训练、模型预测等全流程。
* **一键训练**：支持多模型(qlib自带), 多因子（Alpha158/Alpha360）多股票池的组合训练。
* **每日自动预测**：配合 GitHub Action，可实现每日收盘后自动更新数据并生成预测报告。

---

## 🛠️ 功能模块
分为了三大模块

### 1. 数据管理 (`data`)


从 [investment_data](https://github.com/chenditc/investment_data.git) 下载 `qlib_bin.tar.gz` 打包好的数据

> 目前这个仓库打包的速度较慢, 可能更新不及时, 后续会想办法解决这个问题, 如提供手动在本地打包的方案.


### 2. 模型训练 (`train`)

支持高度自由的参数配置，可批量生产不同组合的模型。

* **支持模型**：`XGBoost`, `Linear`, `DoubleEnsemble`, `LightGBM`
* **支持因子**：`Alpha158`
* **支持池子**：`csi300`

### 3. 模型预测与管理 (`model`)

* **筛选机制**：从训练池中筛选表现优异的模型。
* **多模型集成**：预测时采用多模型 Score 简单平均法，提高预测稳健性。
* **历史回溯**：支持传入特定日期范围进行历史预测验证。

---

## 🚀 快速上手
首先先安装依赖：
```
pip install -r requirements.txt
```

### 第一步：准备数据

```bash
# 下载数据解压到本地
python roll.py data update

# 查看本地数据日期
python roll.py data status
```

### 第二步：模型训练

```bash
# 训练一个基于 Alpha158 因子、沪深300、滑动窗口的 XGBoost 模型
python ./roll.py train start --model_names="XGBoost" --dataset_names="Alpha158" --stock_pools="csi300" --rolling_types="sliding" --step=40
```
> train 支持 断点训练, 一套参数 可能会根据 step 分割出 大量模型, 如果一次没训练完, 因为内存等问题导致挂掉, 只要参数相同, 下次可以继续训练, 不需要重新训练已经完成的模型.

```bash
# 或者 使用 仓库自带的8个模型
tar -zxvf ./model_pkl/qlib_mlruns.tar.gz -C ~
```

### 第三步：模型预测

```bash
# 1. 自动预测最新一天 (根据本地数据更新情况)
python ./roll.py model selection

# 2. 预测指定日期范围 (用于简单回测)
python ./roll.py model selection --predict_dates='[{"start": "2026-02-02", "end": "2026-02-03"}]'

```

---

## 📊 额外说明

### 预测目标 (Label)

我们采用了 Qlib 的默认定义：


* **含义**：基于 T 日收盘数据，预测 **T+1 日收盘买入** 到 **T+2 日收盘卖出** 的期望收益率。
* **实操建议**：预测结果仅供参考。实盘时建议 T+1 日寻找相对低点介入。

### 8 种模型组合参考

本项目预设并训练了以下维度的组合：

* **算法**: XGBoost, Linear, DoubleEnsemble, LightGBM
* **特征**: Alpha158
* **窗口**: Sliding, Expanding
* **股票池**: csi300
* **步长**: 40

alpha158是 技术指标因子集合, 适合使用cpu训练的模型,
alpha360是 原始时序数据集合, 适合使用gpu训练的模型,
本项目暂时仅提供了 alpha158 的模型.

每总组合都会生成多个模型, 根据模型的性能指标为每总组合挑选出了一个模型.

---

## 📅 自动化部署

本项目已集成 **GitHub Action**。它会：

1. 自动拉取最新的 A 股数据。
2. 调用 `model selection` 进行每日预测。
3. 将预测结果（Score 排名）输出到 `analysis_folder` 目录。

---

## ⚠️ 注意事项

* **涨跌幅限制**：Qlib 的模型预测基于数学期望，未考虑 A 股 10% 的涨跌停板机制，Score 可能会出现超过 0.1 的情况。
* **环境依赖**：目前 该项目 仅在WSL2 环境下使用 cpu 训练alpha158类的模型, 未测试其他因子和模型, 如果遇到问题请提 issue.

---

## 🤝 贡献与反馈

如果你有更好的因子建议或者模型优化方案，欢迎提交 Issue 或 Pull Request！

---
