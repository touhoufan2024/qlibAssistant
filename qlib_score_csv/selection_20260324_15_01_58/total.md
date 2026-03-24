# params 
 {'predict_dates': [{'start': '2026-03-24', 'end': '2026-03-24'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260324_14 771465771593798514 (Recorders: 3/5)

	Recorder: a363d9094f4d4abdb76077999b0c76cd

		Model: {'id': 'a363d9094f4d4abdb76077999b0c76cd', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.035, 'Rank IC': 0.029, 'Rank ICIR': 0.172}, 'data_train_vec': ['2021-03-24', '2024-12-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.172', 'weight': '0.042'}

	Recorder: 6b9a3b9a58624b729d18145635af30a9

		Model: {'id': '6b9a3b9a58624b729d18145635af30a9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.101, 'Rank IC': 0.04, 'Rank ICIR': 0.296}, 'data_train_vec': ['2024-03-24', '2025-09-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.296', 'weight': '0.071'}

	Recorder: 04f9bab7c4da45fb9b54a3baa10b251a

		Model: {'id': '04f9bab7c4da45fb9b54a3baa10b251a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.018, 'Rank IC': 0.031, 'Rank ICIR': 0.255}, 'data_train_vec': ['2025-03-24', '2025-12-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.255', 'weight': '0.062'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260324_14 844125136448859464 (Recorders: 2/5)

	Recorder: 60f7f7df5c124258ae29810a0decccff

		Model: {'id': '60f7f7df5c124258ae29810a0decccff', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.057, 'Rank IC': 0.024, 'Rank ICIR': 0.187}, 'data_train_vec': ['2021-03-24', '2024-12-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.187', 'weight': '0.045'}

	Recorder: c5df6c3343974a8c88d08536c003b132

		Model: {'id': 'c5df6c3343974a8c88d08536c003b132', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.348, 'Rank IC': 0.045, 'Rank ICIR': 0.413}, 'data_train_vec': ['2024-03-24', '2025-09-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.413', 'weight': '0.100'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260324_12 473441935372306177 (Recorders: 2/5)

	Recorder: ed5c837f2e7c4a00869c6db15444559c

		Model: {'id': 'ed5c837f2e7c4a00869c6db15444559c', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.11, 'Rank IC': 0.038, 'Rank ICIR': 0.215}, 'data_train_vec': ['2021-03-24', '2024-12-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.215', 'weight': '0.052'}

	Recorder: 61f2aef84ad640c8aa072a5060bc5de2

		Model: {'id': '61f2aef84ad640c8aa072a5060bc5de2', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.342, 'Rank IC': 0.044, 'Rank ICIR': 0.362}, 'data_train_vec': ['2024-03-24', '2025-09-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.362', 'weight': '0.087'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260324_11 630249235309421598 (Recorders: 5/5)

	Recorder: e59e647a259b46f5ab9df651b60335ba

		Model: {'id': 'e59e647a259b46f5ab9df651b60335ba', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.168, 'Rank IC': 0.027, 'Rank ICIR': 0.235}, 'data_train_vec': ['2021-03-24', '2024-12-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.235', 'weight': '0.057'}

	Recorder: 628e75ba58f74a7bb08a75c7ebad2afd

		Model: {'id': '628e75ba58f74a7bb08a75c7ebad2afd', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.054, 'Rank IC': 0.02, 'Rank ICIR': 0.178}, 'data_train_vec': ['2022-03-24', '2025-03-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.178', 'weight': '0.043'}

	Recorder: 7c3c84b9d1e24ec1bf3b1fbb98e075fa

		Model: {'id': '7c3c84b9d1e24ec1bf3b1fbb98e075fa', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.125, 'Rank IC': 0.039, 'Rank ICIR': 0.361}, 'data_train_vec': ['2023-03-24', '2025-06-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.361', 'weight': '0.087'}

	Recorder: 22c3b39a80d94a80bd4858c1985f15ce

		Model: {'id': '22c3b39a80d94a80bd4858c1985f15ce', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.141, 'Rank IC': 0.023, 'Rank ICIR': 0.181}, 'data_train_vec': ['2024-03-24', '2025-09-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.181', 'weight': '0.044'}

	Recorder: 4a49f106031147be807f87c6fe0a5ab8

		Model: {'id': '4a49f106031147be807f87c6fe0a5ab8', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.275, 'Rank IC': 0.036, 'Rank ICIR': 0.357}, 'data_train_vec': ['2025-03-24', '2025-12-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.357', 'weight': '0.086'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260324_11 785439232791858289 (Recorders: 3/5)

	Recorder: be9de332593744cb84dbdc284f406390

		Model: {'id': 'be9de332593744cb84dbdc284f406390', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.09, 'Rank IC': 0.036, 'Rank ICIR': 0.197}, 'data_train_vec': ['2021-03-24', '2024-12-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.197', 'weight': '0.048'}

	Recorder: 6a51175aa05f4aca8aa8ea838fc6b26d

		Model: {'id': '6a51175aa05f4aca8aa8ea838fc6b26d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.192, 'Rank IC': 0.041, 'Rank ICIR': 0.43}, 'data_train_vec': ['2024-03-24', '2025-09-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.430', 'weight': '0.104'}

	Recorder: fce9df3fd1094781a5ccdd0fbd4e73f3

		Model: {'id': 'fce9df3fd1094781a5ccdd0fbd4e73f3', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.174, 'Rank IC': 0.026, 'Rank ICIR': 0.301}, 'data_train_vec': ['2025-03-24', '2025-12-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.301', 'weight': '0.073'}
