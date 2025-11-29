
from abc import ABC, abstractmethod
from utils import get_config
import os
from loguru import logger
import requests
import subprocess
import utils
import qlib
import pandas as pd
from qlib.constant import REG_CN
from qlib.utils import init_instance_by_config, flatten_dict
from qlib.workflow import R
from qlib.config import C
from qlib.workflow.record_temp import SignalRecord, PortAnaRecord, SigAnaRecord
from qlib.tests.data import GetData
from qlib.tests.config import CSI300_BENCH, CSI300_GBDT_TASK

from qlib.contrib.report import analysis_model, analysis_position

from loguru import logger

from dataclasses import dataclass, field
from typing import List

# 统计 某个mlrun目录内的结果
# 重点关注的内容有 label 的排序, 以及性能的排序

class Collector(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def analysis(self):
        pass

@dataclass
class ExperimentInfo:
    id: str
    name: str
    recorders: List[str] = field(default_factory=list)
    config: utils.ConfigLoader = utils.ConfigLoader()

    def set_recorder(self, recorder):
        self.recorder = recorder

    def load_pkl(self):
        self.loaded_objects = {}
        self.loaded_objects['pred'] = self.recorder.load_object("pred.pkl")
        self.loaded_objects['ic_data'] = self.recorder.load_object("sig_analysis/ic.pkl")
        self.loaded_objects['ric_data'] = self.recorder.load_object("sig_analysis/ric.pkl")
        self.loaded_objects['indicators_normal_1day_obj'] = self.recorder.load_object("portfolio_analysis/indicators_normal_1day_obj.pkl")
        self.loaded_objects['report_normal_1day'] = self.recorder.load_object("portfolio_analysis/report_normal_1day.pkl")
        self.loaded_objects['positions_normal_1day'] = self.recorder.load_object("portfolio_analysis/positions_normal_1day.pkl")
        self.loaded_objects['indicators_normal_1day'] = self.recorder.load_object("portfolio_analysis/indicators_normal_1day.pkl")  # 注意这和上面的区分
        self.loaded_objects['port_analysis_1day'] = self.recorder.load_object("portfolio_analysis/port_analysis_1day.pkl")
        self.loaded_objects['indicator_analysis_1day'] = self.recorder.load_object("portfolio_analysis/indicator_analysis_1day.pkl")
        self.loaded_objects['label'] = self.recorder.load_object("label.pkl")
        self.loaded_objects['params'] = self.recorder.load_object("params.pkl")

        self.pred_label = pd.concat([self.loaded_objects['label'], self.loaded_objects['pred']], axis=1, sort=True).reindex(self.loaded_objects['label'].index)
        self.pred_label.columns = ['label', 'score']

        self.output_dir= os.path.join(self.config.get_output_folder(),"myanalysis", self.name, self.recorder.experiment_id, self.recorder.id)
        os.makedirs(self.output_dir, exist_ok=True)

    def pkls_to_csv(self):
        logger.info(f"Saving loaded PKL objects to CSV in directory: {self.output_dir}")
        for key, df in self.loaded_objects.items():
            if isinstance(df, pd.DataFrame) or isinstance(df, pd.Series):
                csv_path = os.path.join(self.output_dir, f"{key}.csv")
                df.to_csv(csv_path)
                logger.info(f"Saved {key} to {csv_path}")

    def save_figures(self, fig_list, prefix):
        for i, fig in enumerate(fig_list):
            base_name = f"{prefix}_{i:02d}"
            img_path = os.path.join(self.output_dir, f"{base_name}.png")
            logger.info(f"save pic: {img_path}")

            fig.write_image(
                img_path,
                format="png",
                width=1200,
                height=800,
                scale=2
            )

    def pkls_to_pictures(self):
        logger.info(f"Saving loaded PKL objects to pictures in directory: {self.output_dir}")
        self.report_figs = analysis_position.report_graph(self.loaded_objects['report_normal_1day'], show_notebook=False)
        self.save_figures(self.report_figs, "report")

        self.risk_figs = analysis_position.risk_analysis_graph(self.loaded_objects['port_analysis_1day'], self.loaded_objects['report_normal_1day'], show_notebook=False)
        self.save_figures(self.risk_figs, "risk_analysis")

        self.ic_figs = analysis_position.score_ic_graph(self.pred_label, show_notebook=False)
        self.save_figures(self.ic_figs, "score_ic")

        self.model_figs = analysis_model.model_performance_graph(self.pred_label, show_notebook=False)
        self.save_figures(self.model_figs, "model_performance")


    def calc_ic(self):
        ic = self.loaded_objects['ic_data']
        ric = self.loaded_objects['ric_data']
        self.IC = ic.mean()
        self.ICIR = ic.mean() / ic.std()
        self.RankIC = ric.mean()
        self.RankICIR = ric.mean() / ric.std()

        metrics = {
            "IC": ic.mean(),
            "ICIR": ic.mean() / ic.std(),
            "Rank IC": ric.mean(),
            "Rank ICIR": ric.mean() / ric.std(),
        }
        logger.info(metrics)

    def handle(self):
        self.pkls_to_csv()
        self.pkls_to_pictures()
        self.calc_ic()

    def handle_pred(self):
        pass

class CollectorMlrunDir(Collector):
    def __init__(self, config):
        super().__init__(config)
        self.config = config
        self.experiment_list: List[ExperimentInfo] = []
    
    def qlib_init(self, mlrun_dir = "../mlruns"):
        logger.info(f"Initializing Qlib with mlrun dir: {mlrun_dir}")
        provider_uri = "~/.qlib/qlib_data/cn_data"  # target_dir
        exp_manager = C["exp_manager"]
        # exp_manager["kwargs"]["uri"] = "file:" + self.config.get_output_folder()
        exp_manager["kwargs"]["uri"] = "file:" + mlrun_dir
        qlib.init(provider_uri=provider_uri, region=REG_CN, exp_manager=exp_manager)

    def get_all_exps(self):
        exps = R.list_experiments()
        for a, b in exps.items():
            exp_info = ExperimentInfo(id=b.id, name=b.name, recorders=b.info['recorders'], config = self.config)
            self.experiment_list.append(exp_info)

    def show_all_exps(self):
        logger.info(f"Found {len(self.experiment_list)} experiments:")
        for exp in self.experiment_list:
            logger.info(f"Experiment ID: {exp.id}, Name: {exp.name}, Recorders: {exp.recorders}")
            expp = R.get_exp(experiment_name=exp.name, create=False)
            rec = expp.get_recorder(recorder_id=exp.recorders[0])
            exp.set_recorder(rec)

    def load_all_pkls(self):
        logger.info("Loading PKL files for all experiments...")
        for exp in self.experiment_list:
            logger.info(f"Loading PKL files for Experiment ID: {exp.id}, Name: {exp.name} rid: {exp.recorder.id}..")
            exp.load_pkl()

    def handle_all_pkls(self):
        logger.info("Handling PKL files for all experiments...")
        for exp in self.experiment_list:
            exp.handle()

    def analysis(self, mlrun_dir=None):
        if mlrun_dir is None:
            mlrun_dir = self.config.get_output_folder()
        logger.info(f"Analyzing mlrun dir: {mlrun_dir} ...")
        self.qlib_init(mlrun_dir)
        self.get_all_exps()
        self.show_all_exps()
        self.load_all_pkls()
        self.handle_all_pkls()


if __name__ == "__main__":
    cfig = utils.ConfigLoader()
    coll = CollectorMlrunDir(cfig)
    coll.analysis("/home/ash/.qlibAssistant/2025-11-27-20/")
