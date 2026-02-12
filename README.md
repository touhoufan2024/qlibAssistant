
[!IMPORTANT] 项目声明：本项目初衷为作者自用的量化脚本，目前正处于从“个人工具”向“开源项目”过渡的完善与规范阶段。

🚀 先看结果：如果你想直接查看工具的实战表现，可以访问由 GitHub Action 每日自动生成的预测报告： 👉 查看每日预测结果预览
https://touhoufan2024.github.io/qlibAssistant/

[!WARNING] 风险提示：量化模型预测仅供参考，不构成任何投资建议。股市有风险，入市需谨慎。

---

# QlibAssistant

**QlibAssistant** 是一个基于微软开源量化框架 [Qlib](https://github.com/microsoft/qlib) 构建的辅助工具。它旨在解决 Qlib 使用门槛高、需要大量编写样板代码的问题，让你能够通过简单的命令行操作，实现 A 股量化模型的**数据准备、模型训练、自动预测与模型管理**。

本项目最初为个人实盘脚本，现已开源，并支持通过 GitHub Actions 实现每日自动预测。

---

## 🌟 核心特性

* **开箱即用**：无需编写复杂的 Python 脚本，通过命令行（基于 `fire` 库）即可完成全流程。
* **一键训练**：支持多策略（XGBoost, LightGBM, DoubleEnsemble 等）与多因子（Alpha158）的组合训练。
* **模型管理**：内置 8 组经过筛选的高性能模型，支持对历史任意日期进行“回测式”预测。
* **多维度滚动**：支持 `Sliding`（滑动窗口）和 `Expanding`（扩展窗口）两种训练模式。
* **每日自动预测**：配合 GitHub Action，可实现每日收盘后自动更新数据并生成预测报告。

---

## 🛠️ 功能模块

### 1. 数据管理 (`data`)

虽然内置了数据同步接口，但由于依赖特定的 Dolt 仓库，推荐使用社区维护的数据包。

* **推荐方案**：从 [investment_data](https://github.com/chenditc/investment_data.git) 下载 `qlib_bin.tar.gz`。

### 2. 模型训练 (`train`)

支持高度自由的参数配置，可批量生产不同组合的模型。

* **支持模型**：`XGBoost`, `Linear`, `DoubleEnsemble`, `LightGBM`
* **支持因子**：`Alpha158` (主要针对 GBDT 类模型优化)
* **支持池子**：`csi300` (沪深300) 等。

### 3. 模型预测与管理 (`model`)

* **筛选机制**：从训练池中筛选表现优异的模型。
* **多模型集成**：预测时采用多模型 Score 简单平均法，提高预测稳健性。
* **历史回溯**：支持传入特定日期范围进行历史预测验证。

---

## 🚀 快速上手

### 第一步：准备数据

```bash
# 下载并解压 Qlib 格式的 A 股数据
mkdir -p ~/.qlib/qlib_data/cn_data
tar -zxvf qlib_bin.tar.gz -C ~/.qlib/qlib_data/cn_data --strip-components=1

```

### 第二步：路径配置 (重要)

> [!CAUTION]
> 由于 Qlib 底层 `mlruns` 记录了绝对路径，目前本项目强制要求路径为：
> `/home/ash/.qlibAssistant/mlruns/`
> 请确保在该路径下操作，或通过软链接 `ln -s` 进行映射。

### 第三步：模型训练

```bash
# 训练一个基于 Alpha158 因子、沪深300、滑动窗口的 XGBoost 模型
python ./roll/roll.py --model_names="XGBoost" --dataset_names="Alpha158" --stock_pools="csi300" --rolling_types="sliding"

```

### 第四步：模型预测

```bash
# 1. 自动预测最新一天 (根据本地数据更新情况)
python ./roll/roll.py model selection

# 2. 预测指定日期范围 (用于简单回测)
python ./roll/roll.py model selection --predict_dates='[{"start": "2026-02-02", "end": "2026-02-03"}]'

```

---

## 📊 逻辑说明

### 预测目标 (Label)

我们采用了 Qlib 的默认定义：


* **含义**：基于 T 日收盘数据，预测 **T+1 日收盘买入** 到 **T+2 日收盘卖出** 的期望收益率。
* **实操建议**：预测结果仅供参考。实盘时建议 T+1 日寻找相对低点介入。

### 8 种模型组合参考

本项目预设并训练了以下维度的组合：

* **算法**: XGBoost, Linear, DoubleEnsemble, LightGBM
* **特征**: Alpha158
* **窗口**: Sliding, Expanding

---

## 📅 自动化部署

本项目已集成 **GitHub Action**。它会：

1. 自动拉取最新的 A 股数据。
2. 调用 `model selection` 进行每日预测。
3. 将预测结果（Score 排名）输出到 `analysis_folder` 目录。

---

## ⚠️ 注意事项

* **涨跌幅限制**：Qlib 的模型预测基于数学期望，未考虑 A 股 10% 的涨跌停板机制，Score 可能会出现超过 0.1 的情况。
* **环境依赖**：目前 `Alpha158` 模型主要在 WSL2 环境下训练，无需 GPU，使用 CPU 即可运行。

---

## 🤝 贡献与反馈

如果你有更好的因子建议或者模型优化方案，欢迎提交 Issue 或 Pull Request！

---

### 💡 润色建议说明：

1. **路径警告**：你提到的路径写死问题是新用户最大的坑，我用 `[!CAUTION]` 高亮标注了。
2. **公式渲染**：使用 LaTeX 渲染了 Label 的公式，显得更专业。
3. **对比表格**：原稿中 Alpha158 的对比很不错，但在 README 中如果太长可以简化。我将其核心逻辑融入了“功能模块”中。
4. **操作指引**：将复杂的描述转化为具体的“第一步、第二步”，降低用户认知负担。

**接下来，你想让我帮你生成一个符合上述路径要求的 `setup.sh` 自动配置脚本吗？**