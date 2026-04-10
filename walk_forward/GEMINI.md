# Walk-Forward 灵活重训与前向回测框架

本模块是一个独立于 `roll/` 的生产级量化执行引擎，旨在实现“定期触发重训、日常高效推理”的流水线，并支持完整的前向步进（Walk-Forward）历史回测与实盘模拟。

## 🎯 核心架构与设计原则

1. **逻辑独立性**：模块完全自持，不引用 `roll/` 目录下的业务逻辑，确保研究与生产环境的清晰边界。
2. **前向步进 (Walk-Forward)**：
   - 模拟真实交易周期：`[历史重训 (Ti) -> 期间预测 (Ti ~ Ti+1) -> 到点再次重训 (Ti+1)]`。
   - **严谨性**：训练数据止于 $T_i - 3$ 交易日，确保 Alpha158 等需要未来信息的标签在训练时已完全实现，杜绝未来函数。
3. **多进程隔离 (Process Isolation)**：
   - **训练与推理**：所有 Qlib 核心操作均在独立子进程中执行。
   - **安全性**：任务结束通过 `os._exit(0)` 强制回收资源，彻底解决 Qlib/PyTorch 的内存占用不释放问题，并规避 Windows 下的导入死锁。
4. **状态持久化与校验 (Self-Healing)**：
   - `wf_state.json` 记录所有成功的重训事件（日期与对应的 MLflow `run_id`）。
   - **一致性检查**：启动时校验磁盘产物是否存在，自动清理失效记录并触发重训。

## 📂 核心组件说明

- **`wf_cli.py`**: 任务总调度器。管理步进循环，负责训练任务派发、推理结果收集及性能指标汇总。
- **`core/task_builder.py`**: 任务工厂。将 YAML 配置转化为 Qlib 任务字典。优化点：固定 Handler 的 `start_time` 以命中 `roll` 模块预生成的磁盘缓存。
- **`core/train.py` & `core/predict.py`**: 子进程执行器。封装了 `multiprocessing` 逻辑，确保主进程环境纯净。
- **`core/state.py`**: 状态管理器。负责 `wf_state.json` 的维护与 MLflow 产物映射。
- **`utils/calendar.py`**: 交易日历工具。基于 `qlib_data` 提供的交易日序列，实现精确的日期偏移、月度对齐及重训点生成。
- **`core/analyzer.py`**: 性能复盘专家。计算 RankIC、Top-K 胜率，并支持 Qlib 官方的实盘模拟回测（含手续费与涨跌停限制）。

## ⚙️ 配置规范 (`walk_forward_config.yaml`)

- **Trigger**: 支持按 `trading_days` 或 `months` 触发重训。
- **Tasks**: 支持多尺度任务配置，可定义不同模型（LGBM/XGB/Linear）、不同回溯长度（Lookback）及切分比例。

## 🚀 常用指令

```powershell
# 执行完整的回测或实盘增量预测
python -m walk_forward.wf_cli run

# 分析最新预测结果并生成可视化图表
python -m walk_forward.wf_cli analyze
```

## ⚠️ 开发注意事项

- **严禁直接导入 qlib**：除子进程内部外，避免在主模块顶层导入 `qlib`，以维持 CLI 启动速度及进程隔离效果。
- **路径处理**：必须使用 `pathlib.Path` 并通过 `.expanduser()` 处理 `~` 路径，确保跨平台一致性。
- **结果落盘**：预测结果统一存放在 `walk_forward_output/` 下，文件命名包含起始日期以便追溯。
