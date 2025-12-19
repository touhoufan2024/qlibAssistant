from loguru import logger
import sys
logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>"
)

class CollectCLI:
    """
    [子模块] 统计
    """
    def __init__(self, exp_name):
        self.exp_name = exp_name

    def tdx(self, top=30, path="C:/new_qlib.blk"):
        """导出通达信板块文件"""
        logger.info(f"正在将 Top {top} 股票导出为通达信板块...")
        logger.success(f"导出成功: {path}")

    def report(self, format="html"):
        """生成每日日报"""
        logger.info(f"正在生成 {format} 格式的交易日报...")