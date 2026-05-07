# params 
 {'predict_dates': [{'start': '2026-05-07', 'end': '2026-05-07'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260507_17 331245556098569164 (Recorders: 2/5)

	Recorder: 50df474c3f604608888aa0961a4c9947

		Model: {'id': '50df474c3f604608888aa0961a4c9947', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.055, 'Rank IC': 0.024, 'Rank ICIR': 0.179}, 'data_train_vec': ['2024-05-07', '2025-11-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.179', 'weight': '0.101'}

	Recorder: 7e6706ddb34f40ff99f1eef5e6908ba9

		Model: {'id': '7e6706ddb34f40ff99f1eef5e6908ba9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.438, 'Rank IC': 0.023, 'Rank ICIR': 0.183}, 'data_train_vec': ['2025-05-07', '2026-02-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.183', 'weight': '0.103'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260507_17 256764882836237673 (Recorders: 2/5)

	Recorder: d053ee126c254d97ac27f2d6d7fe34dc

		Model: {'id': 'd053ee126c254d97ac27f2d6d7fe34dc', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.239, 'Rank IC': 0.024, 'Rank ICIR': 0.199}, 'data_train_vec': ['2024-05-07', '2025-11-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.199', 'weight': '0.112'}

	Recorder: 0f6ca73583224c3ea38827b7393bf9b6

		Model: {'id': '0f6ca73583224c3ea38827b7393bf9b6', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.084, 'ICIR': 0.662, 'Rank IC': 0.035, 'Rank ICIR': 0.335}, 'data_train_vec': ['2025-05-07', '2026-02-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.335', 'weight': '0.189'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260507_14 192552018517345804 (Recorders: 3/5)

	Recorder: 49eaade77953479facf44af4bc3f043b

		Model: {'id': '49eaade77953479facf44af4bc3f043b', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.039, 'Rank IC': 0.034, 'Rank ICIR': 0.195}, 'data_train_vec': ['2023-05-07', '2025-08-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.195', 'weight': '0.110'}

	Recorder: 795d4ce24e824f1f8b3e5a7fdc12065a

		Model: {'id': '795d4ce24e824f1f8b3e5a7fdc12065a', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.09, 'Rank IC': 0.011, 'Rank ICIR': 0.092}, 'data_train_vec': ['2024-05-07', '2025-11-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.092', 'weight': '0.052'}

	Recorder: 16d19638c3e74605a4348a82beaeb8a0

		Model: {'id': '16d19638c3e74605a4348a82beaeb8a0', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.461, 'Rank IC': 0.019, 'Rank ICIR': 0.153}, 'data_train_vec': ['2025-05-07', '2026-02-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.153', 'weight': '0.086'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260507_14 654717485948422972 (Recorders: 2/5)

	Recorder: 8ecff858ed2540619a1fe414aa1ad034

		Model: {'id': '8ecff858ed2540619a1fe414aa1ad034', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.052, 'Rank IC': 0.017, 'Rank ICIR': 0.156}, 'data_train_vec': ['2024-05-07', '2025-11-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.156', 'weight': '0.088'}

	Recorder: ec009d27b14f4b0cba7c617b8dd700fe

		Model: {'id': 'ec009d27b14f4b0cba7c617b8dd700fe', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.563, 'Rank IC': 0.023, 'Rank ICIR': 0.2}, 'data_train_vec': ['2025-05-07', '2026-02-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.200', 'weight': '0.113'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260507_14 393448369421807719 (Recorders: 1/5)

	Recorder: 4ec3dcccb5c64cfbac909d928c7a276c

		Model: {'id': '4ec3dcccb5c64cfbac909d928c7a276c', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.401, 'Rank IC': 0.008, 'Rank ICIR': 0.081}, 'data_train_vec': ['2025-05-07', '2026-02-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.081', 'weight': '0.046'}
