from loguru import logger
import sys
logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>"
)

class ModelCLI:
    """
    [子模块] 模型仓库: 管理历史模型切片
    """
    def __init__(self, exp_name):
        self.exp_name = exp_name

    def ls(self, limit=10, sort="date"):
        """
        列出所有子模型
        :param limit: 显示数量
        :param sort: 排序方式 (date/metric)
        """
        logger.info(f"列出实验 [{self.exp_name}] 的模型清单 (Top {limit})...")
        # TODO: R.list_recorders(self.exp_name)
        # print table...
        logger.info("ID: 12345 | Test: 2023-01~02 | IC: 0.051 (模拟数据)")
        logger.info("ID: 67890 | Test: 2023-02~03 | IC: 0.048 (模拟数据)")

    def best(self, window=3, metric="IC"):
        """获取当前表现最好的模型"""
        logger.info(f"正在根据最近 {window} 个周期的 {metric} 指标筛选最佳模型...")
        # TODO: 计算 avg(metric)
        best_rid = "abcde12345"
        logger.success(f"推荐最佳模型 ID: <green>{best_rid}</green>")

    def prune(self, keep=50):
        """清理过期的旧模型文件"""
        logger.warning(f"正在清理旧模型，仅保留最近 {keep} 个...")