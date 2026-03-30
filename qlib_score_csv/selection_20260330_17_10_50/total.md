# params 
 {'predict_dates': [{'start': '2026-03-30', 'end': '2026-03-30'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260330_16 240504811409209159 (Recorders: 3/5)

	Recorder: 700206f8e6974c1a9b69c344e568a92d

		Model: {'id': '700206f8e6974c1a9b69c344e568a92d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.144, 'Rank IC': 0.044, 'Rank ICIR': 0.295}, 'data_train_vec': ['2021-03-30', '2024-12-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.295', 'weight': '0.068'}

	Recorder: d94160bfdf9b463588cd2f9cee207a9c

		Model: {'id': 'd94160bfdf9b463588cd2f9cee207a9c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.021, 'Rank IC': 0.04, 'Rank ICIR': 0.24}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.240', 'weight': '0.055'}

	Recorder: ae1b118238d3481bba21e4e56dd4255b

		Model: {'id': 'ae1b118238d3481bba21e4e56dd4255b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.137, 'Rank IC': 0.055, 'Rank ICIR': 0.367}, 'data_train_vec': ['2024-03-30', '2025-09-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.367', 'weight': '0.084'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260330_16 248544057112798415 (Recorders: 3/5)

	Recorder: 5a68d187206b45d6a9317212c1e72baf

		Model: {'id': '5a68d187206b45d6a9317212c1e72baf', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.024, 'Rank IC': 0.026, 'Rank ICIR': 0.163}, 'data_train_vec': ['2021-03-30', '2024-12-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.163', 'weight': '0.037'}

	Recorder: 2eef8f838c834825a35532ecc7103535

		Model: {'id': '2eef8f838c834825a35532ecc7103535', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.019, 'Rank IC': 0.036, 'Rank ICIR': 0.221}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.221', 'weight': '0.051'}

	Recorder: 03dd10d97f2c4cd8ae9533cb46187dad

		Model: {'id': '03dd10d97f2c4cd8ae9533cb46187dad', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.312, 'Rank IC': 0.048, 'Rank ICIR': 0.366}, 'data_train_vec': ['2024-03-30', '2025-09-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.366', 'weight': '0.084'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260330_14 553147958961298186 (Recorders: 4/5)

	Recorder: b9bb18a8df1148339143c125ef46c1f8

		Model: {'id': 'b9bb18a8df1148339143c125ef46c1f8', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.119, 'Rank IC': 0.037, 'Rank ICIR': 0.219}, 'data_train_vec': ['2021-03-30', '2024-12-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.219', 'weight': '0.050'}

	Recorder: b498fc6b91254dbebcef4b4291a7e9d6

		Model: {'id': 'b498fc6b91254dbebcef4b4291a7e9d6', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.001, 'ICIR': 0.006, 'Rank IC': 0.037, 'Rank ICIR': 0.216}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.216', 'weight': '0.050'}

	Recorder: 4c930bca586944eaa58516d27650c620

		Model: {'id': '4c930bca586944eaa58516d27650c620', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.334, 'Rank IC': 0.046, 'Rank ICIR': 0.398}, 'data_train_vec': ['2024-03-30', '2025-09-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.398', 'weight': '0.091'}

	Recorder: 2084e2c344ca419eb4dd77cf7ae96442

		Model: {'id': '2084e2c344ca419eb4dd77cf7ae96442', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.086, 'Rank IC': 0.023, 'Rank ICIR': 0.212}, 'data_train_vec': ['2025-03-28', '2025-12-27'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.212', 'weight': '0.049'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260330_14 287542138580794807 (Recorders: 5/5)

	Recorder: f5a6f3da733a4d0493e909b7e3d2e3fd

		Model: {'id': 'f5a6f3da733a4d0493e909b7e3d2e3fd', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.139, 'Rank IC': 0.027, 'Rank ICIR': 0.228}, 'data_train_vec': ['2021-03-30', '2024-12-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.228', 'weight': '0.052'}

	Recorder: 0f80ddba2eb74042b06dd385dd90842c

		Model: {'id': '0f80ddba2eb74042b06dd385dd90842c', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.024, 'Rank IC': 0.019, 'Rank ICIR': 0.168}, 'data_train_vec': ['2022-03-30', '2025-03-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.168', 'weight': '0.039'}

	Recorder: c300df2242734444b0ce440a10a5a465

		Model: {'id': 'c300df2242734444b0ce440a10a5a465', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.118, 'Rank IC': 0.037, 'Rank ICIR': 0.334}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.334', 'weight': '0.077'}

	Recorder: db41f7604ec94ca09664fa79382df7c1

		Model: {'id': 'db41f7604ec94ca09664fa79382df7c1', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.08, 'Rank IC': 0.012, 'Rank ICIR': 0.095}, 'data_train_vec': ['2024-03-30', '2025-09-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.095', 'weight': '0.022'}

	Recorder: cf0c4ffadd4542db8c3a34d119ada372

		Model: {'id': 'cf0c4ffadd4542db8c3a34d119ada372', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.134, 'Rank IC': 0.022, 'Rank ICIR': 0.194}, 'data_train_vec': ['2025-03-28', '2025-12-27'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.194', 'weight': '0.045'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260330_13 840704802559348849 (Recorders: 3/5)

	Recorder: 75763177fa3e4bac8021eb783d486b5b

		Model: {'id': '75763177fa3e4bac8021eb783d486b5b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.063, 'Rank IC': 0.038, 'Rank ICIR': 0.216}, 'data_train_vec': ['2021-03-30', '2024-12-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.216', 'weight': '0.050'}

	Recorder: e757f6b7e0f14f4aa153d925dd2937da

		Model: {'id': 'e757f6b7e0f14f4aa153d925dd2937da', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.019, 'Rank IC': 0.033, 'Rank ICIR': 0.199}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.199', 'weight': '0.046'}

	Recorder: c4af89ccae7345248370d4ac4fc3370a

		Model: {'id': 'c4af89ccae7345248370d4ac4fc3370a', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.071, 'Rank IC': 0.024, 'Rank ICIR': 0.22}, 'data_train_vec': ['2024-03-30', '2025-09-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.220', 'weight': '0.051'}
