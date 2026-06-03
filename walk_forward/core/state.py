import json
import os
from pathlib import Path
from typing import List, Dict, Any
from loguru import logger

class WFStateManager:
    """管理重训历史记录并校验模型文件的完整性"""
    
    def __init__(self, state_file: str, mlruns_uri: str):
        self.state_file = Path(state_file).resolve()
        self.mlruns_dir = Path(mlruns_uri).expanduser().resolve()
        self.history = self._load_history()

    def _load_history(self) -> List[Dict[str, Any]]:
        if not self.state_file.exists():
            return []
        try:
            with open(self.state_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"加载状态文件失败: {e}")
            return []

    def save_retrain_event(self, date_str: str, tasks_status: Dict[str, str]):
        """
        记录一次成功的重训事件
        tasks_status: {task_name: run_id}
        """
        event = {
            "retrain_date": date_str,
            "tasks": tasks_status,
            "timestamp": os.path.getmtime(self.state_file) if self.state_file.exists() else None
        }
        self.history.append(event)
        # 按日期排序
        self.history.sort(key=lambda x: x["retrain_date"])
        
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump(self.history, f, indent=2, ensure_ascii=False)
        logger.info(f"已记录重训事件: {date_str}")

    def get_last_retrain_date(self) -> str:
        if not self.history:
            return ""
        return self.history[-1]["retrain_date"]

    def verify_consistency(self) -> bool:
        """
        检查历史记录中的所有重训点，其对应的 MLflow 产物是否真实存在于磁盘
        返回 False 表示发现记录丢失或损坏
        """
        if not self.history:
            return True
            
        logger.info("正在执行状态一致性检查...")
        all_ok = True
        valid_history = []
        
        for event in self.history:
            event_ok = True
            for task_name, run_id in event.get("tasks", {}).items():
                # MLflow 的存储结构通常是 mlruns/<exp_id>/<run_id>/artifacts/params.pkl
                # 这里我们简化检查 run_id 目录是否存在，或者更严格地检查 params.pkl
                # 遍历 mlruns 目录寻找 run_id (因为 exp_id 我们不确定)
                run_found = False
                for exp_dir in self.mlruns_dir.iterdir():
                    if not exp_dir.is_dir(): continue
                    run_dir = exp_dir / run_id
                    if run_dir.exists():
                        # 检查关键产物
                        if (run_dir / "artifacts" / "params.pkl").exists():
                            run_found = True
                            break
                
                if not run_found:
                    logger.warning(f"重训点 {event['retrain_date']} 的任务 {task_name} (ID: {run_id}) 产物丢失！")
                    event_ok = False
                    all_ok = False
            
            if event_ok:
                valid_history.append(event)
        
        if not all_ok:
            logger.warning("发现损坏的历史记录，已清理无效条目。")
            self.history = valid_history
            with open(self.state_file, "w", encoding="utf-8") as f:
                json.dump(self.history, f, indent=2, ensure_ascii=False)
                
        return all_ok
