import itertools
import subprocess
import time
from loguru import logger

def run_batch_experiments():
    # 1. 定义参数列表
    model_names = ["XGBoost", "Linear", "DoubleEnsemble", "LightGBM"]
    dataset_names = ["Alpha158", "Alpha360"]
    stock_pools = ["csi300", "csi500"]
    rolling_types = ["sliding", "expanding"]

    # 2. 生成所有组合 (笛卡尔积)
    # 4 * 2 * 2 * 2 = 32 个任务
    combinations = list(itertools.product(model_names, dataset_names, stock_pools, rolling_types))
    
    total_tasks = len(combinations)
    logger.info(f"🚀 总共生成了 {total_tasks} 个组合任务，准备顺序执行...\n")

    # 3. 顺序执行
    for i, (model, dataset, pool, r_type) in enumerate(combinations):
        current_idx = i + 1
        
        # 构造命令字符串
        # 注意: 如果你的 roll.py 需要特定的 python 环境，可以在前面加 "python "
        cmd = (
            f'python ./roll.py '
            f'--pfx_name="EXP" '
            f'--model_name="{model}" '
            f'--dataset_name="{dataset}" '
            f'--stock_pool="{pool}" '
            f'--rolling_type="{r_type}" '
            f'train start'
        )
        
        logger.info(f"[{current_idx}/{total_tasks}] 正在执行: {cmd}")
        start_time = time.time()
        
        try:
            # shell=True 允许执行完整的 shell 命令字符串
            # check=True 会在命令返回非0退出码时抛出异常
            subprocess.run(cmd, shell=True, check=True)
            
            elapsed = time.time() - start_time
            logger.info(f"✅ 任务 [{current_idx}/{total_tasks}] 完成! 耗时: {elapsed:.2f}秒\n")
            
        except subprocess.CalledProcessError as e:
            logger.info(f"❌ 任务 [{current_idx}/{total_tasks}] 失败! (Exit Code: {e.returncode})")
            logger.info(f"   跳过此任务，继续下一个...\n")
        except KeyboardInterrupt:
            logger.info("\n🛑 用户手动停止脚本。")
            break

if __name__ == "__main__":
    run_batch_experiments()