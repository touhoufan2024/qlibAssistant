# params 
 {'predict_dates': [{'start': '2026-03-13', 'end': '2026-03-13'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'stock_list': ['SH601699', 'SH601318'], 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.02}, {'icir': 0.25}, {'rankic': 0.02}, {'rankicir': 0.2}]}



 # model info 

Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260314_01 382284216727150022 (Recorders: 2/5)

	Recorder: 3a9a17b46a9f4f28a561431ea759348f

		Model: {'id': '3a9a17b46a9f4f28a561431ea759348f', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.253, 'Rank IC': 0.035, 'Rank ICIR': 0.35}, 'data_train_vec': ['2024-03-14', '2025-09-13'], 'train_time_vec': ['2026-03-14', '2026-03-14']}

	Recorder: 917eac3e631544f2bc8560c6c31156ed

		Model: {'id': '917eac3e631544f2bc8560c6c31156ed', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.304, 'Rank IC': 0.074, 'Rank ICIR': 0.637}, 'data_train_vec': ['2025-03-14', '2025-12-13'], 'train_time_vec': ['2026-03-14', '2026-03-14']}
