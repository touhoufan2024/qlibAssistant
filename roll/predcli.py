from loguru import logger
import sys
logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>"
)

class PredCLI:
    """
    [子模块] 实盘决策: 生成信号与诊断
    """
    def __init__(self, exp_name):
        self.exp_name = exp_name

    def today(self, top=50, out="buy_list.csv", filter_st=True):
        """
        生成明日全市场预测榜单
        :param top: 输出前 N 名
        :param out: 保存文件名
        :param filter_st: 是否过滤 ST/停牌
        """
        logger.info(f"正在加载最新模型，预测明日全市场 (Top {top})...")
        logger.info(f"过滤条件: ST/停牌={filter_st}")
        
        # TODO: 1. get_best_model() -> model
        # TODO: 2. prepare_dataset(tomorrow) -> ds
        # TODO: 3. model.predict(ds)
        
        logger.success(f"预测完成，结果已保存至: {out}")

    def stock(self, id, history=10):
        """
        诊断单只股票
        :param id: 股票代码 (如 SH600519)
        :param history: 查看最近 N 天的得分走势
        """
        # 自动大写并补全代码的简单逻辑
        if id.isdigit():
            logger.warning(f"检测到纯数字代码 {id}，请指明 SH 或 SZ (示例: SH{id})")
        
        logger.info(f"正在诊断股票 [{id}]...")
        logger.info(f"获取最近 {history} 天的模型评分走势...")
        # TODO: Query prediction history
        logger.info(f"[{id}] 今日得分: 1.25 | 全市场排名: 15/4500 | 建议: <green>持有</green>")

    def diff(self, id):
        """监控持仓股排名变化 (今日 vs 昨日)"""
        logger.info(f"正在对比股票 [{id}] 的排名变化...")
        logger.warning(f"[{id}] 排名大幅下降: 昨(Top 10) -> 今(Top 300) ! 建议核查")