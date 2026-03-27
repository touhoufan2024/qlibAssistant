# params 
 {'predict_dates': [{'start': '2026-03-27', 'end': '2026-03-27'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260327_16 737335210786894193 (Recorders: 5/5)

	Recorder: 5646adfaefeb4e5a9607a8376a3ab693

		Model: {'id': '5646adfaefeb4e5a9607a8376a3ab693', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.046, 'Rank IC': 0.021, 'Rank ICIR': 0.157}, 'data_train_vec': ['2021-03-27', '2024-12-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.157', 'weight': '0.046'}

	Recorder: 6d041dd01f0f4e5e88c106faaaac8b8e

		Model: {'id': '6d041dd01f0f4e5e88c106faaaac8b8e', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.058, 'Rank IC': 0.034, 'Rank ICIR': 0.169}, 'data_train_vec': ['2022-03-27', '2025-03-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.169', 'weight': '0.050'}

	Recorder: 462250298776474eb80b8c9975d978be

		Model: {'id': '462250298776474eb80b8c9975d978be', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.001, 'ICIR': 0.008, 'Rank IC': 0.049, 'Rank ICIR': 0.324}, 'data_train_vec': ['2023-03-27', '2025-06-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.324', 'weight': '0.096'}

	Recorder: 87329fdf25a14ab7a419a110ff02d5d1

		Model: {'id': '87329fdf25a14ab7a419a110ff02d5d1', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.093, 'Rank IC': 0.036, 'Rank ICIR': 0.249}, 'data_train_vec': ['2024-03-27', '2025-09-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.249', 'weight': '0.073'}

	Recorder: c3eb26f5ed4e4e7497215ea5257fc959

		Model: {'id': 'c3eb26f5ed4e4e7497215ea5257fc959', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.019, 'Rank IC': 0.005, 'Rank ICIR': 0.036}, 'data_train_vec': ['2025-03-27', '2025-12-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.036', 'weight': '0.011'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260327_16 697820401338384474 (Recorders: 2/5)

	Recorder: 27ae29c372a943989ab3bc90bb6f0fdd

		Model: {'id': '27ae29c372a943989ab3bc90bb6f0fdd', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.045, 'Rank IC': 0.026, 'Rank ICIR': 0.162}, 'data_train_vec': ['2021-03-27', '2024-12-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.162', 'weight': '0.048'}

	Recorder: 9f07a2ecae484ed290d0694102f0a998

		Model: {'id': '9f07a2ecae484ed290d0694102f0a998', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.285, 'Rank IC': 0.046, 'Rank ICIR': 0.36}, 'data_train_vec': ['2024-03-27', '2025-09-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.360', 'weight': '0.106'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260327_13 332888271884250743 (Recorders: 3/5)

	Recorder: 4ac944e9926d49b887928661f4210ca6

		Model: {'id': '4ac944e9926d49b887928661f4210ca6', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.108, 'Rank IC': 0.037, 'Rank ICIR': 0.207}, 'data_train_vec': ['2021-03-27', '2024-12-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.207', 'weight': '0.061'}

	Recorder: a45ac0e333384bc28f15292080c40eef

		Model: {'id': 'a45ac0e333384bc28f15292080c40eef', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.193, 'Rank IC': 0.03, 'Rank ICIR': 0.259}, 'data_train_vec': ['2024-03-27', '2025-09-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.259', 'weight': '0.076'}

	Recorder: 233fd969642a4b1092faf82599471d7c

		Model: {'id': '233fd969642a4b1092faf82599471d7c', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.054, 'Rank IC': 0.021, 'Rank ICIR': 0.199}, 'data_train_vec': ['2025-03-27', '2025-12-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.199', 'weight': '0.059'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260327_13 949653153316339667 (Recorders: 5/5)

	Recorder: cd9fa42c04bf4d0cb163806ee8af03e2

		Model: {'id': 'cd9fa42c04bf4d0cb163806ee8af03e2', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.166, 'Rank IC': 0.028, 'Rank ICIR': 0.24}, 'data_train_vec': ['2021-03-27', '2024-12-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.240', 'weight': '0.071'}

	Recorder: 8bdfd07f40744fa3b5fd4c45d2ca91e6

		Model: {'id': '8bdfd07f40744fa3b5fd4c45d2ca91e6', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.057, 'Rank IC': 0.023, 'Rank ICIR': 0.199}, 'data_train_vec': ['2022-03-27', '2025-03-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.199', 'weight': '0.059'}

	Recorder: 33f1399a99f14053b45c4c1f00838925

		Model: {'id': '33f1399a99f14053b45c4c1f00838925', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.136, 'Rank IC': 0.039, 'Rank ICIR': 0.353}, 'data_train_vec': ['2023-03-27', '2025-06-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.353', 'weight': '0.104'}

	Recorder: e3d83c3eaa724f299e335e38bc61ca80

		Model: {'id': 'e3d83c3eaa724f299e335e38bc61ca80', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.127, 'Rank IC': 0.015, 'Rank ICIR': 0.121}, 'data_train_vec': ['2024-03-27', '2025-09-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.121', 'weight': '0.036'}

	Recorder: 77976c2b1f6b4420a9500570679aea5e

		Model: {'id': '77976c2b1f6b4420a9500570679aea5e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.075, 'Rank IC': 0.017, 'Rank ICIR': 0.151}, 'data_train_vec': ['2025-03-27', '2025-12-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.151', 'weight': '0.045'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260327_13 623713513443187850 (Recorders: 1/5)

	Recorder: fa25660291104148860f4539114db5ed

		Model: {'id': 'fa25660291104148860f4539114db5ed', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.067, 'Rank IC': 0.037, 'Rank ICIR': 0.205}, 'data_train_vec': ['2021-03-27', '2024-12-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.205', 'weight': '0.060'}
