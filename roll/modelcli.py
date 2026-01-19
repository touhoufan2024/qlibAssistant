from loguru import logger
from tabulate import tabulate
from utils import check_match_in_list, append_to_file, get_normalized_stock_list
import numpy as np
import pandas as pd
import sys
import qlib
from qlib.constant import REG_CN
from qlib.data import D
from qlib.workflow import R
from qlib.config import C
from qlib.workflow.task.gen import RollingGen, task_generator
from qlib.workflow.task.manage import TaskManager, run_task
from qlib.workflow.task.collect import RecorderCollector
from qlib.model.ens.group import RollingGroup
from qlib.model.trainer import TrainerR, TrainerRM, task_train
from pathlib import Path
from myconfig import CSI300_RECORD_LGB_TASK_CONFIG, CSI100_RECORD_XGBOOST_TASK_CONFIG
from qlib.utils import init_instance_by_config
import os
from tqdm import tqdm
from functools import partialmethod
from pprint import pprint
import datetime
from qlib.contrib.data.handler import Alpha158, Alpha360
logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>"
)
from dataclasses import dataclass, field
from typing import List
import logging

@dataclass
class ModelContext:
    exp_name: str
    rid: List[str] = field(default_factory=list)

class ModelCLI:
    """
    [子模块] 模型仓库: 管理历史模型切片
    """
    def __init__(
        self,
        region=REG_CN,
        provider_uri="~/.qlib/qlib_data/cn_data",
        **kwargs
    ):
        uri_folder = kwargs["uri_folder"]
        self.kwargs = kwargs
        exp_manager = C["exp_manager"]
        exp_manager["kwargs"]["uri"] = "file:" + str(Path(uri_folder).expanduser())
        logger.info(f"Experiment uri: {exp_manager['kwargs']['uri']}")
        qlib.init(provider_uri=provider_uri, region=region, exp_manager=exp_manager) 

    def filter_rec(self, rec):
        ic_info, ic_list = self.get_ic_info(rec)
        ic_filter = self.kwargs['rec_filter']
        if not ic_filter:
            return True
        # print(ic_list, ic_filter)
        all_passed = all(val > list(d.values())[0] for val, d in zip(ic_list, ic_filter))
        # print("all_passed:", all_passed)
        if not all_passed:
            return False
        return True

    def get_model_list(self):
        logger.info(f"get all model in the uri_folder: {self.kwargs['uri_folder']}")
        f_list = self.kwargs['model_filter']
        exps = R.list_experiments()
        ret = []
        for a, b in exps.items():
            if a == 'Default':
                continue
            if not check_match_in_list(a, f_list):
                continue
            mc =  ModelContext(a) 
            exp = R.get_exp(experiment_name=a)
            for rid in exp.list_recorders():
                rec = exp.get_recorder(recorder_id=rid)
                if not rec.list_artifacts():
                    continue
                lista = rec.list_artifacts()
                if "params.pkl" not in lista or "sig_analysis" not in lista:
                    continue
                if not self.filter_rec(rec):
                    continue
                mc.rid.append(rid)
            ret.append(mc)
        logger.info(f"model_filter {self.kwargs['model_filter']}, rec_filter {self.kwargs['rec_filter']}")
        logger.info(f"experiment num: {str(len(ret))}, rid num: {str(sum(len(mc.rid) for mc in ret))}")
        return ret

    def get_ic_info(self, rec):
        ic = rec.load_object("sig_analysis/ic.pkl")
        ric = rec.load_object("sig_analysis/ric.pkl")
        IC = ic.mean()
        ICIR = ic.mean() / ic.std()
        RankIC = ric.mean()
        RankICIR = ric.mean() / ric.std()

        ic_info = {
            "IC": float(np.around(IC, 3)),
            "ICIR": float(np.around(ICIR, 3)),
            "Rank IC": float(np.around(RankIC, 3)),
            "Rank ICIR": float(np.around(RankICIR, 3)),
        }
        return ic_info, [IC, ICIR, RankIC, RankICIR]

    def get_train_time(self, rec):
        task = rec.load_object("task")
        start_time = rec.info['start_time'].split()[0]
        end_time = rec.info['end_time'].split()[0]
        data_train = task['dataset']['kwargs']['segments']['train']
        data_train_vec = [data_train[0].strftime("%Y-%m-%d"), data_train[1].strftime("%Y-%m-%d")]
        train_time_vec = [start_time, end_time]
        return data_train_vec, train_time_vec

    def print_rec(self, rec):
        task = rec.load_object("task")
        ic_info, ic_list = self.get_ic_info(rec)
        data_train_vec, train_time_vec = self.get_train_time(rec)
        print("\t", rec.id, task["model"]['class'], task['dataset']['kwargs']['handler']['class'], ic_info, data_train_vec, train_time_vec)
        # print(task)


    def ls(self, all=False):
        tqdm.__init__ = partialmethod(tqdm.__init__, disable=True)
        logger.info("Listing all model in the uri_folder:")
        model_list = self.get_model_list()
        for mc in model_list:
            exp = R.get_exp(experiment_name=mc.exp_name)
            count = len(mc.rid)
            print(f"Experiment: {exp.name} {exp.id} (Recorders: {count}/{len(exp.list_recorders())})")
            if all:
                for rid in mc.rid:
                    rec = exp.get_recorder(recorder_id=rid)
                    self.print_rec(rec)

    def clean(self):
        logger.info("清除无效的exp_name 和 rec:")
        exps = R.list_experiments()
        for name in exps:
            if name == 'Default':
                continue
            exp = R.get_exp(experiment_name=name)
            if len(exp.list_recorders()) == 0:
                logger.info(f"删除 Experiment: {name} {exp.id}")
                R.delete_exp(experiment_name=name)
                continue
            for rid in exp.list_recorders():
                rec = exp.get_recorder(recorder_id=rid)
                if (not rec.list_artifacts()) or ("params.pkl" not in rec.list_artifacts()) or ("sig_analysis" not in rec.list_artifacts()):
                    logger.info(f"Experiment: {name} 删除 Recorder: {rid} ")
                    exp.delete_recorder(rid)

    def anilysis(self, stock_list=None):
        """
        模型分析, 问股或者选股
        """
        logger.info("This is a placeholder for the analysis method.")
        logger.info(f"股票列表: {stock_list}")
        ret = []
        model_list = self.get_model_list()
        for mc in model_list:
            exp = R.get_exp(experiment_name=mc.exp_name)
            print(f"Experiment: {exp.name} {exp.id}")
            for rid in mc.rid:
                rec = exp.get_recorder(recorder_id=rid)
                task = rec.load_object("task")

                model = rec.load_object("params.pkl")
                logger.info(f"模型加载成功:{rec.id}")
                self.print_rec(rec)
                # print(rec.load_object("task"))
                dataset_config = task['dataset']
                # pprint(dataset_config)

                predict_date1 = pd.Timestamp(self.kwargs['predict_dates'][0]['start'])
                predict_date2 = pd.Timestamp(self.kwargs['predict_dates'][0]['end'])
                dataset_config['kwargs']['segments']['test'] = (predict_date1, predict_date2)
                dataset_config['kwargs']['handler']['kwargs']['end_time'] = predict_date2
                if stock_list is not None:
                    dataset_config['kwargs']['handler']['kwargs']['instruments'] = stock_list
                # pprint(dataset_config)

                dataset = init_instance_by_config(dataset_config)

                logger.info("数据集加载成功")
                # example_df = dataset.prepare("test")
                # print(example_df.head())
                pred_score = model.predict(dataset, segment="test")
                pprint(pred_score)
                ret.append([mc.exp_name, rid, pred_score])
        return ret

    def inquiry(self):
        """
        问股, 分析股票列表的 score
        """
        results = self.anilysis(stock_list=self.kwargs.get('stock_list', []))
        
        if not results:
            logger.warning("未获取到分析结果 (results is empty).")
            return
        self.collect(results, stock_list=self.kwargs.get('stock_list', []))

    def selection(self):
        """
        选股, 分析csi300成分股的 score
        """
        results = self.anilysis()
        
        if not results:
            logger.warning("未获取到分析结果 (results is empty).")
            return
        self.collect(results)

    def collect(self, results, stock_list=None):
        func_name = "nameless"
        if stock_list:
            func_name = "inquiry"
        else:
            func_name = "selection"

        latest_stock_list = get_normalized_stock_list()

        # --- 1. 数据处理 (List Comprehension + Pandas) ---
        processed_list = []
        for exp_name, rid, series_data in results:
            # 链式调用：转DataFrame -> 重置索引 -> 添加新列
            df = series_data.to_frame(name='score').reset_index()
            df['exp_name'] = exp_name
            df['rid'] = rid
            processed_list.append(df)

        # 合并并调整列顺序
        df_final = pd.concat(processed_list, axis=0, ignore_index=True)
        target_cols = ['exp_name', 'rid', 'datetime', 'instrument', 'score']
        # 确保列存在再筛选，防止报错 (鲁棒性)
        df_final = df_final[[c for c in target_cols if c in df_final.columns]]
        # 排序
        df_final['datetime'] = pd.to_datetime(df_final['datetime'])
        df_final = df_final.sort_values(by='datetime')

        # --- 2. 终端打印 ---
        # 打印表格 (psql 风格好看)
        # print(tabulate(df_final, headers='keys', tablefmt='psql', showindex=False))

        real_df = self.get_real_label()
        alpha158_df = self.get_alpha_data()
        alpha158_df = alpha158_df.reset_index()
        label_clean = real_df.reset_index()
        label_clean = label_clean[['datetime', 'instrument', 'real_label']]
        df_final['datetime'] = pd.to_datetime(df_final['datetime'])
        label_clean['datetime'] = pd.to_datetime(label_clean['datetime'])
        result_df = pd.merge(
            df_final, 
            label_clean, 
            on=['datetime', 'instrument'], 
            how='left'
        )
        result_df['error'] = result_df['score'] - result_df['real_label']
        result_df['abs_error'] = result_df['error'].abs()
        df_final = result_df
        print(result_df)

        # --- 3. 文件创建 ---
        base_dir = Path(self.kwargs['anilysis_folder']).expanduser()
        now_str = datetime.datetime.now().strftime("%Y%m%d_%H_%M_%S")
        save_dir = base_dir / f"{func_name}_{now_str}"
        save_dir.mkdir(parents=True, exist_ok=True)
        md_file_path = save_dir / "total.md"
        logger.info(f"保存路径: {md_file_path}")

        # --- 4. 保存 Markdown 和 CSV ---
        append_to_file(md_file_path, f" {now_str}\n\n")
        append_to_file(md_file_path, f" {self.kwargs}\n\n")
        
        # inquiry 模式下，按股票拆分保存
        if stock_list:
            for stock in stock_list:
                res = df_final[df_final['instrument'] == stock]
                append_to_file(md_file_path, f"\n\n # {stock}\n\n")

                sub_df = df_final[df_final['instrument'] == stock].copy()
                daily_scores = sub_df.groupby('datetime')['score'].apply(list)
                append_to_file(md_file_path, f"--- 股票 {stock} 的每日预测统计 ---\n\n")
                for date, scores in daily_scores.items():
                    scores_str = ", ".join([str(s) for s in scores])
                    positive_scores = [s for s in scores if s > 0]
                    pos_pct = (len(positive_scores) / len(scores)) * 100
                    append_to_file(md_file_path, f"{stock} 在 {date} 的 score 结果正向占比: {pos_pct}%\n\n")
                append_to_file(md_file_path, f"{res.to_markdown(index=False)}\n\n")

        # selection 模式下，按日期拆分保存
        if not stock_list:
            last_date = df_final['datetime'].max()
            for date, group_df in df_final.groupby('datetime'):
                date_str = str(date.date())
                append_to_file(md_file_path, f"\n\n # {date_str}\n\n")

                for model, model_df in group_df.groupby('rid'):
                    df_sorted = model_df.sort_values(by='score', ascending=False)
                    top_df = df_sorted.head(20).copy()  # 加上 .copy() 是为了避免后续修改时出现警告
                    append_to_file(md_file_path, f"\n\n ## 模型 {model}\n\n")
                    append_to_file(md_file_path, f"{top_df.to_markdown(index=False)}\n\n")

                # 1. 计算平均分和正向比例
                ret_df = group_df.groupby('instrument')['score'].agg(
                    avg_score='mean',
                    pos_ratio=lambda x: (x > 0).mean()
                ).reset_index()

                # 2. 按照 avg_score 从高到低排序
                ret_df = ret_df.sort_values(by='avg_score', ascending=False)

                # 3. 合并真实 label
                try:
                    # 1. 【关键步骤】预处理 real_df
                    # 如果 datetime 在索引里，把它变成了普通列，这样才能用 real_df['datetime']
                    # 为了不影响循环外的 real_df，我们只在切片时操作，或者使用一个临时变量
                    temp_real_df = real_df.copy()
                    if 'datetime' not in temp_real_df.columns:
                        temp_real_df = temp_real_df.reset_index()

                    # 2. 筛选当天的真实数据
                    # 确保类型一致：把两边都转为字符串比较，最稳妥
                    # (假设 date 是 Timestamp, temp_real_df['datetime'] 也是 Timestamp)
                    daily_real_df = temp_real_df[temp_real_df['datetime'] == date].copy()
                    
                    # 3. 准备要合并的数据
                    # 我们只需要 instrument 和 label
                    if 'real_label' in daily_real_df.columns:
                        daily_label = daily_real_df[['instrument', 'real_label']]
                    else:
                        # 尝试兼容 Qlib 默认的 label 列名 (通常是 'real_label' 或者 '$close' 等，具体看你数据)
                        # 如果找不到 label，尝试找最后一列
                        cols = daily_real_df.columns.tolist()
                        # 排除掉 instrument 和 datetime
                        value_cols = [c for c in cols if c not in ['datetime', 'instrument']]
                        if value_cols:
                            # 假设最后一列是 label
                            target_col = value_cols[-1] 
                            daily_label = daily_real_df[['instrument', target_col]].rename(columns={target_col: 'real_label'})
                        else:
                            print("Warning: 没在 real_df 里找到 label 列")
                            daily_label = pd.DataFrame(columns=['instrument', 'real_label'])

                    # 4. 合并
                    ret_df = pd.merge(ret_df, daily_label, on='instrument', how='left')

                except Exception as e:
                    print(f"合并真实 Label 时出错 (日期: {date}): {e}")
                    ret_df['real_label'] = float('nan')

                # 4. 合并 最新日期详细数据
                ret_df = pd.merge(
                    ret_df,
                    latest_stock_list, 
                    left_on='instrument', 
                    right_on='代码',
                    how='left'
                )

                alpha158_df_daily = alpha158_df[alpha158_df['datetime'] == date]
                # 5. 合并 Alpha158 数据
                ret_df = pd.merge(
                    ret_df,
                    alpha158_df_daily, 
                    on='instrument', 
                    how='left'
                )

                append_to_file(md_file_path, f"\n\n ## 简单平均 \n\n")
                append_to_file(md_file_path, f"{ret_df.to_markdown(index=False)}\n\n")
                logger.info(f"保存日期 {date_str} 分析结果 {save_dir}")
                ret_df.to_csv(save_dir / f"{date_str}_ret.csv", index=False, encoding="utf-8-sig")

        append_to_file(md_file_path, " # total\n\n")
        append_to_file(md_file_path, f"{df_final.to_markdown(index=False)}")
        # 保存 CSV
        df_final.to_csv(save_dir / "total.csv", index=False, encoding="utf-8-sig")
        
        logger.info("分析结果保存完成。")

    def get_real_label(self):
        start_time = self.kwargs['predict_dates'][0]['start']
        end_time = self.kwargs['predict_dates'][0]['end']
        logger.info(f"获取 real_label 数据: {start_time} -> {end_time}")

        df = D.features(D.instruments('all'), ['Ref($close, -2)/Ref($close, -1) - 1'],
            start_time = start_time,
            end_time = end_time,
            freq='day')
        df.columns = ['real_label']
        # print(df.info()) 
        # print(df)
        return df

    def get_alpha_data(self, name="Alpha158"):
        start_time = self.kwargs['predict_dates'][0]['start']
        end_time = self.kwargs['predict_dates'][0]['end']
        logger.info(f"获取 {name} 数据: {start_time} -> {end_time}")

        # 设定参数
        handler_kwargs = {
            "instruments": "csi300",  # 或者 D.instruments('all')，但注意内存
            "start_time": start_time,
            "end_time": end_time,
            "infer_processors": [] # 如果你想要原始值不归一化，可以传空列表，否则默认会有 ZScore
        }

        # 2. 实例化 Handler
        if name == "Alpha158":
            handler = Alpha158(**handler_kwargs)
        if name == "Alpha360":
            handler = Alpha360(**handler_kwargs)

        # 3. 获取 DataFrame
        # col_set="feature" 表示只获取特征列，不包含 label
        df = handler.fetch(col_set="feature")
        print(df)
        return df