from abc import ABC, abstractmethod
from utils import get_config
import os
from loguru import logger
import requests
import subprocess
import utils
from utils import ConfigLoader
from concurrent.futures import ProcessPoolExecutor, as_completed

# 创建本日的目录, 用于存放今日执行的结果 
# 执行任务, 将 mlrun 路径放在 今日目录中, 将 pkl 等全部保存


class Execute(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def runTasks(self):
        pass

class ExecuteYamls(Execute):
    def __init__(self, config):
        super().__init__(config)
        self.config = config

    @staticmethod
    def _run_single_task(cmd, work_dir):
        """
        静态辅助方法：在子进程中执行，不依赖 self。
        """
        logger.info(f"[进程 {os.getpid()}] 开始执行命令: {cmd}")
        try:
            # 注意：这里直接使用传入的 work_dir，而不是 self.config
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                check=True,
                cwd=work_dir
            )
            # 可以在这里记录，也可以返回给主进程记录
            logger.info(f"[进程 {os.getpid()}] 命令输出:\n{result.stdout}")
            return True, cmd, result.stdout
        except subprocess.CalledProcessError as e:
            error_msg = (
                f"命令执行失败！\n"
                f"命令: {e.cmd}\n"
                f"退出状态码: {e.returncode}\n"
                f"标准错误输出: {e.stderr}"
            )
            logger.error(f"[进程 {os.getpid()}] {error_msg}")
            return False, cmd, error_msg
        except FileNotFoundError as e:
            error_msg = f"未找到命令！错误信息: {e}"
            logger.error(f"[进程 {os.getpid()}] {error_msg}")
            return False, cmd, error_msg
        except Exception as e:
            error_msg = f"发生未知错误！错误信息: {e}"
            logger.error(f"[进程 {os.getpid()}] {error_msg}")
            return False, cmd, error_msg


    def runTasks(self):
        self.config.mkdir_output_folder()
        if self.config.output_folder_is_exists() and self.config.parse().force == 0:
            logger.info("Output folder already exists, skipping execution.")
            return None
        if self.config.parse().force == 0:
            logger.info("Force execution is disabled, skipping execution.")
            return None
        self.config.rm_output_folder()
        self.config.mkdir_output_folder()

        examples_qlib_path = os.path.join(self.config.config["qlib_path"], "examples")
        cmd_list = self.config.get_qrun_cmd_list()
        max_workers = self.config.config["work_num"]

        logger.info(f"开始并行执行任务，进程池大小: {max_workers}")

        # 3. 使用 ProcessPoolExecutor 并行执行
        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            # 提交任务
            # future_to_cmd 是一个字典，用于映射 future 对象到对应的命令，方便后续处理
            future_to_cmd = {
                executor.submit(self._run_single_task, cmd, examples_qlib_path): cmd
                for cmd in cmd_list
            }

            # 4. 等待结果 (as_completed 会在任务完成时立刻生成结果)
            for future in as_completed(future_to_cmd):
                cmd = future_to_cmd[future]
                try:
                    success, original_cmd, output = future.result()
                    if success:
                        logger.info(f"✅ 任务完成: {original_cmd}")
                    else:
                        logger.warning(f"❌ 任务失败: {original_cmd}")
                except Exception as exc:
                    logger.error(f"任务 {cmd} 抛出了异常: {exc}")

        logger.info("所有任务执行完毕。")


if __name__ == "__main__":
    cfig = utils.ConfigLoader()
    exec = ExecuteYamls(cfig)
    exec.runTasks()