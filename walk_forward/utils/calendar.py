import os
import yaml
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional, Tuple, Dict
from datetime import datetime
from dateutil.relativedelta import relativedelta
import bisect
from loguru import logger

# --- 数据结构定义 ---

@dataclass
class SplitConfig:
    method: str  # "ratio" (比例) or "fixed" (固定长度)
    unit: str    # "trading_days" or "months"
    train: float # 如果是 ratio 则是比例 (如 0.8), 如果是 fixed 则是具体数值 (如 1000 或 36)
    valid: float
    test: Optional[float] = None # 在重训切分时，test 通常指紧贴 Ti 之前的观察窗

@dataclass
class TaskConfig:
    name: str
    model_name: str
    dataset_name: str
    lookback_length: int
    lookback_unit: str # "trading_days" or "months"
    split: SplitConfig

@dataclass
class WFConfig:
    start_date: str
    end_date: str
    provider_uri: str
    mlruns_uri: str
    stock_pool: str
    trigger_unit: str # "trading_days" or "months"
    trigger_interval: int
    tasks: List[TaskConfig]

# --- 交易日历管理器 (不依赖 roll.utils) ---

class WFCalendar:
    def __init__(self, provider_uri: str):
        self.provider_uri = Path(provider_uri).expanduser()
        calendar_path = self.provider_uri / "calendars" / "day.txt"
        self.trade_dates = []
        if calendar_path.exists():
            with open(calendar_path, "r", encoding="utf-8") as f:
                self.trade_dates = [line.strip() for line in f if line.strip()]
        else:
            logger.error(f"未找到交易日历文件: {calendar_path}")

    def get_closest_trade_date(self, date_str: str, direction: str = "past") -> str:
        if not self.trade_dates: return date_str
        if date_str in self.trade_dates: return date_str
        idx = bisect.bisect_right(self.trade_dates, date_str)
        if direction == "past":
            return self.trade_dates[max(0, idx - 1)]
        return self.trade_dates[min(len(self.trade_dates) - 1, idx)]

    def offset_trading_days(self, start_date: str, days: int) -> str:
        base = self.get_closest_trade_date(start_date)
        try:
            idx = self.trade_dates.index(base)
            target_idx = max(0, min(len(self.trade_dates) - 1, idx + days))
            return self.trade_dates[target_idx]
        except ValueError:
            return base

    def offset_months(self, start_date: str, months: int) -> str:
        dt = datetime.strptime(start_date, "%Y-%m-%d")
        target_dt = dt + relativedelta(months=months)
        target_str = target_dt.strftime("%Y-%m-%d")
        return self.get_closest_trade_date(target_str, direction="past" if months < 0 else "future")

    def count_trading_days(self, start_date: str, end_date: str) -> int:
        try:
            s_idx = self.trade_dates.index(self.get_closest_trade_date(start_date, "future"))
            e_idx = self.trade_dates.index(self.get_closest_trade_date(end_date, "past"))
            return max(0, e_idx - s_idx + 1)
        except ValueError:
            return 0

    def generate_retrain_dates(self, start_date: str, end_date: str, unit: str, interval: int) -> List[str]:
        triggers = []
        current = self.get_closest_trade_date(start_date, "future")
        last_trade_date = self.trade_dates[-1]
        target_end = min(end_date, last_trade_date)
        
        while current <= target_end:
            triggers.append(current)
            if unit == "trading_days":
                next_date = self.offset_trading_days(current, interval)
            else:
                next_date = self.offset_months(current, interval)
            
            if next_date == current: break
            current = next_date
        return triggers

    def generate_split_segments(self, ti: str, lookback_unit: str, lookback_length: int, 
                                method: str, train_val: float, valid_val: float) -> Dict[str, Tuple[str, str]]:
        # 绝对严谨：训练数据必须止于重训点 Ti 之前的三个交易日 (Ti-3)
        # 因为 Alpha158 的 Label 需要未来 2 天的价格计算。在 Ti 日训练时，Ti-1 是已知最新价，
        # 故只有 Ti-3 的 Label 是基于完全已知数据计算的。
        data_end = self.offset_trading_days(ti, -3)
        
        # 计算回溯起点
        if lookback_unit == "trading_days":
            data_start = self.offset_trading_days(ti, -lookback_length)
        else:
            data_start = self.offset_months(ti, -lookback_length)
            
        # 计算切分点
        if method == "ratio":
            total_days = self.count_trading_days(data_start, data_end)
            train_days = int(total_days * (train_val / (train_val + valid_val)))
            train_end = self.offset_trading_days(data_start, train_days - 1)
            valid_start = self.offset_trading_days(train_end, 1)
        else: # fixed
            # 这里的 valid_val 被理解为从 data_end 向前推的天数或月数
            if lookback_unit == "trading_days":
                valid_start = self.offset_trading_days(ti, -int(valid_val))
            else:
                valid_start = self.offset_months(ti, -int(valid_val))
            train_end = self.offset_trading_days(valid_start, -1)
            
        return {
            "train": (data_start, train_end),
            "valid": (valid_start, data_end),
            "test": (ti, ti) # 默认 test 为重训点本身，随后会被 wf_cli 覆盖
        }
