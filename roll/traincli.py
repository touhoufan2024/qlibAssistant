
from loguru import logger
import sys
logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>"
)

class TrainCLI:
    """
    [子模块] 训练引擎: 负责滚动训练 (Rolling)
    """
    def __init__(self, exp_name, **kwargs):
        self.exp_name = exp_name

    def init(self, model="LGB", step=20):
        """
        [警告] 初始化并全量重新训练
        :param model: 模型配置文件名 (如 LGB, XGB)
        :param step: 滚动步长
        """
        logger.warning(f"!!! 准备重置实验 [{self.exp_name}] 并全量训练 !!!")
        logger.info(f"模型配置: {model} | 滚动步长: {step}")
        # TODO: inst = RollingTaskExample(experiment_name=self.exp_name, ...)
        # TODO: inst.reset()
        # TODO: inst.run()

    def update(self, step=20):
        """
        [核心] 增量滚动训练: 仅训练新产生的时间段
        """
        logger.info(f"检查实验 [{self.exp_name}] 是否需要增量训练...")
        # TODO: 比较 R.list_recorders 的 max(test_end_date) 与 数据最新日期
        need_train = True # 模拟判断
        if need_train:
            logger.info("发现新数据，开始训练新的滚动子模型...")
            # TODO: inst = RollingTaskExample(...)
            # TODO: inst.task_training(...)
            logger.success("增量训练完成")
        else:
            logger.info("当前模型已是最新的，无需训练。")

    def repair(self, rid):
        """修复特定 Recorder ID 的训练"""
        logger.info(f"正在修复/重跑 Recorder ID: [{rid}]...")