# roll 模块架构与规范 (Qlib 滚动训练引擎)

该模块是基于 **Qlib** 构建的自动化量化研究与交易闭环工具集，核心目标是通过 CLI 实现从数据维护到策略回测的全流程自动化。

## 1. 核心架构设计

### 1.1 入口与调度层
- **`roll.py` (RollingTrader)**: 系统的总调度中心。
  - **延迟加载 (Lazy Init)**: 仅在调用子命令时初始化 `qlib`，避免不必要的环境开销。
  - **配置优先级**: 命令行参数 > `config.yaml`。
- **`config.yaml`**: 定义全局路径（`uri_folder`, `provider_uri`）、实验命名规范及默认训练参数。

### 1.2 数据管理层 (Data & Utils)
- **`datacli.py`**: 封装数据更新逻辑。通过 `akshare` 校验本地与远程交易日差异。
- **`utils.py`**: 提供跨平台兼容性工具。
  - **关键工具**: `fix_mlflow_paths` 用于修复因环境迁移（如 Windows/Linux 切换）导致的 MLflow 配置文件中 `artifact_location` 路径失效问题。
  - **标准化**: 统一 A 股代码前缀（SH/SZ/BJ）。

### 1.3 滚动训练层 (Train Engine)
- **`traincli.py`**: 核心训练逻辑。
  - **多进程隔离**: 使用 `multiprocessing` 启动子进程训练模型，任务结束即销毁，彻底解决 Qlib/PyTorch 的内存泄露问题。
  - **任务生成**: 支持 `expanding`（扩张）和 `sliding`（滑动）两种窗口模式。
- **`myconfig.py`**: 集中管理各模型的超参数模板（CatBoost, LightGBM, XGBoost 等）。

### 1.4 模型复盘与管理层 (Model & Review)
- **`modelcli.py`**: 实验记录管理。支持基于 IC/ICIR 指标的 Recorder 自动筛选。
- **`model_review.py`**: “马后炮”复盘逻辑。计算预测分数的 Top-K 胜率、持仓收益及换手率。
- **`model_backup.py`**: 实验快照工具。支持 `mlruns` 文件夹的打包备份与跨机迁移。

## 2. 关键业务流程
1. **Data Update**: `roll.py data update` (同步最新日频数据)。
2. **Rolling Train**: `roll.py train start` (按 `step` 生成滚动区间并训练)。
3. **Model Selection**: `roll.py model selection` (加载历史 Recorder，集成预测并输出股票评分)。
4. **Post-Review**: `roll.py model review` (对比真实收益，生成复盘报告)。
5. **Backtest**: `roll.py model backtest` (模拟交易，输出净值曲线数据)。

## 3. 开发规范与约束
- **严禁直接在主进程训练**: 所有涉及模型训练的逻辑必须封装在子进程中。
- **路径处理**: 必须使用 `pathlib.Path` 处理路径，确保 Windows 与 Linux 开发环境的无缝切换。
- **依赖管理**: 新模型超参数应在 `myconfig.py` 中定义，严禁在 `traincli.py` 中硬编码。
- **资源清理**: 复盘生成的临时 CSV 建议统一存放于根目录下的 `qlib_score_csv` 或 `review_csv`。
