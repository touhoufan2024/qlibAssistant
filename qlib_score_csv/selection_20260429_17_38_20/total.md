# params 
 {'predict_dates': [{'start': '2026-04-29', 'end': '2026-04-29'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260429_17 510891024320453812 (Recorders: 2/5)

	Recorder: 25d0bdea930a4f8b8ca9378ee366164a

		Model: {'id': '25d0bdea930a4f8b8ca9378ee366164a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.06, 'Rank IC': 0.014, 'Rank ICIR': 0.142}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.142', 'weight': '0.091'}

	Recorder: b3a78504b8c4400bbc8352d2e4ed7547

		Model: {'id': 'b3a78504b8c4400bbc8352d2e4ed7547', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.185, 'Rank IC': 0.009, 'Rank ICIR': 0.056}, 'data_train_vec': ['2025-04-29', '2026-01-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.056', 'weight': '0.036'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260429_17 303298876613309433 (Recorders: 2/5)

	Recorder: 7fc96d77a53e43b098ad47a15b8c487a

		Model: {'id': '7fc96d77a53e43b098ad47a15b8c487a', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.082, 'Rank IC': 0.012, 'Rank ICIR': 0.111}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.111', 'weight': '0.071'}

	Recorder: fc81205cb468447da0b855f702848408

		Model: {'id': 'fc81205cb468447da0b855f702848408', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.063, 'ICIR': 0.543, 'Rank IC': 0.031, 'Rank ICIR': 0.232}, 'data_train_vec': ['2025-04-29', '2026-01-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.232', 'weight': '0.148'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260429_14 380754341754121380 (Recorders: 3/5)

	Recorder: 7c5eef6784164f26a5cd7142cdd09b47

		Model: {'id': '7c5eef6784164f26a5cd7142cdd09b47', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.041, 'Rank IC': 0.037, 'Rank ICIR': 0.216}, 'data_train_vec': ['2023-04-29', '2025-07-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.216', 'weight': '0.138'}

	Recorder: 5db6ae761697492784e6d08b4991e356

		Model: {'id': '5db6ae761697492784e6d08b4991e356', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.052, 'Rank IC': 0.003, 'Rank ICIR': 0.026}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.026', 'weight': '0.017'}

	Recorder: 25b5bf4bccca48a48d69d477f18aea76

		Model: {'id': '25b5bf4bccca48a48d69d477f18aea76', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.219, 'Rank IC': 0.012, 'Rank ICIR': 0.069}, 'data_train_vec': ['2025-04-29', '2026-01-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.069', 'weight': '0.044'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260429_14 375184397664047577 (Recorders: 2/5)

	Recorder: 7b5ee8d0b6704ab8b6c16a7223e3738a

		Model: {'id': '7b5ee8d0b6704ab8b6c16a7223e3738a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.031, 'Rank IC': 0.01, 'Rank ICIR': 0.084}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.084', 'weight': '0.054'}

	Recorder: 00ae8ef3d377471f92e20a54e1d84930

		Model: {'id': '00ae8ef3d377471f92e20a54e1d84930', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.068, 'ICIR': 0.626, 'Rank IC': 0.042, 'Rank ICIR': 0.342}, 'data_train_vec': ['2025-04-29', '2026-01-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.342', 'weight': '0.218'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260429_14 825483446180710142 (Recorders: 2/5)

	Recorder: df2a7633793f4fb9a4bfb094a1b9733d

		Model: {'id': 'df2a7633793f4fb9a4bfb094a1b9733d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.06, 'Rank IC': 0.02, 'Rank ICIR': 0.177}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.177', 'weight': '0.113'}

	Recorder: b1f42146089c4304a55c2ad587f7b8fd

		Model: {'id': 'b1f42146089c4304a55c2ad587f7b8fd', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.188, 'Rank IC': 0.014, 'Rank ICIR': 0.113}, 'data_train_vec': ['2025-04-29', '2026-01-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.113', 'weight': '0.072'}
