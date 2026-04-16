# params 
 {'predict_dates': [{'start': '2026-04-16', 'end': '2026-04-16'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260416_16 344499797888155349 (Recorders: 3/5)

	Recorder: 28d74a1e3a14473d8d112286f39776af

		Model: {'id': '28d74a1e3a14473d8d112286f39776af', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.259, 'Rank IC': 0.045, 'Rank ICIR': 0.305}, 'data_train_vec': ['2023-04-16', '2025-07-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.305', 'weight': '0.082'}

	Recorder: a8b0087cd0624906acd06165c72c8850

		Model: {'id': 'a8b0087cd0624906acd06165c72c8850', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.33, 'Rank IC': 0.056, 'Rank ICIR': 0.391}, 'data_train_vec': ['2024-04-16', '2025-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.391', 'weight': '0.105'}

	Recorder: e653a644871a4de7ba2809befb74b49a

		Model: {'id': 'e653a644871a4de7ba2809befb74b49a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.062, 'ICIR': 0.37, 'Rank IC': 0.048, 'Rank ICIR': 0.292}, 'data_train_vec': ['2025-04-16', '2026-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.292', 'weight': '0.079'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260416_16 286439615900089074 (Recorders: 2/5)

	Recorder: eb1f6e6eb2fb40d28e19090a47b293ba

		Model: {'id': 'eb1f6e6eb2fb40d28e19090a47b293ba', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.125, 'Rank IC': 0.029, 'Rank ICIR': 0.239}, 'data_train_vec': ['2024-04-16', '2025-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.239', 'weight': '0.064'}

	Recorder: 6530b4ef21704c2bbf9179dfc7a52079

		Model: {'id': '6530b4ef21704c2bbf9179dfc7a52079', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.305, 'Rank IC': 0.037, 'Rank ICIR': 0.245}, 'data_train_vec': ['2025-04-16', '2026-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.245', 'weight': '0.066'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260416_14 540799381065665676 (Recorders: 4/5)

	Recorder: 251c689e2096480d89a71d828cc6bc5b

		Model: {'id': '251c689e2096480d89a71d828cc6bc5b', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.039, 'Rank IC': 0.024, 'Rank ICIR': 0.14}, 'data_train_vec': ['2021-04-16', '2025-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.140', 'weight': '0.038'}

	Recorder: cd02d15618544f6abf2867c796966193

		Model: {'id': 'cd02d15618544f6abf2867c796966193', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.096, 'Rank IC': 0.047, 'Rank ICIR': 0.274}, 'data_train_vec': ['2023-04-16', '2025-07-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.274', 'weight': '0.074'}

	Recorder: 87afb0e3904d481a8c0a5b75841f954f

		Model: {'id': '87afb0e3904d481a8c0a5b75841f954f', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.167, 'Rank IC': 0.032, 'Rank ICIR': 0.239}, 'data_train_vec': ['2024-04-16', '2025-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.239', 'weight': '0.064'}

	Recorder: 94825007d28744ef9de02f9e87f15ae8

		Model: {'id': '94825007d28744ef9de02f9e87f15ae8', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.051, 'ICIR': 0.282, 'Rank IC': 0.038, 'Rank ICIR': 0.201}, 'data_train_vec': ['2025-04-16', '2026-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.201', 'weight': '0.054'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260416_14 592278585623298708 (Recorders: 4/5)

	Recorder: 9dc3cc3bf7324e84b94f5ff6c35f3ef1

		Model: {'id': '9dc3cc3bf7324e84b94f5ff6c35f3ef1', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.032, 'Rank IC': 0.016, 'Rank ICIR': 0.136}, 'data_train_vec': ['2021-04-16', '2025-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.136', 'weight': '0.037'}

	Recorder: bc1866fde8274c1b90822f4ce2bab383

		Model: {'id': 'bc1866fde8274c1b90822f4ce2bab383', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.033, 'Rank IC': 0.029, 'Rank ICIR': 0.242}, 'data_train_vec': ['2023-04-16', '2025-07-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.242', 'weight': '0.065'}

	Recorder: e6fb308f7b09470cb5bfc08bb7faecb6

		Model: {'id': 'e6fb308f7b09470cb5bfc08bb7faecb6', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.076, 'Rank IC': 0.017, 'Rank ICIR': 0.142}, 'data_train_vec': ['2024-04-16', '2025-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.142', 'weight': '0.038'}

	Recorder: 9874321de0844c8a97dee69cd24f8cec

		Model: {'id': '9874321de0844c8a97dee69cd24f8cec', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.062, 'ICIR': 0.364, 'Rank IC': 0.048, 'Rank ICIR': 0.269}, 'data_train_vec': ['2025-04-16', '2026-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.269', 'weight': '0.072'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260416_14 491306118417098322 (Recorders: 3/5)

	Recorder: 815a94bb09e64a2b9a636ba52e9ce1c1

		Model: {'id': '815a94bb09e64a2b9a636ba52e9ce1c1', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.094, 'Rank IC': 0.021, 'Rank ICIR': 0.116}, 'data_train_vec': ['2021-04-16', '2025-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.116', 'weight': '0.031'}

	Recorder: 101131a911d14bbaa753c29ca55a4915

		Model: {'id': '101131a911d14bbaa753c29ca55a4915', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.102, 'Rank IC': 0.04, 'Rank ICIR': 0.241}, 'data_train_vec': ['2023-04-16', '2025-07-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.241', 'weight': '0.065'}

	Recorder: a172498b34ae4e679a708e501d90cd6f

		Model: {'id': 'a172498b34ae4e679a708e501d90cd6f', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.26, 'Rank IC': 0.035, 'Rank ICIR': 0.244}, 'data_train_vec': ['2025-04-16', '2026-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.244', 'weight': '0.066'}
