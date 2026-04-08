# params 
 {'predict_dates': [{'start': '2026-04-08', 'end': '2026-04-08'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260408_15 248244008953586305 (Recorders: 3/5)

	Recorder: 52d29797f9f34a85bbdb13ffe5f86dad

		Model: {'id': '52d29797f9f34a85bbdb13ffe5f86dad', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.141, 'Rank IC': 0.045, 'Rank ICIR': 0.285}, 'data_train_vec': ['2023-04-08', '2025-07-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.285', 'weight': '0.082'}

	Recorder: f68a395f39284f8f9302c834ca2ca4fa

		Model: {'id': 'f68a395f39284f8f9302c834ca2ca4fa', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.312, 'Rank IC': 0.035, 'Rank ICIR': 0.296}, 'data_train_vec': ['2024-04-08', '2025-10-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.296', 'weight': '0.086'}

	Recorder: f6ae599bee744b6fa6db95d9c7efaea7

		Model: {'id': 'f6ae599bee744b6fa6db95d9c7efaea7', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.144, 'Rank IC': 0.011, 'Rank ICIR': 0.071}, 'data_train_vec': ['2025-04-08', '2026-01-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.071', 'weight': '0.021'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260408_15 386740022133625610 (Recorders: 1/5)

	Recorder: f567be4a73aa48fdb886b235a2418e32

		Model: {'id': 'f567be4a73aa48fdb886b235a2418e32', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.322, 'Rank IC': 0.037, 'Rank ICIR': 0.311}, 'data_train_vec': ['2024-04-08', '2025-10-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.311', 'weight': '0.090'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260408_13 198165851428394103 (Recorders: 4/5)

	Recorder: 7434c9a90f4c47368ee7ef3b0a539487

		Model: {'id': '7434c9a90f4c47368ee7ef3b0a539487', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.058, 'Rank IC': 0.028, 'Rank ICIR': 0.158}, 'data_train_vec': ['2021-04-08', '2025-01-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.158', 'weight': '0.046'}

	Recorder: 599afa8d5f4e43a5a038589c19f1d6fb

		Model: {'id': '599afa8d5f4e43a5a038589c19f1d6fb', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.001, 'ICIR': 0.006, 'Rank IC': 0.03, 'Rank ICIR': 0.169}, 'data_train_vec': ['2022-04-08', '2025-04-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.169', 'weight': '0.049'}

	Recorder: 7a551305b932475bac273f32402153d4

		Model: {'id': '7a551305b932475bac273f32402153d4', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.145, 'Rank IC': 0.057, 'Rank ICIR': 0.337}, 'data_train_vec': ['2023-04-08', '2025-07-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.337', 'weight': '0.098'}

	Recorder: c481e51c1e7b4eb19e3f6cc080584c5b

		Model: {'id': 'c481e51c1e7b4eb19e3f6cc080584c5b', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.38, 'Rank IC': 0.035, 'Rank ICIR': 0.332}, 'data_train_vec': ['2024-04-08', '2025-10-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.332', 'weight': '0.096'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260408_13 386868291115487617 (Recorders: 5/5)

	Recorder: 323305c910f54021bb1a6473ac84b333

		Model: {'id': '323305c910f54021bb1a6473ac84b333', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.111, 'Rank IC': 0.022, 'Rank ICIR': 0.183}, 'data_train_vec': ['2021-04-08', '2025-01-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.183', 'weight': '0.053'}

	Recorder: 829dc818529145e087aa9db04ab60362

		Model: {'id': '829dc818529145e087aa9db04ab60362', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.057, 'Rank IC': 0.025, 'Rank ICIR': 0.212}, 'data_train_vec': ['2022-04-08', '2025-04-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.212', 'weight': '0.061'}

	Recorder: 79acac9b19f0458caacd4e64c77346c4

		Model: {'id': '79acac9b19f0458caacd4e64c77346c4', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.153, 'Rank IC': 0.044, 'Rank ICIR': 0.38}, 'data_train_vec': ['2023-04-08', '2025-07-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.380', 'weight': '0.110'}

	Recorder: 789c4d96b1eb4cef8b5b502fa2cdbe1b

		Model: {'id': '789c4d96b1eb4cef8b5b502fa2cdbe1b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.067, 'Rank IC': 0.011, 'Rank ICIR': 0.092}, 'data_train_vec': ['2024-04-08', '2025-10-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.092', 'weight': '0.027'}

	Recorder: 8ce44aa7d01a4eb6b08c6b03173c386e

		Model: {'id': '8ce44aa7d01a4eb6b08c6b03173c386e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.07, 'Rank IC': 0.005, 'Rank ICIR': 0.029}, 'data_train_vec': ['2025-04-08', '2026-01-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.029', 'weight': '0.008'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260408_13 260121469224988276 (Recorders: 3/5)

	Recorder: 99c5312c70dc48bb89a0c0d687346067

		Model: {'id': '99c5312c70dc48bb89a0c0d687346067', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.088, 'Rank IC': 0.025, 'Rank ICIR': 0.141}, 'data_train_vec': ['2021-04-08', '2025-01-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.141', 'weight': '0.041'}

	Recorder: 8da10174596e46afa0f3c5013c78b890

		Model: {'id': '8da10174596e46afa0f3c5013c78b890', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.035, 'Rank IC': 0.032, 'Rank ICIR': 0.189}, 'data_train_vec': ['2023-04-08', '2025-07-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.189', 'weight': '0.055'}

	Recorder: 7f62b555a8f745a69f3d7e0d6bee4ccc

		Model: {'id': '7f62b555a8f745a69f3d7e0d6bee4ccc', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.301, 'Rank IC': 0.031, 'Rank ICIR': 0.27}, 'data_train_vec': ['2024-04-08', '2025-10-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.270', 'weight': '0.078'}
