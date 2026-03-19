# params 
 {'predict_dates': [{'start': '2026-03-18', 'end': '2026-03-18'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260318_14 516731099797649493 (Recorders: 3/5)

	Recorder: 323d51ab782b4868833085be70340cf4

		Model: {'id': '323d51ab782b4868833085be70340cf4', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.028, 'Rank IC': 0.023, 'Rank ICIR': 0.111}, 'data_train_vec': ['2021-03-18', '2024-12-17'], 'train_time_vec': ['2026-03-18', '2026-03-18'], 'rank_icir': '0.111', 'weight': '0.023'}

	Recorder: bb64450c6b6f4844aa1bf4ac370239c7

		Model: {'id': 'bb64450c6b6f4844aa1bf4ac370239c7', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.044, 'Rank IC': 0.02, 'Rank ICIR': 0.11}, 'data_train_vec': ['2024-03-18', '2025-09-17'], 'train_time_vec': ['2026-03-18', '2026-03-18'], 'rank_icir': '0.110', 'weight': '0.022'}

	Recorder: 3fad4284aeb747f5b24a56abdb340c23

		Model: {'id': '3fad4284aeb747f5b24a56abdb340c23', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.142, 'Rank IC': 0.111, 'Rank ICIR': 0.786}, 'data_train_vec': ['2025-03-18', '2025-12-17'], 'train_time_vec': ['2026-03-18', '2026-03-18'], 'rank_icir': '0.786', 'weight': '0.159'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260318_14 774368643167601611 (Recorders: 2/5)

	Recorder: 7b75a1385dab49e8ba8062c8425fffab

		Model: {'id': '7b75a1385dab49e8ba8062c8425fffab', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.262, 'Rank IC': 0.046, 'Rank ICIR': 0.346}, 'data_train_vec': ['2024-03-18', '2025-09-17'], 'train_time_vec': ['2026-03-18', '2026-03-18'], 'rank_icir': '0.346', 'weight': '0.070'}

	Recorder: 5cea6d35a87f410e996f1c703f2bfb00

		Model: {'id': '5cea6d35a87f410e996f1c703f2bfb00', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.123, 'Rank IC': 0.046, 'Rank ICIR': 0.421}, 'data_train_vec': ['2025-03-18', '2025-12-17'], 'train_time_vec': ['2026-03-18', '2026-03-18'], 'rank_icir': '0.421', 'weight': '0.085'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260318_11 815733234952482590 (Recorders: 4/5)

	Recorder: 5043eb070b6e4c68b8a14d6c723782d0

		Model: {'id': '5043eb070b6e4c68b8a14d6c723782d0', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.072, 'Rank IC': 0.03, 'Rank ICIR': 0.175}, 'data_train_vec': ['2021-03-18', '2024-12-17'], 'train_time_vec': ['2026-03-18', '2026-03-18'], 'rank_icir': '0.175', 'weight': '0.035'}

	Recorder: ac3e679343124265928f7101deab724d

		Model: {'id': 'ac3e679343124265928f7101deab724d', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.02, 'Rank IC': 0.023, 'Rank ICIR': 0.124}, 'data_train_vec': ['2022-03-18', '2025-03-17'], 'train_time_vec': ['2026-03-18', '2026-03-18'], 'rank_icir': '0.124', 'weight': '0.025'}

	Recorder: dcab44e08b96427a8c9475fcb76f90c6

		Model: {'id': 'dcab44e08b96427a8c9475fcb76f90c6', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.247, 'Rank IC': 0.036, 'Rank ICIR': 0.338}, 'data_train_vec': ['2024-03-18', '2025-09-17'], 'train_time_vec': ['2026-03-18', '2026-03-18'], 'rank_icir': '0.338', 'weight': '0.069'}

	Recorder: e04f5412e8c241a09c8d2fb511e654a9

		Model: {'id': 'e04f5412e8c241a09c8d2fb511e654a9', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.149, 'Rank IC': 0.036, 'Rank ICIR': 0.375}, 'data_train_vec': ['2025-03-18', '2025-12-17'], 'train_time_vec': ['2026-03-18', '2026-03-18'], 'rank_icir': '0.375', 'weight': '0.076'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260318_11 583681018094443169 (Recorders: 5/5)

	Recorder: 9a4e4aca35d347ffbd3b24372b8218be

		Model: {'id': '9a4e4aca35d347ffbd3b24372b8218be', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.136, 'Rank IC': 0.023, 'Rank ICIR': 0.204}, 'data_train_vec': ['2021-03-18', '2024-12-17'], 'train_time_vec': ['2026-03-18', '2026-03-18'], 'rank_icir': '0.204', 'weight': '0.041'}

	Recorder: 5acb79b1a5444d619202d2f4eb2a39ba

		Model: {'id': '5acb79b1a5444d619202d2f4eb2a39ba', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.122, 'Rank IC': 0.024, 'Rank ICIR': 0.205}, 'data_train_vec': ['2022-03-18', '2025-03-17'], 'train_time_vec': ['2026-03-18', '2026-03-18'], 'rank_icir': '0.205', 'weight': '0.042'}

	Recorder: 79f757f7c32d4c6aa42fcd91c75051bb

		Model: {'id': '79f757f7c32d4c6aa42fcd91c75051bb', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.106, 'Rank IC': 0.033, 'Rank ICIR': 0.282}, 'data_train_vec': ['2023-03-18', '2025-06-17'], 'train_time_vec': ['2026-03-18', '2026-03-18'], 'rank_icir': '0.282', 'weight': '0.057'}

	Recorder: ea5db9a2e7144e54b97822aa874bca40

		Model: {'id': 'ea5db9a2e7144e54b97822aa874bca40', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.15, 'Rank IC': 0.016, 'Rank ICIR': 0.151}, 'data_train_vec': ['2024-03-18', '2025-09-17'], 'train_time_vec': ['2026-03-18', '2026-03-18'], 'rank_icir': '0.151', 'weight': '0.031'}

	Recorder: 2b37e4c2b8d94317b36cd4234b395d15

		Model: {'id': '2b37e4c2b8d94317b36cd4234b395d15', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.322, 'Rank IC': 0.045, 'Rank ICIR': 0.452}, 'data_train_vec': ['2025-03-18', '2025-12-17'], 'train_time_vec': ['2026-03-18', '2026-03-18'], 'rank_icir': '0.452', 'weight': '0.092'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260318_11 316698524547875216 (Recorders: 3/5)

	Recorder: aa7ba1c7858244369bd69ef5eb88c489

		Model: {'id': 'aa7ba1c7858244369bd69ef5eb88c489', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.017, 'Rank IC': 0.022, 'Rank ICIR': 0.121}, 'data_train_vec': ['2021-03-18', '2024-12-17'], 'train_time_vec': ['2026-03-18', '2026-03-18'], 'rank_icir': '0.121', 'weight': '0.025'}

	Recorder: e615ba6484b14210925abc3945d296ae

		Model: {'id': 'e615ba6484b14210925abc3945d296ae', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.244, 'Rank IC': 0.028, 'Rank ICIR': 0.229}, 'data_train_vec': ['2024-03-18', '2025-09-17'], 'train_time_vec': ['2026-03-18', '2026-03-18'], 'rank_icir': '0.229', 'weight': '0.046'}

	Recorder: 58c5c13946c44ca393e6dd4c2bff5600

		Model: {'id': '58c5c13946c44ca393e6dd4c2bff5600', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.315, 'Rank IC': 0.054, 'Rank ICIR': 0.502}, 'data_train_vec': ['2025-03-18', '2025-12-17'], 'train_time_vec': ['2026-03-18', '2026-03-18'], 'rank_icir': '0.502', 'weight': '0.102'}
