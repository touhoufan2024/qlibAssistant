# params 
 {'predict_dates': [{'start': '2026-03-09', 'end': '2026-03-09'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'stock_list': ['SH601699', 'SH601318'], 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.03}, {'icir': 0.3}, {'rankic': 0.02}, {'rankicir': 0.2}]}



 # model info 

Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260309_15 158657308469953466 (Recorders: 1/5)

	Recorder: 03d8adce5ec445068e54adb3ccbc820d

		Model: {'id': '03d8adce5ec445068e54adb3ccbc820d', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.348, 'Rank IC': 0.055, 'Rank ICIR': 0.494}, 'data_train_vec': ['2025-03-09', '2025-12-08'], 'train_time_vec': ['2026-03-09', '2026-03-09']}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260309_13 129937724089840375 (Recorders: 2/5)

	Recorder: 7abd7f0944184d358db32d5ec90474bb

		Model: {'id': '7abd7f0944184d358db32d5ec90474bb', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.321, 'Rank IC': 0.031, 'Rank ICIR': 0.269}, 'data_train_vec': ['2024-03-09', '2025-09-08'], 'train_time_vec': ['2026-03-09', '2026-03-09']}

	Recorder: 321fbed1e65e4aef84846dba17508f30

		Model: {'id': '321fbed1e65e4aef84846dba17508f30', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.069, 'ICIR': 0.426, 'Rank IC': 0.072, 'Rank ICIR': 0.529}, 'data_train_vec': ['2025-03-09', '2025-12-08'], 'train_time_vec': ['2026-03-09', '2026-03-09']}
