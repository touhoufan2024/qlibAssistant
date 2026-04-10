# QlibAssistant 项目上下文 (Project Context)

`qlibAssistant` 是一个专为沪深 300 (CSI300) 指数选股设计的自动化量化投资平台。它基于微软的 **Qlib** 框架构建，提供了从数据获取、模型训练到预测生成及性能复盘的完整流水线。

## 🚀 项目概览

- **核心目标**：基于机器学习模型集成，每日生成沪深 300 选股清单。
- **主要技术栈**：Python, Microsoft Qlib, XGBoost, LightGBM, CatBoost, DoubleEnsemble, VitePress (用于文档和仪表盘)。
- **系统架构**：
    - **数据层**：通过 AkShare 自动从 `chenditc/investment_data` 同步每日 A 股数据。
    - **模型层**：对 20 多个模型进行滚动训练（包含 5 种算法 × 5 种回溯周期）。
    - **集成层**：根据 IC/ICIR 等指标筛选表现优异的模型，并进行简单平均加权集成。
    - **复盘层**：“马后炮”分析模块，用于验证历史预测的准确性。
    - **展示层**：通过 VitePress 自动生成网页并部署至 GitHub Pages。
- **跨平台兼容**：需要兼容linux和windows双环境，在执行命令和写代码时，需要考虑跨平台的兼容性。

## 📂 核心目录结构

- `roll/`：**核心引擎**。包含数据维护、训练和模型逻辑的主要 CLI。
    - `roll.py`：所有操作的主入口。
    - `config.yaml`：全局配置（路径、训练参数等）。
    - `traincli.py`：滚动训练逻辑（使用进程隔离以防止内存泄漏）。
    - `modelcli.py`：模型推理、筛选及集成逻辑。
    - `model_review.py`：性能评估与“马后炮”分析。
    - `GEMINI.md`：模块特定的架构细节与规范。
- `script/`：自动化与工具脚本。
    - `run.py`：批量实验运行脚本，涵盖所有模型组合。
- `page/`：基于 VitePress 的仪表盘与文档。
- `tests/`：核心组件的 Pytest 测试套件。
- `model_pkl/`：压缩后的模型产物存储位 (`mlruns`)。
- `backtest_csv/`, `qlib_score_csv/`, `review_csv/`：结果文件、日志与复盘数据的输出目录。

## 项目详细说明

### 模型集成方案 (Ensemble Strategy)

- **基础算法**：XGBoost、LightGBM、DoubleEnsemble、Linear
- **训练窗口**：滚动回溯过去 1～5 年历史数据，共得到 20 个模型
- **模型筛选**：按 IC、ICIR、Rank IC、Rank ICIR 等指标筛选表现较好的模型
- **聚合方式**：对通过筛选的模型预测分（Score）取**简单平均**

### 功能模块

| 模块 | 说明 |
|------|------|
| 数据管理 (`data`) | 从 [chenditc/investment_data](https://github.com/chenditc/investment_data) 同步最新 A 股日线数据 |
| 模型训练 (`train`) | 支持断点续训，自动管理模型实验 |
| 模型预测 (`model`) | 筛选最优模型并执行推理，输出 `xxx_ret`、`xxx_filter_ret` 等汇总表 |

### 完整本地运行步骤

**第一步：更新每日数据**

```bash
cd ./roll && python ./roll.py data update

**第二步：模型训练**

```bash
# 滚动训练 LightGBM 模型
cd ./roll && python ./roll.py --pfx_name="EXP" --model_name="LightGBM" --dataset_name="Alpha158" --stock_pool="csi300" --rolling_type="custom" train start_custom

# 使用 CI 同款方式训练 20 个模型（1～5 年周期）
cd ./roll && python ../script/run.py

# 或直接解压仓库自带的最新模型（每日更新）到 ~/.qlibAssistant/mlruns
cd ./roll && python roll.py model decompress_mlruns
```

**第三步：生成预测**

```bash
cd ./roll && python ./roll.py model selection
```

### 预测逻辑说明

- **目标 (Label)**：基于 T 日收盘数据，预测「T+1 日收盘买入、T+2 日收盘卖出」的期望收益率（理论值，未考虑 A 股 10% 涨跌停限制）
- **下载最新模型**：📦 [GitHub Releases](https://github.com/touhoufan2024/qlibAssistant/releases)


### 测试与开发
- `pytest` - 运行测试套件。
- `cd page && npm run docs:dev` - 启动本地文档/仪表盘预览服务器。

## 📏 开发规范

- **进程隔离**：所有模型训练必须在独立的子进程中执行，以规避 Qlib/PyTorch 的内存占用问题。
- **延迟初始化**：仅在需要时（如执行 `train` 或 `model` 子命令）初始化 Qlib，以保持 CLI 的响应速度。
- **路径处理**：始终使用 `pathlib.Path` 以确保 Windows 和 Linux 环境下的跨平台兼容性。
- **MLflow 迁移**：在不同环境间移动 `mlruns` 文件夹后，需运行 `utils.fix_mlflow_paths` 修复路径。
- **配置优先级**：命令行参数 > `config.yaml` > 默认值。
- **代码风格**：新增 CLI 命令应遵循 `roll/` 目录下的既有模式，并保持类型注解 (Type Hinting)。

