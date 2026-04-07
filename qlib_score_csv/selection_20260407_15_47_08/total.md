# params 
 {'predict_dates': [{'start': '2026-04-07', 'end': '2026-04-07'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260407_15 870916823857084939 (Recorders: 4/5)

	Recorder: bff55a63aa554eccafbe0da68ff9e104

		Model: {'id': 'bff55a63aa554eccafbe0da68ff9e104', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.048, 'Rank IC': 0.025, 'Rank ICIR': 0.135}, 'data_train_vec': ['2021-04-07', '2025-01-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.135', 'weight': '0.035'}

	Recorder: 83a5cd28e8074708baa529c1d1c1fc8f

		Model: {'id': '83a5cd28e8074708baa529c1d1c1fc8f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.011, 'Rank IC': 0.034, 'Rank ICIR': 0.182}, 'data_train_vec': ['2022-04-07', '2025-04-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.182', 'weight': '0.048'}

	Recorder: 67ed10859d6a44089aeb21c382016411

		Model: {'id': '67ed10859d6a44089aeb21c382016411', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.072, 'Rank IC': 0.048, 'Rank ICIR': 0.364}, 'data_train_vec': ['2023-04-07', '2025-07-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.364', 'weight': '0.095'}

	Recorder: a41a15bf075d479b870922ff886bffe4

		Model: {'id': 'a41a15bf075d479b870922ff886bffe4', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.322, 'Rank IC': 0.039, 'Rank ICIR': 0.336}, 'data_train_vec': ['2024-04-07', '2025-10-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.336', 'weight': '0.088'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260407_15 982336798382851630 (Recorders: 1/5)

	Recorder: afa5773fc5a14ecbb7681d433d4d80db

		Model: {'id': 'afa5773fc5a14ecbb7681d433d4d80db', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.302, 'Rank IC': 0.037, 'Rank ICIR': 0.312}, 'data_train_vec': ['2024-04-07', '2025-10-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.312', 'weight': '0.082'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260407_12 802512337622394489 (Recorders: 4/5)

	Recorder: 6ad091d7ca064d03b515c7d5692a35b4

		Model: {'id': '6ad091d7ca064d03b515c7d5692a35b4', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.1, 'Rank IC': 0.036, 'Rank ICIR': 0.195}, 'data_train_vec': ['2021-04-07', '2025-01-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.195', 'weight': '0.051'}

	Recorder: 3e1b80634be44d318fdeb86f631c2382

		Model: {'id': '3e1b80634be44d318fdeb86f631c2382', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.024, 'Rank IC': 0.034, 'Rank ICIR': 0.189}, 'data_train_vec': ['2022-04-07', '2025-04-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.189', 'weight': '0.050'}

	Recorder: bc7a0a820f3e4e3f952c976852419022

		Model: {'id': 'bc7a0a820f3e4e3f952c976852419022', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.132, 'Rank IC': 0.058, 'Rank ICIR': 0.331}, 'data_train_vec': ['2023-04-07', '2025-07-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.331', 'weight': '0.087'}

	Recorder: 6062be51472845998e0436548b869a96

		Model: {'id': '6062be51472845998e0436548b869a96', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.304, 'Rank IC': 0.033, 'Rank ICIR': 0.33}, 'data_train_vec': ['2024-04-07', '2025-10-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.330', 'weight': '0.087'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260407_12 676839182065917395 (Recorders: 3/5)

	Recorder: 08560f8c327b4b31a86ff813ac1dd514

		Model: {'id': '08560f8c327b4b31a86ff813ac1dd514', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.11, 'Rank IC': 0.023, 'Rank ICIR': 0.187}, 'data_train_vec': ['2021-04-07', '2025-01-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.187', 'weight': '0.049'}

	Recorder: 2f8802bc91914a6a8faf91371252d8a8

		Model: {'id': '2f8802bc91914a6a8faf91371252d8a8', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.054, 'Rank IC': 0.024, 'Rank ICIR': 0.204}, 'data_train_vec': ['2022-04-07', '2025-04-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.204', 'weight': '0.054'}

	Recorder: 3b4cae5432654897825d34ee9adc7775

		Model: {'id': '3b4cae5432654897825d34ee9adc7775', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.101, 'Rank IC': 0.039, 'Rank ICIR': 0.338}, 'data_train_vec': ['2023-04-07', '2025-07-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.338', 'weight': '0.089'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260407_12 738222674760582891 (Recorders: 3/5)

	Recorder: 3ce6d32dc9744f90a798f38efb3e93ca

		Model: {'id': '3ce6d32dc9744f90a798f38efb3e93ca', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.048, 'Rank IC': 0.028, 'Rank ICIR': 0.151}, 'data_train_vec': ['2021-04-07', '2025-01-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.151', 'weight': '0.040'}

	Recorder: 72a7bc16d8004305a3d442f814d946d0

		Model: {'id': '72a7bc16d8004305a3d442f814d946d0', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.087, 'Rank IC': 0.048, 'Rank ICIR': 0.286}, 'data_train_vec': ['2023-04-07', '2025-07-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.286', 'weight': '0.075'}

	Recorder: 2d6750f43c1e4a0bb4dd4db6cfdf3db7

		Model: {'id': '2d6750f43c1e4a0bb4dd4db6cfdf3db7', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.287, 'Rank IC': 0.032, 'Rank ICIR': 0.273}, 'data_train_vec': ['2024-04-07', '2025-10-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.273', 'weight': '0.072'}
