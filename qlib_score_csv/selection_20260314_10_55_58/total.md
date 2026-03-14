# params 
 {'predict_dates': [{'start': '2026-03-13', 'end': '2026-03-13'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'stock_list': ['SH601699', 'SH601318'], 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.02}, {'icir': 0.25}, {'rankic': 0.02}, {'rankicir': 0.2}]}



 # model info 

Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260314_08 496693124032819978 (Recorders: 2/5)

	Recorder: 12b9658903fe4bb994f115472828ade0

		Model: {'id': '12b9658903fe4bb994f115472828ade0', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.255, 'Rank IC': 0.028, 'Rank ICIR': 0.282}, 'data_train_vec': ['2024-03-14', '2025-09-13'], 'train_time_vec': ['2026-03-14', '2026-03-14']}

	Recorder: 789c459d0e1d40629e379c401e78d720

		Model: {'id': '789c459d0e1d40629e379c401e78d720', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.276, 'Rank IC': 0.066, 'Rank ICIR': 0.616}, 'data_train_vec': ['2025-03-14', '2025-12-13'], 'train_time_vec': ['2026-03-14', '2026-03-14']}
