# params 
 {'predict_dates': [{'start': '2026-03-06', 'end': '2026-03-06'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'stock_list': ['SH601699', 'SH601318'], 'model_filter': ['.*'], 'rec_filter': None}



 # model info 

Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260306_01 342661914672456904 (Recorders: 5/5)

	Recorder: afe431228f7f4fff8912d62cf5a21a46

		Model: {'id': 'afe431228f7f4fff8912d62cf5a21a46', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.038, 'Rank IC': 0.023, 'Rank ICIR': 0.134}, 'data_train_vec': ['2021-03-06', '2024-12-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}

	Recorder: 28b9609831da4e868cb67251dbee2c5f

		Model: {'id': '28b9609831da4e868cb67251dbee2c5f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': -0.003, 'ICIR': -0.022, 'Rank IC': 0.019, 'Rank ICIR': 0.107}, 'data_train_vec': ['2022-03-06', '2025-03-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}

	Recorder: 3918c8537e994d5fbff6470338243e96

		Model: {'id': '3918c8537e994d5fbff6470338243e96', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': -0.028, 'ICIR': -0.197, 'Rank IC': -0.002, 'Rank ICIR': -0.01}, 'data_train_vec': ['2023-03-06', '2025-06-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}

	Recorder: 10c497d5b7fb4f9ab075b67eb1635b45

		Model: {'id': '10c497d5b7fb4f9ab075b67eb1635b45', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': -0.012, 'ICIR': -0.124, 'Rank IC': 0.005, 'Rank ICIR': 0.041}, 'data_train_vec': ['2024-03-06', '2025-09-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}

	Recorder: 01fcbaafb2ea4473aeae6e9fc721eab2

		Model: {'id': '01fcbaafb2ea4473aeae6e9fc721eab2', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.06, 'ICIR': 0.385, 'Rank IC': 0.061, 'Rank ICIR': 0.517}, 'data_train_vec': ['2025-03-06', '2025-12-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260306_00 485477480125775998 (Recorders: 5/5)

	Recorder: d7a26e49646147479bbb316775adaa89

		Model: {'id': 'd7a26e49646147479bbb316775adaa89', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.084, 'Rank IC': 0.03, 'Rank ICIR': 0.17}, 'data_train_vec': ['2021-03-06', '2024-12-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}

	Recorder: e393494973fe428e8305807651654014

		Model: {'id': 'e393494973fe428e8305807651654014', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': -0.005, 'ICIR': -0.028, 'Rank IC': 0.019, 'Rank ICIR': 0.103}, 'data_train_vec': ['2022-03-06', '2025-03-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}

	Recorder: 2701efff498d4ae8a8fa9b80ea7445c9

		Model: {'id': '2701efff498d4ae8a8fa9b80ea7445c9', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': -0.032, 'ICIR': -0.195, 'Rank IC': 0.0, 'Rank ICIR': 0.0}, 'data_train_vec': ['2023-03-06', '2025-06-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}

	Recorder: ea6c7dd4bf8640feab87ffbe456324a5

		Model: {'id': 'ea6c7dd4bf8640feab87ffbe456324a5', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.137, 'Rank IC': 0.021, 'Rank ICIR': 0.171}, 'data_train_vec': ['2024-03-06', '2025-09-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}

	Recorder: d896f49b7c2e4e868cf9a6ccc883d65f

		Model: {'id': 'd896f49b7c2e4e868cf9a6ccc883d65f', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.085, 'ICIR': 0.629, 'Rank IC': 0.087, 'Rank ICIR': 0.76}, 'data_train_vec': ['2025-03-06', '2025-12-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260306_00 101920508972497825 (Recorders: 5/5)

	Recorder: 5c3fb6342c0543459c378e733aab6ea9

		Model: {'id': '5c3fb6342c0543459c378e733aab6ea9', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.105, 'Rank IC': 0.015, 'Rank ICIR': 0.106}, 'data_train_vec': ['2021-03-06', '2024-12-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}

	Recorder: acdf3da5d71e4d2d82cbcbfef7e072a2

		Model: {'id': 'acdf3da5d71e4d2d82cbcbfef7e072a2', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.126, 'Rank IC': 0.02, 'Rank ICIR': 0.164}, 'data_train_vec': ['2022-03-06', '2025-03-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}

	Recorder: 969987f754694c8b8934435b3d683f01

		Model: {'id': '969987f754694c8b8934435b3d683f01', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.126, 'Rank IC': 0.018, 'Rank ICIR': 0.131}, 'data_train_vec': ['2023-03-06', '2025-06-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}

	Recorder: 95b5a892e42e46d59063c1e69443f30b

		Model: {'id': '95b5a892e42e46d59063c1e69443f30b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.261, 'Rank IC': 0.028, 'Rank ICIR': 0.238}, 'data_train_vec': ['2024-03-06', '2025-09-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}

	Recorder: 4de064229362492aa7ee8f9da71828ec

		Model: {'id': '4de064229362492aa7ee8f9da71828ec', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.06, 'ICIR': 0.606, 'Rank IC': 0.052, 'Rank ICIR': 0.745}, 'data_train_vec': ['2025-03-06', '2025-12-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260306_00 544399067649578239 (Recorders: 5/5)

	Recorder: 911f7a051c4541a18d345fbe5b1833f1

		Model: {'id': '911f7a051c4541a18d345fbe5b1833f1', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.088, 'Rank IC': 0.027, 'Rank ICIR': 0.147}, 'data_train_vec': ['2021-03-06', '2024-12-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}

	Recorder: 4e0e698495d64605942da15214f5fda9

		Model: {'id': '4e0e698495d64605942da15214f5fda9', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.0, 'ICIR': 0.002, 'Rank IC': 0.019, 'Rank ICIR': 0.097}, 'data_train_vec': ['2022-03-06', '2025-03-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}

	Recorder: a9e8f4fb5fbb4befb3737454a16d748e

		Model: {'id': 'a9e8f4fb5fbb4befb3737454a16d748e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': -0.035, 'ICIR': -0.242, 'Rank IC': -0.007, 'Rank ICIR': -0.037}, 'data_train_vec': ['2023-03-06', '2025-06-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}

	Recorder: 107411294dc54787b5107545effd8d1e

		Model: {'id': '107411294dc54787b5107545effd8d1e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': -0.001, 'ICIR': -0.009, 'Rank IC': -0.003, 'Rank ICIR': -0.024}, 'data_train_vec': ['2024-03-06', '2025-09-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}

	Recorder: e33097ed07de4cd59f1abd8b92e7018f

		Model: {'id': 'e33097ed07de4cd59f1abd8b92e7018f', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.084, 'Rank IC': 0.076, 'Rank ICIR': 0.566}, 'data_train_vec': ['2025-03-06', '2025-12-05'], 'train_time_vec': ['2026-03-05', '2026-03-05']}
