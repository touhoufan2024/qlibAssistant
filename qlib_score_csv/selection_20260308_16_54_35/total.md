# params 
 {'predict_dates': [{'start': '2026-03-06', 'end': '2026-03-06'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'stock_list': ['SH601699', 'SH601318'], 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.03}, {'icir': 0.3}, {'rankic': 0.02}, {'rankicir': 0.2}]}



 # model info 

Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260308_15 765535758186367582 (Recorders: 1/5)

	Recorder: 3a31a26784814e90be6f0e3abedfff7f

		Model: {'id': '3a31a26784814e90be6f0e3abedfff7f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.056, 'ICIR': 0.369, 'Rank IC': 0.039, 'Rank ICIR': 0.318}, 'data_train_vec': ['2025-03-08', '2025-12-07'], 'train_time_vec': ['2026-03-08', '2026-03-08']}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260308_12 762850902860982512 (Recorders: 1/5)

	Recorder: 1a76e1cb5ac24f08845bf5b24a685da0

		Model: {'id': '1a76e1cb5ac24f08845bf5b24a685da0', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.077, 'ICIR': 0.489, 'Rank IC': 0.08, 'Rank ICIR': 0.585}, 'data_train_vec': ['2025-03-08', '2025-12-07'], 'train_time_vec': ['2026-03-08', '2026-03-08']}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260308_12 924445783955222230 (Recorders: 2/5)

	Recorder: ddbfd8300374491fa4021a9b60c29b11

		Model: {'id': 'ddbfd8300374491fa4021a9b60c29b11', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.343, 'Rank IC': 0.029, 'Rank ICIR': 0.246}, 'data_train_vec': ['2024-03-08', '2025-09-07'], 'train_time_vec': ['2026-03-08', '2026-03-08']}

	Recorder: 48802dc52b1b4213ba1328a8fde17acf

		Model: {'id': '48802dc52b1b4213ba1328a8fde17acf', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.064, 'ICIR': 0.595, 'Rank IC': 0.04, 'Rank ICIR': 0.456}, 'data_train_vec': ['2025-03-08', '2025-12-07'], 'train_time_vec': ['2026-03-08', '2026-03-08']}
