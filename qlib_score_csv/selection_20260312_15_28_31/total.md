# params 
 {'predict_dates': [{'start': '2026-03-12', 'end': '2026-03-12'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'stock_list': ['SH601699', 'SH601318'], 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.02}, {'icir': 0.25}, {'rankic': 0.02}, {'rankicir': 0.2}]}



 # model info 

Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260312_12 111441598852736287 (Recorders: 2/5)

	Recorder: c1b5872dcc3c4499bf749e404a666c3a

		Model: {'id': 'c1b5872dcc3c4499bf749e404a666c3a', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.278, 'Rank IC': 0.034, 'Rank ICIR': 0.311}, 'data_train_vec': ['2024-03-12', '2025-09-11'], 'train_time_vec': ['2026-03-12', '2026-03-12']}

	Recorder: a233a576ac05444e899c5717607cec27

		Model: {'id': 'a233a576ac05444e899c5717607cec27', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.256, 'Rank IC': 0.055, 'Rank ICIR': 0.502}, 'data_train_vec': ['2025-03-12', '2025-12-11'], 'train_time_vec': ['2026-03-12', '2026-03-12']}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260312_12 880489231297263464 (Recorders: 1/5)

	Recorder: cd58a528fe3548529e09443bec98af5b

		Model: {'id': 'cd58a528fe3548529e09443bec98af5b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.313, 'Rank IC': 0.058, 'Rank ICIR': 0.487}, 'data_train_vec': ['2025-03-12', '2025-12-11'], 'train_time_vec': ['2026-03-12', '2026-03-12']}
