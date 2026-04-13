# params 
 {'predict_dates': [{'start': '2026-04-13', 'end': '2026-04-13'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260413_16 648398555622997575 (Recorders: 3/5)

	Recorder: 6c0317e85506441c84834841047daec9

		Model: {'id': '6c0317e85506441c84834841047daec9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.28, 'Rank IC': 0.046, 'Rank ICIR': 0.316}, 'data_train_vec': ['2023-04-13', '2025-07-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.316', 'weight': '0.089'}

	Recorder: 3faf7ddfc789487aafe2bf6e5422f26b

		Model: {'id': '3faf7ddfc789487aafe2bf6e5422f26b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.224, 'Rank IC': 0.051, 'Rank ICIR': 0.411}, 'data_train_vec': ['2024-04-13', '2025-10-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.411', 'weight': '0.115'}

	Recorder: e8bbc951c0a24b5e8fd8858e3d745dbc

		Model: {'id': 'e8bbc951c0a24b5e8fd8858e3d745dbc', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.362, 'Rank IC': 0.043, 'Rank ICIR': 0.345}, 'data_train_vec': ['2025-04-13', '2026-01-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.345', 'weight': '0.097'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260413_16 450431214942585564 (Recorders: 2/5)

	Recorder: 0587a5f6edbc48168e37548e095254b4

		Model: {'id': '0587a5f6edbc48168e37548e095254b4', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.108, 'Rank IC': 0.017, 'Rank ICIR': 0.141}, 'data_train_vec': ['2024-04-13', '2025-10-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.141', 'weight': '0.040'}

	Recorder: 6c07159c59c84e3f933465dd8aacacf9

		Model: {'id': '6c07159c59c84e3f933465dd8aacacf9', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.203, 'Rank IC': 0.036, 'Rank ICIR': 0.223}, 'data_train_vec': ['2025-04-13', '2026-01-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.223', 'weight': '0.063'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260413_14 110031488376067241 (Recorders: 4/5)

	Recorder: 8821c59709774a4180e8395c61e90bca

		Model: {'id': '8821c59709774a4180e8395c61e90bca', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.024, 'Rank IC': 0.022, 'Rank ICIR': 0.132}, 'data_train_vec': ['2021-04-13', '2025-01-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.132', 'weight': '0.037'}

	Recorder: 64573b0bbfed4c60a92c89ba3d82d9df

		Model: {'id': '64573b0bbfed4c60a92c89ba3d82d9df', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.097, 'Rank IC': 0.047, 'Rank ICIR': 0.283}, 'data_train_vec': ['2023-04-13', '2025-07-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.283', 'weight': '0.080'}

	Recorder: 1a9e1bc1adc343f3b90637994beedf09

		Model: {'id': '1a9e1bc1adc343f3b90637994beedf09', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.099, 'Rank IC': 0.02, 'Rank ICIR': 0.17}, 'data_train_vec': ['2024-04-13', '2025-10-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.170', 'weight': '0.048'}

	Recorder: 9b8513b6ce4a4b42872cd05cd22209cf

		Model: {'id': '9b8513b6ce4a4b42872cd05cd22209cf', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.135, 'Rank IC': 0.016, 'Rank ICIR': 0.094}, 'data_train_vec': ['2025-04-13', '2026-01-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.094', 'weight': '0.026'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260413_14 947046112820953674 (Recorders: 4/5)

	Recorder: 4e93027fcea44cc98ababa2d72738886

		Model: {'id': '4e93027fcea44cc98ababa2d72738886', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.063, 'Rank IC': 0.018, 'Rank ICIR': 0.16}, 'data_train_vec': ['2021-04-13', '2025-01-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.160', 'weight': '0.045'}

	Recorder: 962d36eef2e748d3b33b326bcec3a3b3

		Model: {'id': '962d36eef2e748d3b33b326bcec3a3b3', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.1, 'Rank IC': 0.037, 'Rank ICIR': 0.321}, 'data_train_vec': ['2023-04-13', '2025-07-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.321', 'weight': '0.090'}

	Recorder: ffa9b0bace2547a9bd8edf00f08a557b

		Model: {'id': 'ffa9b0bace2547a9bd8edf00f08a557b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.115, 'Rank IC': 0.02, 'Rank ICIR': 0.172}, 'data_train_vec': ['2024-04-13', '2025-10-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.172', 'weight': '0.048'}

	Recorder: cd11e392878840b38752bc372cac9e1e

		Model: {'id': 'cd11e392878840b38752bc372cac9e1e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.2, 'Rank IC': 0.022, 'Rank ICIR': 0.138}, 'data_train_vec': ['2025-04-13', '2026-01-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.138', 'weight': '0.039'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260413_14 480156686633248556 (Recorders: 3/5)

	Recorder: c1645976e41048c19df7f20b7ab22b0d

		Model: {'id': 'c1645976e41048c19df7f20b7ab22b0d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.124, 'Rank IC': 0.037, 'Rank ICIR': 0.226}, 'data_train_vec': ['2023-04-13', '2025-07-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.226', 'weight': '0.064'}

	Recorder: 82717269be33433f8a1b919eeb371b2a

		Model: {'id': '82717269be33433f8a1b919eeb371b2a', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.161, 'Rank IC': 0.041, 'Rank ICIR': 0.351}, 'data_train_vec': ['2024-04-13', '2025-10-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.351', 'weight': '0.099'}

	Recorder: 4e4b0781335644f98acf80700cf6f6d8

		Model: {'id': '4e4b0781335644f98acf80700cf6f6d8', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.121, 'Rank IC': 0.012, 'Rank ICIR': 0.076}, 'data_train_vec': ['2025-04-13', '2026-01-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.076', 'weight': '0.021'}
