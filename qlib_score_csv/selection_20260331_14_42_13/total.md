# params 
 {'predict_dates': [{'start': '2026-03-31', 'end': '2026-03-31'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260331_14 369569164089120150 (Recorders: 3/5)

	Recorder: beeae1c63a7a448f9ccced993fa4b0fb

		Model: {'id': 'beeae1c63a7a448f9ccced993fa4b0fb', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.105, 'Rank IC': 0.026, 'Rank ICIR': 0.173}, 'data_train_vec': ['2021-03-31', '2024-12-30'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.173', 'weight': '0.044'}

	Recorder: 8176ab0e50d94fe895d47af28922dd01

		Model: {'id': '8176ab0e50d94fe895d47af28922dd01', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.08, 'Rank IC': 0.048, 'Rank ICIR': 0.29}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.290', 'weight': '0.073'}

	Recorder: e549e3b1077e40d0bd5cda85150ae79a

		Model: {'id': 'e549e3b1077e40d0bd5cda85150ae79a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.056, 'Rank IC': 0.053, 'Rank ICIR': 0.378}, 'data_train_vec': ['2024-03-30', '2025-09-29'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.378', 'weight': '0.095'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260331_14 408532601023786446 (Recorders: 3/5)

	Recorder: 9cd1d8714de74267bf02f85d8f6e2528

		Model: {'id': '9cd1d8714de74267bf02f85d8f6e2528', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.011, 'Rank IC': 0.022, 'Rank ICIR': 0.141}, 'data_train_vec': ['2021-03-31', '2024-12-30'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.141', 'weight': '0.036'}

	Recorder: a1dd7596754f4723916c8dd03de4e431

		Model: {'id': 'a1dd7596754f4723916c8dd03de4e431', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.062, 'Rank IC': 0.043, 'Rank ICIR': 0.27}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.270', 'weight': '0.068'}

	Recorder: 437a690d770645e781ddabacc98b170b

		Model: {'id': '437a690d770645e781ddabacc98b170b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.303, 'Rank IC': 0.051, 'Rank ICIR': 0.383}, 'data_train_vec': ['2024-03-30', '2025-09-29'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.383', 'weight': '0.097'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260331_11 818328938496463856 (Recorders: 4/5)

	Recorder: d3f30638bf264421a9de9c9de8ba3d2f

		Model: {'id': 'd3f30638bf264421a9de9c9de8ba3d2f', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.122, 'Rank IC': 0.041, 'Rank ICIR': 0.227}, 'data_train_vec': ['2021-03-31', '2024-12-30'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.227', 'weight': '0.057'}

	Recorder: a965494b62514b5a90a3fc938ec3b3df

		Model: {'id': 'a965494b62514b5a90a3fc938ec3b3df', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.099, 'Rank IC': 0.05, 'Rank ICIR': 0.293}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.293', 'weight': '0.074'}

	Recorder: 4a86f64a80674106a89e1e27788f3297

		Model: {'id': '4a86f64a80674106a89e1e27788f3297', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.29, 'Rank IC': 0.042, 'Rank ICIR': 0.371}, 'data_train_vec': ['2024-03-30', '2025-09-29'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.371', 'weight': '0.094'}

	Recorder: 51be83adeb7b461bb76242af2ffa992f

		Model: {'id': '51be83adeb7b461bb76242af2ffa992f', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.021, 'Rank IC': 0.01, 'Rank ICIR': 0.093}, 'data_train_vec': ['2025-03-28', '2025-12-27'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.093', 'weight': '0.023'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260331_11 886871268014350939 (Recorders: 4/5)

	Recorder: 562efdd2392945b5b8b182931ccd4e08

		Model: {'id': '562efdd2392945b5b8b182931ccd4e08', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.143, 'Rank IC': 0.027, 'Rank ICIR': 0.229}, 'data_train_vec': ['2021-03-31', '2024-12-30'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.229', 'weight': '0.058'}

	Recorder: 88fa1e44ffaf4537a9fe0cf158f3f35a

		Model: {'id': '88fa1e44ffaf4537a9fe0cf158f3f35a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.037, 'Rank IC': 0.021, 'Rank ICIR': 0.184}, 'data_train_vec': ['2022-03-30', '2025-03-29'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.184', 'weight': '0.046'}

	Recorder: f10108592c86470783357c483d4dbe9f

		Model: {'id': 'f10108592c86470783357c483d4dbe9f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.156, 'Rank IC': 0.042, 'Rank ICIR': 0.388}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.388', 'weight': '0.098'}

	Recorder: 19a7218e848742f199223407fbd04a31

		Model: {'id': '19a7218e848742f199223407fbd04a31', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.043, 'Rank IC': 0.009, 'Rank ICIR': 0.072}, 'data_train_vec': ['2025-03-28', '2025-12-27'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.072', 'weight': '0.018'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260331_11 618269648857960541 (Recorders: 2/5)

	Recorder: 77dcd4a3d6ac4c29b55866afce836e1b

		Model: {'id': '77dcd4a3d6ac4c29b55866afce836e1b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.077, 'Rank IC': 0.038, 'Rank ICIR': 0.205}, 'data_train_vec': ['2021-03-31', '2024-12-30'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.205', 'weight': '0.052'}

	Recorder: 3e0f6de2f1414ddd8fc1abfa9556b4da

		Model: {'id': '3e0f6de2f1414ddd8fc1abfa9556b4da', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.077, 'Rank IC': 0.043, 'Rank ICIR': 0.263}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.263', 'weight': '0.066'}
