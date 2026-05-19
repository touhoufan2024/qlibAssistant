# params 
 {'predict_dates': [{'start': '2026-05-19', 'end': '2026-05-19'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260519_17 215704996630628585 (Recorders: 4/5)

	Recorder: 2f592afc65df4194b82c61603a0320d3

		Model: {'id': '2f592afc65df4194b82c61603a0320d3', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.085, 'Rank IC': 0.022, 'Rank ICIR': 0.143}, 'data_train_vec': ['2022-05-19', '2025-05-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.143', 'weight': '0.043'}

	Recorder: 13da5d717196474d91f9a7561d60905d

		Model: {'id': '13da5d717196474d91f9a7561d60905d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.029, 'Rank IC': 0.032, 'Rank ICIR': 0.196}, 'data_train_vec': ['2023-05-19', '2025-08-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.196', 'weight': '0.058'}

	Recorder: 6c3131c5a5cb4983a86cbd8dc76cd0fb

		Model: {'id': '6c3131c5a5cb4983a86cbd8dc76cd0fb', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.142, 'Rank IC': 0.01, 'Rank ICIR': 0.092}, 'data_train_vec': ['2024-05-19', '2025-11-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.092', 'weight': '0.027'}

	Recorder: dc03257ac7c94a0496e3d55ee09e1f21

		Model: {'id': 'dc03257ac7c94a0496e3d55ee09e1f21', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.258, 'Rank IC': 0.037, 'Rank ICIR': 0.227}, 'data_train_vec': ['2025-05-19', '2026-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.227', 'weight': '0.068'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260519_17 706143468430920092 (Recorders: 3/5)

	Recorder: d907be7dbc6b4adeb96c00aac7dcf033

		Model: {'id': 'd907be7dbc6b4adeb96c00aac7dcf033', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.164, 'Rank IC': 0.029, 'Rank ICIR': 0.243}, 'data_train_vec': ['2023-05-19', '2025-08-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.243', 'weight': '0.072'}

	Recorder: 1be193f1593f48648e22ebabf8202459

		Model: {'id': '1be193f1593f48648e22ebabf8202459', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.133, 'Rank IC': 0.005, 'Rank ICIR': 0.05}, 'data_train_vec': ['2024-05-19', '2025-11-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.050', 'weight': '0.015'}

	Recorder: 810650773fbb4e7e9a52b88e4bb2dccf

		Model: {'id': '810650773fbb4e7e9a52b88e4bb2dccf', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.09, 'ICIR': 0.577, 'Rank IC': 0.043, 'Rank ICIR': 0.257}, 'data_train_vec': ['2025-05-19', '2026-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.257', 'weight': '0.077'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260519_15 928640851950152299 (Recorders: 4/5)

	Recorder: 3f6b1f7296064ee99f05e9ebbcdd6985

		Model: {'id': '3f6b1f7296064ee99f05e9ebbcdd6985', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.029, 'Rank IC': 0.025, 'Rank ICIR': 0.168}, 'data_train_vec': ['2021-05-19', '2025-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.168', 'weight': '0.050'}

	Recorder: 6d55328c41b94450964406dd0a7953b5

		Model: {'id': '6d55328c41b94450964406dd0a7953b5', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.033, 'Rank IC': 0.034, 'Rank ICIR': 0.185}, 'data_train_vec': ['2022-05-19', '2025-05-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.185', 'weight': '0.055'}

	Recorder: d713df6028704606bd0c5f83b0d13c66

		Model: {'id': 'd713df6028704606bd0c5f83b0d13c66', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.141, 'Rank IC': 0.039, 'Rank ICIR': 0.252}, 'data_train_vec': ['2023-05-19', '2025-08-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.252', 'weight': '0.075'}

	Recorder: 333ed43a1f574ae298f3448874981cad

		Model: {'id': '333ed43a1f574ae298f3448874981cad', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.063, 'ICIR': 0.376, 'Rank IC': 0.031, 'Rank ICIR': 0.174}, 'data_train_vec': ['2025-05-19', '2026-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.174', 'weight': '0.052'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260519_15 737837632796617477 (Recorders: 4/5)

	Recorder: 89bb1a1169114b0d8f5278ef4d058901

		Model: {'id': '89bb1a1169114b0d8f5278ef4d058901', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.063, 'Rank IC': 0.031, 'Rank ICIR': 0.276}, 'data_train_vec': ['2021-05-19', '2025-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.276', 'weight': '0.082'}

	Recorder: 7dcccbf1acdf49c986947eb1881e11a8

		Model: {'id': '7dcccbf1acdf49c986947eb1881e11a8', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.091, 'Rank IC': 0.036, 'Rank ICIR': 0.325}, 'data_train_vec': ['2023-05-19', '2025-08-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.325', 'weight': '0.097'}

	Recorder: 9af37d0af9db4b2d83e1d9a8c5cd3c33

		Model: {'id': '9af37d0af9db4b2d83e1d9a8c5cd3c33', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.044, 'Rank IC': 0.014, 'Rank ICIR': 0.123}, 'data_train_vec': ['2024-05-19', '2025-11-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.123', 'weight': '0.037'}

	Recorder: e189db3dcf7c4d4094d35e1139c6c7fa

		Model: {'id': 'e189db3dcf7c4d4094d35e1139c6c7fa', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.069, 'ICIR': 0.504, 'Rank IC': 0.048, 'Rank ICIR': 0.302}, 'data_train_vec': ['2025-05-19', '2026-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.302', 'weight': '0.090'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260519_15 663291645648909532 (Recorders: 2/5)

	Recorder: 81e3347196b9417aa08b565ed90f4ab9

		Model: {'id': '81e3347196b9417aa08b565ed90f4ab9', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.022, 'Rank IC': 0.024, 'Rank ICIR': 0.148}, 'data_train_vec': ['2023-05-19', '2025-08-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.148', 'weight': '0.044'}

	Recorder: 79de62d9d6a9494f8e16264cba0a21df

		Model: {'id': '79de62d9d6a9494f8e16264cba0a21df', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.235, 'Rank IC': 0.031, 'Rank ICIR': 0.193}, 'data_train_vec': ['2025-05-19', '2026-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.193', 'weight': '0.058'}
