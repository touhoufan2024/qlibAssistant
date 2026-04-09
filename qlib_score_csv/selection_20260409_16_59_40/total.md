# params 
 {'predict_dates': [{'start': '2026-04-09', 'end': '2026-04-09'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260409_16 442678094956591924 (Recorders: 1/5)

	Recorder: 510a7a62a8134348afa5e8ab089a80b0

		Model: {'id': '510a7a62a8134348afa5e8ab089a80b0', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.233, 'Rank IC': 0.045, 'Rank ICIR': 0.29}, 'data_train_vec': ['2023-04-09', '2025-07-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.290', 'weight': '0.118'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260409_16 323416171342883501 (Recorders: 1/5)

	Recorder: f9cfae6562db484a9fdbf1ab6a8be096

		Model: {'id': 'f9cfae6562db484a9fdbf1ab6a8be096', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.251, 'Rank IC': 0.036, 'Rank ICIR': 0.313}, 'data_train_vec': ['2024-04-09', '2025-10-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.313', 'weight': '0.127'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260409_14 565495719036246609 (Recorders: 4/5)

	Recorder: 65eb0090b51a48f6a563af7ece17e32d

		Model: {'id': '65eb0090b51a48f6a563af7ece17e32d', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.054, 'Rank IC': 0.027, 'Rank ICIR': 0.151}, 'data_train_vec': ['2021-04-09', '2025-01-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.151', 'weight': '0.061'}

	Recorder: 3eddcaf7dfc14643a28158c01ed50bb6

		Model: {'id': '3eddcaf7dfc14643a28158c01ed50bb6', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.013, 'Rank IC': 0.03, 'Rank ICIR': 0.164}, 'data_train_vec': ['2022-04-09', '2025-04-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.164', 'weight': '0.067'}

	Recorder: f90961f121e940a893b63d88c13a7fa7

		Model: {'id': 'f90961f121e940a893b63d88c13a7fa7', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.115, 'Rank IC': 0.053, 'Rank ICIR': 0.304}, 'data_train_vec': ['2023-04-09', '2025-07-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.304', 'weight': '0.123'}

	Recorder: c093698bbb004a59acb24616f65b288e

		Model: {'id': 'c093698bbb004a59acb24616f65b288e', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.28, 'Rank IC': 0.034, 'Rank ICIR': 0.333}, 'data_train_vec': ['2024-04-09', '2025-10-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.333', 'weight': '0.135'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260409_14 812823378785123109 (Recorders: 5/5)

	Recorder: 2e950396dd0946b0997416691c63b867

		Model: {'id': '2e950396dd0946b0997416691c63b867', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.088, 'Rank IC': 0.019, 'Rank ICIR': 0.156}, 'data_train_vec': ['2021-04-09', '2025-01-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.156', 'weight': '0.063'}

	Recorder: 179287fc89b141c4bb03c9d2b1fb2add

		Model: {'id': '179287fc89b141c4bb03c9d2b1fb2add', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.012, 'Rank IC': 0.017, 'Rank ICIR': 0.147}, 'data_train_vec': ['2022-04-09', '2025-04-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.147', 'weight': '0.060'}

	Recorder: 7ab4dec42203460491f2efbb0dd7bc74

		Model: {'id': '7ab4dec42203460491f2efbb0dd7bc74', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.149, 'Rank IC': 0.042, 'Rank ICIR': 0.36}, 'data_train_vec': ['2023-04-09', '2025-07-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.360', 'weight': '0.146'}

	Recorder: 66ff0bfe75af4f09bfb5efe4d1bc9189

		Model: {'id': '66ff0bfe75af4f09bfb5efe4d1bc9189', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.052, 'Rank IC': 0.011, 'Rank ICIR': 0.087}, 'data_train_vec': ['2024-04-09', '2025-10-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.087', 'weight': '0.035'}

	Recorder: e1799b031ecb4733a249c9b4bfd968ce

		Model: {'id': 'e1799b031ecb4733a249c9b4bfd968ce', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.078, 'Rank IC': 0.006, 'Rank ICIR': 0.046}, 'data_train_vec': ['2025-04-09', '2026-01-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.046', 'weight': '0.019'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260409_14 594066583939261587 (Recorders: 1/5)

	Recorder: e79780d7cbf74eca99e5dc1f73d9055a

		Model: {'id': 'e79780d7cbf74eca99e5dc1f73d9055a', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.032, 'Rank IC': 0.021, 'Rank ICIR': 0.112}, 'data_train_vec': ['2021-04-09', '2025-01-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.112', 'weight': '0.045'}
