# params 
 {'predict_dates': [{'start': '2026-05-18', 'end': '2026-05-18'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260518_18 890080988693875427 (Recorders: 4/5)

	Recorder: 86905f8b5f2848218360a3424fbb01b9

		Model: {'id': '86905f8b5f2848218360a3424fbb01b9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.095, 'Rank IC': 0.016, 'Rank ICIR': 0.12}, 'data_train_vec': ['2021-05-18', '2025-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.120', 'weight': '0.040'}

	Recorder: b9f59ea1f14a47ff964bf266a1ab6aa1

		Model: {'id': 'b9f59ea1f14a47ff964bf266a1ab6aa1', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.059, 'Rank IC': 0.014, 'Rank ICIR': 0.09}, 'data_train_vec': ['2022-05-18', '2025-05-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.090', 'weight': '0.030'}

	Recorder: de1b6b34e21b40cf9e15d10d80173bd6

		Model: {'id': 'de1b6b34e21b40cf9e15d10d80173bd6', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.092, 'Rank IC': 0.023, 'Rank ICIR': 0.147}, 'data_train_vec': ['2023-05-18', '2025-08-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.147', 'weight': '0.049'}

	Recorder: 19d3c725a4e648cc88470402a5cdaa9e

		Model: {'id': '19d3c725a4e648cc88470402a5cdaa9e', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.272, 'Rank IC': 0.039, 'Rank ICIR': 0.232}, 'data_train_vec': ['2025-05-18', '2026-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.232', 'weight': '0.078'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260518_18 949639799946767704 (Recorders: 3/5)

	Recorder: 85ef1b2bb4004b67aef08d64f734a0a1

		Model: {'id': '85ef1b2bb4004b67aef08d64f734a0a1', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.143, 'Rank IC': 0.026, 'Rank ICIR': 0.203}, 'data_train_vec': ['2023-05-18', '2025-08-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.203', 'weight': '0.068'}

	Recorder: e4cb2cd268d0486aa3a9939f73170977

		Model: {'id': 'e4cb2cd268d0486aa3a9939f73170977', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.114, 'Rank IC': 0.003, 'Rank ICIR': 0.034}, 'data_train_vec': ['2024-05-18', '2025-11-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.034', 'weight': '0.011'}

	Recorder: 537348b0d0cd4273953891b755aeadfd

		Model: {'id': '537348b0d0cd4273953891b755aeadfd', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.095, 'ICIR': 0.595, 'Rank IC': 0.048, 'Rank ICIR': 0.277}, 'data_train_vec': ['2025-05-18', '2026-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.277', 'weight': '0.093'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260518_16 635287619570894227 (Recorders: 3/5)

	Recorder: 682ab5a0776a41f78dfc90a36359a261

		Model: {'id': '682ab5a0776a41f78dfc90a36359a261', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.014, 'Rank IC': 0.031, 'Rank ICIR': 0.169}, 'data_train_vec': ['2022-05-18', '2025-05-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.169', 'weight': '0.057'}

	Recorder: 8f81db0b21eb42e4833b2800d90303da

		Model: {'id': '8f81db0b21eb42e4833b2800d90303da', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.115, 'Rank IC': 0.036, 'Rank ICIR': 0.228}, 'data_train_vec': ['2023-05-18', '2025-08-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.228', 'weight': '0.077'}

	Recorder: 40832a8dcc1247b2af43553be9fb3d02

		Model: {'id': '40832a8dcc1247b2af43553be9fb3d02', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.065, 'ICIR': 0.389, 'Rank IC': 0.03, 'Rank ICIR': 0.172}, 'data_train_vec': ['2025-05-18', '2026-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.172', 'weight': '0.058'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260518_16 595593818584997126 (Recorders: 4/5)

	Recorder: a0172017d98748aa9fcd6162640ef097

		Model: {'id': 'a0172017d98748aa9fcd6162640ef097', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.035, 'Rank IC': 0.027, 'Rank ICIR': 0.241}, 'data_train_vec': ['2021-05-18', '2025-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.241', 'weight': '0.081'}

	Recorder: a4bc3341e0814b03a9fea54afa153732

		Model: {'id': 'a4bc3341e0814b03a9fea54afa153732', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.071, 'Rank IC': 0.034, 'Rank ICIR': 0.304}, 'data_train_vec': ['2023-05-18', '2025-08-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.304', 'weight': '0.102'}

	Recorder: 46bb0d43a1224184b733f50614a9cb30

		Model: {'id': '46bb0d43a1224184b733f50614a9cb30', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.04, 'Rank IC': 0.015, 'Rank ICIR': 0.132}, 'data_train_vec': ['2024-05-18', '2025-11-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.132', 'weight': '0.044'}

	Recorder: a60ad87426b84d4d9b37853978ee7a12

		Model: {'id': 'a60ad87426b84d4d9b37853978ee7a12', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.069, 'ICIR': 0.485, 'Rank IC': 0.043, 'Rank ICIR': 0.265}, 'data_train_vec': ['2025-05-18', '2026-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.265', 'weight': '0.089'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260518_15 624669771853458397 (Recorders: 2/5)

	Recorder: 79b5da9c1ec14f04ad70bf15db809a33

		Model: {'id': '79b5da9c1ec14f04ad70bf15db809a33', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.082, 'Rank IC': 0.027, 'Rank ICIR': 0.169}, 'data_train_vec': ['2023-05-18', '2025-08-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.169', 'weight': '0.057'}

	Recorder: 940b47b9f31c4263990fff88336b75f3

		Model: {'id': '940b47b9f31c4263990fff88336b75f3', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.217, 'Rank IC': 0.031, 'Rank ICIR': 0.187}, 'data_train_vec': ['2025-05-18', '2026-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.187', 'weight': '0.063'}
