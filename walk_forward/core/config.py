import yaml
from pathlib import Path
from ..utils.calendar import WFConfig, TaskConfig, SplitConfig

def load_wf_config(path: str) -> WFConfig:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    
    tasks = []
    for t in data.get("tasks", []):
        s = t.get("split", {})
        split = SplitConfig(
            method=s.get("method"),
            unit=s.get("unit"),
            train=s.get("train"),
            valid=s.get("valid"),
            test=s.get("test")
        )
        task = TaskConfig(
            name=t.get("name"),
            model_name=t.get("model_name"),
            dataset_name=t.get("dataset_name"),
            lookback_length=t.get("lookback_length"),
            lookback_unit=t.get("lookback_unit"),
            split=split
        )
        tasks.append(task)
        
    return WFConfig(
        start_date=data.get("start_date"),
        end_date=data.get("end_date"),
        provider_uri=data.get("provider_uri"),
        mlruns_uri=data.get("mlruns_uri"),
        stock_pool=data.get("stock_pool"),
        trigger_unit=data.get("trigger_unit"),
        trigger_interval=data.get("trigger_interval"),
        tasks=tasks
    )
