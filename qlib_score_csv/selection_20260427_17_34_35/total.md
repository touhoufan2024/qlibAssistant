# params 
 {'predict_dates': [{'start': '2026-04-27', 'end': '2026-04-27'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260427_17 296202884048707460 (Recorders: 2/5)

	Recorder: 331dcbdff1064d77aa79b6e5b477282f

		Model: {'id': '331dcbdff1064d77aa79b6e5b477282f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.045, 'Rank IC': 0.027, 'Rank ICIR': 0.161}, 'data_train_vec': ['2023-04-27', '2025-07-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.161', 'weight': '0.100'}

	Recorder: a7a4172c87c548bfa93b00248202f06c

		Model: {'id': 'a7a4172c87c548bfa93b00248202f06c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.154, 'Rank IC': 0.003, 'Rank ICIR': 0.02}, 'data_train_vec': ['2025-04-27', '2026-01-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.020', 'weight': '0.012'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260427_17 663603235349751977 (Recorders: 3/5)

	Recorder: e6e4e98e56664ad480a94b6fc33786b7

		Model: {'id': 'e6e4e98e56664ad480a94b6fc33786b7', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.048, 'Rank IC': 0.03, 'Rank ICIR': 0.211}, 'data_train_vec': ['2023-04-27', '2025-07-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.211', 'weight': '0.131'}

	Recorder: b26c161ad80541e58e2638cf13463324

		Model: {'id': 'b26c161ad80541e58e2638cf13463324', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.057, 'Rank IC': 0.015, 'Rank ICIR': 0.121}, 'data_train_vec': ['2024-04-27', '2025-10-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.121', 'weight': '0.075'}

	Recorder: 1412769aa286491cb2ec8ffd4960e1f8

		Model: {'id': '1412769aa286491cb2ec8ffd4960e1f8', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.24, 'Rank IC': 0.021, 'Rank ICIR': 0.136}, 'data_train_vec': ['2025-04-27', '2026-01-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.136', 'weight': '0.084'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260427_14 998657384505633229 (Recorders: 3/5)

	Recorder: 9c3e7fd931004bd79b662757fb8cba98

		Model: {'id': '9c3e7fd931004bd79b662757fb8cba98', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.088, 'Rank IC': 0.044, 'Rank ICIR': 0.266}, 'data_train_vec': ['2023-04-27', '2025-07-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.266', 'weight': '0.165'}

	Recorder: 90710309d89f4657a75306eb4dc59d1b

		Model: {'id': '90710309d89f4657a75306eb4dc59d1b', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.064, 'Rank IC': 0.009, 'Rank ICIR': 0.077}, 'data_train_vec': ['2024-04-27', '2025-10-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.077', 'weight': '0.048'}

	Recorder: dd596ecf3b454381a21d539476e4d46c

		Model: {'id': 'dd596ecf3b454381a21d539476e4d46c', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.167, 'Rank IC': 0.009, 'Rank ICIR': 0.049}, 'data_train_vec': ['2025-04-27', '2026-01-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.049', 'weight': '0.030'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260427_14 210191435176051402 (Recorders: 2/5)

	Recorder: a45b72b28ff34ae1ae9cd1adddf42b87

		Model: {'id': 'a45b72b28ff34ae1ae9cd1adddf42b87', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.014, 'Rank IC': 0.009, 'Rank ICIR': 0.072}, 'data_train_vec': ['2024-04-27', '2025-10-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.072', 'weight': '0.045'}

	Recorder: 3a3cf9aaaf054b75bfbd6840e7117f57

		Model: {'id': '3a3cf9aaaf054b75bfbd6840e7117f57', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.057, 'ICIR': 0.452, 'Rank IC': 0.032, 'Rank ICIR': 0.223}, 'data_train_vec': ['2025-04-27', '2026-01-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.223', 'weight': '0.138'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260427_14 178945260130064615 (Recorders: 2/5)

	Recorder: a28f4ecec267466d9cd9bb1e25898dbb

		Model: {'id': 'a28f4ecec267466d9cd9bb1e25898dbb', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.081, 'Rank IC': 0.029, 'Rank ICIR': 0.265}, 'data_train_vec': ['2024-04-27', '2025-10-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.265', 'weight': '0.164'}

	Recorder: b263cd2dbc2543c28accf39eb5f0c1ca

		Model: {'id': 'b263cd2dbc2543c28accf39eb5f0c1ca', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.055, 'Rank IC': 0.002, 'Rank ICIR': 0.012}, 'data_train_vec': ['2025-04-27', '2026-01-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.012', 'weight': '0.007'}
