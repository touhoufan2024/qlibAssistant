# params 
 {'predict_dates': [{'start': '2026-04-02', 'end': '2026-04-02'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260402_16 393278720187928568 (Recorders: 4/5)

	Recorder: 6985f1eafad943198d1362299fad82d4

		Model: {'id': '6985f1eafad943198d1362299fad82d4', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.04, 'Rank IC': 0.033, 'Rank ICIR': 0.159}, 'data_train_vec': ['2021-04-02', '2025-01-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.159', 'weight': '0.041'}

	Recorder: 5b62d1eaea0c4841aada16ba62cf62e2

		Model: {'id': '5b62d1eaea0c4841aada16ba62cf62e2', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.278, 'Rank IC': 0.053, 'Rank ICIR': 0.327}, 'data_train_vec': ['2023-04-02', '2025-07-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.327', 'weight': '0.083'}

	Recorder: df3f25890f8d404d91a78762c25d0afb

		Model: {'id': 'df3f25890f8d404d91a78762c25d0afb', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.039, 'Rank IC': 0.04, 'Rank ICIR': 0.317}, 'data_train_vec': ['2024-04-02', '2025-10-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.317', 'weight': '0.081'}

	Recorder: 57cbb34bf2524e43b135d4140d7f657f

		Model: {'id': '57cbb34bf2524e43b135d4140d7f657f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.104, 'Rank IC': 0.002, 'Rank ICIR': 0.017}, 'data_train_vec': ['2025-04-02', '2026-01-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.017', 'weight': '0.004'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260402_16 815986043880766501 (Recorders: 3/5)

	Recorder: 59d3d91547424261bd70a21e36753045

		Model: {'id': '59d3d91547424261bd70a21e36753045', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.017, 'Rank IC': 0.024, 'Rank ICIR': 0.155}, 'data_train_vec': ['2021-04-02', '2025-01-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.155', 'weight': '0.040'}

	Recorder: 67773b8c697743ecb64e11a70571c096

		Model: {'id': '67773b8c697743ecb64e11a70571c096', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.037, 'Rank IC': 0.046, 'Rank ICIR': 0.267}, 'data_train_vec': ['2023-04-02', '2025-07-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.267', 'weight': '0.068'}

	Recorder: 566323ff9b8f484ca1001aef2ac62f37

		Model: {'id': '566323ff9b8f484ca1001aef2ac62f37', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.246, 'Rank IC': 0.04, 'Rank ICIR': 0.353}, 'data_train_vec': ['2024-04-02', '2025-10-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.353', 'weight': '0.090'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260402_14 607040263094609924 (Recorders: 4/5)

	Recorder: c4a2650a98bd425da2b08f51e40331b5

		Model: {'id': 'c4a2650a98bd425da2b08f51e40331b5', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.121, 'Rank IC': 0.041, 'Rank ICIR': 0.224}, 'data_train_vec': ['2021-04-02', '2025-01-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.224', 'weight': '0.057'}

	Recorder: 7724fbd16f3d4aecbc4e336d55330b32

		Model: {'id': '7724fbd16f3d4aecbc4e336d55330b32', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.025, 'Rank IC': 0.029, 'Rank ICIR': 0.163}, 'data_train_vec': ['2022-04-02', '2025-04-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.163', 'weight': '0.042'}

	Recorder: 86980d8581f042838e54adab912de45f

		Model: {'id': '86980d8581f042838e54adab912de45f', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.108, 'Rank IC': 0.053, 'Rank ICIR': 0.305}, 'data_train_vec': ['2023-04-02', '2025-07-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.305', 'weight': '0.078'}

	Recorder: 888b86affcb64b8ca71cd2eb9cafe645

		Model: {'id': '888b86affcb64b8ca71cd2eb9cafe645', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.212, 'Rank IC': 0.035, 'Rank ICIR': 0.333}, 'data_train_vec': ['2024-04-02', '2025-10-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.333', 'weight': '0.085'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260402_13 453622501940986476 (Recorders: 3/5)

	Recorder: b7f896b3afb04912a6922ca6e87c7b40

		Model: {'id': 'b7f896b3afb04912a6922ca6e87c7b40', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.107, 'Rank IC': 0.024, 'Rank ICIR': 0.193}, 'data_train_vec': ['2021-04-02', '2025-01-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.193', 'weight': '0.049'}

	Recorder: 34b602f0b6d7490195dbbb5d9cba6a55

		Model: {'id': '34b602f0b6d7490195dbbb5d9cba6a55', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.03, 'Rank IC': 0.021, 'Rank ICIR': 0.178}, 'data_train_vec': ['2022-04-02', '2025-04-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.178', 'weight': '0.045'}

	Recorder: 40fc9415411045b99c86d17a06884ddf

		Model: {'id': '40fc9415411045b99c86d17a06884ddf', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.113, 'Rank IC': 0.039, 'Rank ICIR': 0.327}, 'data_train_vec': ['2023-04-02', '2025-07-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.327', 'weight': '0.083'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260402_13 374407975450350326 (Recorders: 4/5)

	Recorder: 3eda21f786e047df82fb34f5677c0d7c

		Model: {'id': '3eda21f786e047df82fb34f5677c0d7c', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.064, 'Rank IC': 0.03, 'Rank ICIR': 0.16}, 'data_train_vec': ['2021-04-02', '2025-01-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.160', 'weight': '0.041'}

	Recorder: d3f9f529c5004a24b8ec66be0a6daead

		Model: {'id': 'd3f9f529c5004a24b8ec66be0a6daead', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.018, 'Rank IC': 0.026, 'Rank ICIR': 0.15}, 'data_train_vec': ['2022-04-02', '2025-04-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.150', 'weight': '0.038'}

	Recorder: 34dbbe28587f4d50828a9cb6c0bfb042

		Model: {'id': '34dbbe28587f4d50828a9cb6c0bfb042', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.043, 'Rank IC': 0.043, 'Rank ICIR': 0.252}, 'data_train_vec': ['2023-04-02', '2025-07-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.252', 'weight': '0.064'}

	Recorder: 3bfc427f14284f779ee6f0f35c1fae29

		Model: {'id': '3bfc427f14284f779ee6f0f35c1fae29', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.07, 'Rank IC': 0.005, 'Rank ICIR': 0.044}, 'data_train_vec': ['2025-04-02', '2026-01-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.044', 'weight': '0.011'}
