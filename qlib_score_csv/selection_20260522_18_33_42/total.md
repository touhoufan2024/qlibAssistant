# params 
 {'predict_dates': [{'start': '2026-05-22', 'end': '2026-05-22'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260522_18 160348301125110098 (Recorders: 3/5)

	Recorder: 2a0569aa2b6b4652abbc979dfb442c93

		Model: {'id': '2a0569aa2b6b4652abbc979dfb442c93', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.03, 'Rank IC': 0.027, 'Rank ICIR': 0.189}, 'data_train_vec': ['2022-05-22', '2025-05-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.189', 'weight': '0.055'}

	Recorder: bf9fa18f8ef645ca8678c677115ccbb7

		Model: {'id': 'bf9fa18f8ef645ca8678c677115ccbb7', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.119, 'Rank IC': 0.037, 'Rank ICIR': 0.254}, 'data_train_vec': ['2023-05-22', '2025-08-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.254', 'weight': '0.074'}

	Recorder: 14a40799d19345b6802e86c25f352931

		Model: {'id': '14a40799d19345b6802e86c25f352931', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.069, 'ICIR': 0.48, 'Rank IC': 0.03, 'Rank ICIR': 0.182}, 'data_train_vec': ['2025-05-22', '2026-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.182', 'weight': '0.053'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260522_17 812279638358442319 (Recorders: 3/5)

	Recorder: 2fa077ffc9524723899d0df04d3043f1

		Model: {'id': '2fa077ffc9524723899d0df04d3043f1', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.182, 'Rank IC': 0.027, 'Rank ICIR': 0.219}, 'data_train_vec': ['2023-05-22', '2025-08-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.219', 'weight': '0.064'}

	Recorder: fd6606f20d86488196e5555f5677fd13

		Model: {'id': 'fd6606f20d86488196e5555f5677fd13', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.228, 'Rank IC': 0.007, 'Rank ICIR': 0.07}, 'data_train_vec': ['2024-05-22', '2025-11-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.070', 'weight': '0.020'}

	Recorder: f8e14305235d45b188895a1602853adc

		Model: {'id': 'f8e14305235d45b188895a1602853adc', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.096, 'ICIR': 0.536, 'Rank IC': 0.047, 'Rank ICIR': 0.252}, 'data_train_vec': ['2025-05-22', '2026-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.252', 'weight': '0.073'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260522_15 258616158391768120 (Recorders: 4/5)

	Recorder: 528c7549ec2643d5b10c6cecfaba4dd4

		Model: {'id': '528c7549ec2643d5b10c6cecfaba4dd4', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.022, 'Rank IC': 0.027, 'Rank ICIR': 0.178}, 'data_train_vec': ['2021-05-22', '2025-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.178', 'weight': '0.052'}

	Recorder: 63f4ea030afb4757b61331b305cafb9b

		Model: {'id': '63f4ea030afb4757b61331b305cafb9b', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.015, 'Rank IC': 0.037, 'Rank ICIR': 0.204}, 'data_train_vec': ['2022-05-22', '2025-05-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.204', 'weight': '0.059'}

	Recorder: 5cbaad66a8b1446c9f93bc852d898c23

		Model: {'id': '5cbaad66a8b1446c9f93bc852d898c23', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.174, 'Rank IC': 0.039, 'Rank ICIR': 0.265}, 'data_train_vec': ['2023-05-22', '2025-08-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.265', 'weight': '0.077'}

	Recorder: 226ae5346fec4c3e8f402ec20ebec218

		Model: {'id': '226ae5346fec4c3e8f402ec20ebec218', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.078, 'ICIR': 0.471, 'Rank IC': 0.045, 'Rank ICIR': 0.242}, 'data_train_vec': ['2025-05-22', '2026-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.242', 'weight': '0.070'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260522_15 664869282511188682 (Recorders: 4/5)

	Recorder: dff146e076204613be2b0e8f5b3019e9

		Model: {'id': 'dff146e076204613be2b0e8f5b3019e9', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.065, 'Rank IC': 0.031, 'Rank ICIR': 0.28}, 'data_train_vec': ['2021-05-22', '2025-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.280', 'weight': '0.081'}

	Recorder: 25b244d71e4b45c3855c3cbac8ae7dc9

		Model: {'id': '25b244d71e4b45c3855c3cbac8ae7dc9', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.108, 'Rank IC': 0.036, 'Rank ICIR': 0.337}, 'data_train_vec': ['2023-05-22', '2025-08-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.337', 'weight': '0.098'}

	Recorder: 0ce4f9eb665940f9a2f8e6d759430411

		Model: {'id': '0ce4f9eb665940f9a2f8e6d759430411', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.001, 'ICIR': 0.008, 'Rank IC': 0.012, 'Rank ICIR': 0.091}, 'data_train_vec': ['2024-05-22', '2025-11-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.091', 'weight': '0.026'}

	Recorder: 61cd92fb4156431d9710d254fbdc7e5b

		Model: {'id': '61cd92fb4156431d9710d254fbdc7e5b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.081, 'ICIR': 0.486, 'Rank IC': 0.059, 'Rank ICIR': 0.311}, 'data_train_vec': ['2025-05-22', '2026-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.311', 'weight': '0.090'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260522_15 963901531068043516 (Recorders: 2/5)

	Recorder: 4d139df9bee3440280e8c44798ac6bd6

		Model: {'id': '4d139df9bee3440280e8c44798ac6bd6', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.075, 'Rank IC': 0.032, 'Rank ICIR': 0.233}, 'data_train_vec': ['2023-05-22', '2025-08-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.233', 'weight': '0.068'}

	Recorder: 3f88139ef60441799a753b36dd5d2dc8

		Model: {'id': '3f88139ef60441799a753b36dd5d2dc8', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.349, 'Rank IC': 0.021, 'Rank ICIR': 0.135}, 'data_train_vec': ['2025-05-22', '2026-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.135', 'weight': '0.039'}
