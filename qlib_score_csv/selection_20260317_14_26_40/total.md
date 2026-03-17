# params 
 {'predict_dates': [{'start': '2026-03-17', 'end': '2026-03-17'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.02}, {'icir': 0.25}, {'rankic': 0.02}, {'rankicir': 0.2}]}



 # model info 

Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260317_12 325812596008727400 (Recorders: 1/5)

	Recorder: c29cd594b1f341389dcecf762c0981a2

		Model: {'id': 'c29cd594b1f341389dcecf762c0981a2', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.254, 'Rank IC': 0.03, 'Rank ICIR': 0.301}, 'data_train_vec': ['2024-03-17', '2025-09-16'], 'train_time_vec': ['2026-03-17', '2026-03-17']}
