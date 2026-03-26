# params 
 {'predict_dates': [{'start': '2026-03-26', 'end': '2026-03-26'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260326_14 878061782558740633 (Recorders: 3/5)

	Recorder: d4f7c9b52a8f43f9ba82c7770b26ae66

		Model: {'id': 'd4f7c9b52a8f43f9ba82c7770b26ae66', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.124, 'Rank IC': 0.026, 'Rank ICIR': 0.215}, 'data_train_vec': ['2021-03-26', '2024-12-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.215', 'weight': '0.047'}

	Recorder: 0da3fc42bda147a389cf446fac48b173

		Model: {'id': '0da3fc42bda147a389cf446fac48b173', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.213, 'Rank IC': 0.022, 'Rank ICIR': 0.183}, 'data_train_vec': ['2024-03-26', '2025-09-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.183', 'weight': '0.040'}

	Recorder: d9db5f4e984548c09ad2f72789181c36

		Model: {'id': 'd9db5f4e984548c09ad2f72789181c36', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.215, 'Rank IC': 0.045, 'Rank ICIR': 0.352}, 'data_train_vec': ['2025-03-26', '2025-12-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.352', 'weight': '0.076'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260326_14 104412098645274656 (Recorders: 2/5)

	Recorder: 422e8206ce9245bea252f06718c5c74b

		Model: {'id': '422e8206ce9245bea252f06718c5c74b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.059, 'Rank IC': 0.029, 'Rank ICIR': 0.196}, 'data_train_vec': ['2021-03-26', '2024-12-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.196', 'weight': '0.042'}

	Recorder: 495376903ff84fe08231b4e31a4147bd

		Model: {'id': '495376903ff84fe08231b4e31a4147bd', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.391, 'Rank IC': 0.057, 'Rank ICIR': 0.482}, 'data_train_vec': ['2024-03-26', '2025-09-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.482', 'weight': '0.104'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260326_12 374457964106543470 (Recorders: 3/5)

	Recorder: 60204b00e1f741b8bf9983126148e761

		Model: {'id': '60204b00e1f741b8bf9983126148e761', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.11, 'Rank IC': 0.037, 'Rank ICIR': 0.211}, 'data_train_vec': ['2021-03-26', '2024-12-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.211', 'weight': '0.046'}

	Recorder: 4bb207799bd34b09a6de024816cf5c4f

		Model: {'id': '4bb207799bd34b09a6de024816cf5c4f', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.341, 'Rank IC': 0.045, 'Rank ICIR': 0.363}, 'data_train_vec': ['2024-03-26', '2025-09-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.363', 'weight': '0.079'}

	Recorder: 78da0b6769294b0d86a65c31b4713937

		Model: {'id': '78da0b6769294b0d86a65c31b4713937', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.163, 'Rank IC': 0.036, 'Rank ICIR': 0.306}, 'data_train_vec': ['2025-03-26', '2025-12-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.306', 'weight': '0.066'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260326_12 582563462120050783 (Recorders: 5/5)

	Recorder: 1857ed69ca5f485abd2bac334082ba39

		Model: {'id': '1857ed69ca5f485abd2bac334082ba39', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.183, 'Rank IC': 0.029, 'Rank ICIR': 0.251}, 'data_train_vec': ['2021-03-26', '2024-12-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.251', 'weight': '0.054'}

	Recorder: f87be69938c2409b9c221bba00f910d7

		Model: {'id': 'f87be69938c2409b9c221bba00f910d7', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.047, 'Rank IC': 0.021, 'Rank ICIR': 0.181}, 'data_train_vec': ['2022-03-26', '2025-03-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.181', 'weight': '0.039'}

	Recorder: e2bf3756edea4716b7631e3852531cf6

		Model: {'id': 'e2bf3756edea4716b7631e3852531cf6', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.149, 'Rank IC': 0.04, 'Rank ICIR': 0.362}, 'data_train_vec': ['2023-03-26', '2025-06-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.362', 'weight': '0.078'}

	Recorder: deeb6d16db5341faa0b1a912bf07fae7

		Model: {'id': 'deeb6d16db5341faa0b1a912bf07fae7', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.118, 'Rank IC': 0.022, 'Rank ICIR': 0.174}, 'data_train_vec': ['2024-03-26', '2025-09-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.174', 'weight': '0.038'}

	Recorder: f65c7ddb139c4e7fa86371e83cfa1abc

		Model: {'id': 'f65c7ddb139c4e7fa86371e83cfa1abc', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.151, 'Rank IC': 0.026, 'Rank ICIR': 0.246}, 'data_train_vec': ['2025-03-26', '2025-12-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.246', 'weight': '0.053'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260326_12 462627966980708185 (Recorders: 3/5)

	Recorder: 50408329e0e14e4fae56086f100fb0b6

		Model: {'id': '50408329e0e14e4fae56086f100fb0b6', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.043, 'Rank IC': 0.03, 'Rank ICIR': 0.159}, 'data_train_vec': ['2021-03-26', '2024-12-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.159', 'weight': '0.034'}

	Recorder: 8adb6ccc3a544aeb9f0c2bec9c3a69e8

		Model: {'id': '8adb6ccc3a544aeb9f0c2bec9c3a69e8', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.015, 'Rank IC': 0.051, 'Rank ICIR': 0.424}, 'data_train_vec': ['2024-03-26', '2025-09-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.424', 'weight': '0.092'}

	Recorder: 106f16210c114745bf11d3acadfc4335

		Model: {'id': '106f16210c114745bf11d3acadfc4335', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.257, 'Rank IC': 0.046, 'Rank ICIR': 0.514}, 'data_train_vec': ['2025-03-26', '2025-12-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.514', 'weight': '0.111'}
