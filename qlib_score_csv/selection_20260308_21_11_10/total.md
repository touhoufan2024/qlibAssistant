# params 
 {'predict_dates': [{'start': '2026-03-06', 'end': '2026-03-06'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'stock_list': ['SH601699', 'SH601318'], 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.03}, {'icir': 0.3}, {'rankic': 0.02}, {'rankicir': 0.2}]}



 # model info 

Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260308_20 469326048968797751 (Recorders: 1/5)

	Recorder: 9a1809d4a05642c0b6c44717d0b7791b

		Model: {'id': '9a1809d4a05642c0b6c44717d0b7791b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.056, 'ICIR': 0.369, 'Rank IC': 0.039, 'Rank ICIR': 0.318}, 'data_train_vec': ['2025-03-08', '2025-12-07'], 'train_time_vec': ['2026-03-08', '2026-03-08']}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260308_18 976217793700210755 (Recorders: 1/5)

	Recorder: 2f6bf48bd36a430f87480c2c22a5f1ec

		Model: {'id': '2f6bf48bd36a430f87480c2c22a5f1ec', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.076, 'ICIR': 0.493, 'Rank IC': 0.069, 'Rank ICIR': 0.543}, 'data_train_vec': ['2025-03-08', '2025-12-07'], 'train_time_vec': ['2026-03-08', '2026-03-08']}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260308_18 811839259337734857 (Recorders: 2/5)

	Recorder: b14392cb790a4c73821c9ea07c39b83d

		Model: {'id': 'b14392cb790a4c73821c9ea07c39b83d', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.343, 'Rank IC': 0.029, 'Rank ICIR': 0.246}, 'data_train_vec': ['2024-03-08', '2025-09-07'], 'train_time_vec': ['2026-03-08', '2026-03-08']}

	Recorder: 6b03741af6474555aa7bc2b8e643f11c

		Model: {'id': '6b03741af6474555aa7bc2b8e643f11c', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.064, 'ICIR': 0.595, 'Rank IC': 0.04, 'Rank ICIR': 0.456}, 'data_train_vec': ['2025-03-08', '2025-12-07'], 'train_time_vec': ['2026-03-08', '2026-03-08']}
