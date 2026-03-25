# params 
 {'predict_dates': [{'start': '2026-03-25', 'end': '2026-03-25'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260325_16 967043139346852973 (Recorders: 3/5)

	Recorder: dbd8eda0346e4df5bbb0cff9d943f87d

		Model: {'id': 'dbd8eda0346e4df5bbb0cff9d943f87d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.045, 'Rank IC': 0.021, 'Rank ICIR': 0.159}, 'data_train_vec': ['2021-03-25', '2024-12-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.159', 'weight': '0.034'}

	Recorder: 2cf7c5df6a914b9f9bb13bfda831d0f6

		Model: {'id': '2cf7c5df6a914b9f9bb13bfda831d0f6', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.106, 'Rank IC': 0.038, 'Rank ICIR': 0.304}, 'data_train_vec': ['2024-03-25', '2025-09-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.304', 'weight': '0.065'}

	Recorder: 7449ee690da34db29bf4c66195f89eed

		Model: {'id': '7449ee690da34db29bf4c66195f89eed', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.169, 'Rank IC': 0.017, 'Rank ICIR': 0.115}, 'data_train_vec': ['2025-03-25', '2025-12-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.115', 'weight': '0.024'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260325_16 198275085490698208 (Recorders: 2/5)

	Recorder: 311436a03429409fa0db764fdbbf31f3

		Model: {'id': '311436a03429409fa0db764fdbbf31f3', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.06, 'Rank IC': 0.026, 'Rank ICIR': 0.189}, 'data_train_vec': ['2021-03-25', '2024-12-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.189', 'weight': '0.040'}

	Recorder: ef99fb2ae1624626a6c47ccd7999d4eb

		Model: {'id': 'ef99fb2ae1624626a6c47ccd7999d4eb', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.352, 'Rank IC': 0.051, 'Rank ICIR': 0.441}, 'data_train_vec': ['2024-03-25', '2025-09-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.441', 'weight': '0.094'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260325_13 152546684946291310 (Recorders: 3/5)

	Recorder: f49aebe726dc4aef9c5a54acb95cd84c

		Model: {'id': 'f49aebe726dc4aef9c5a54acb95cd84c', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.112, 'Rank IC': 0.036, 'Rank ICIR': 0.212}, 'data_train_vec': ['2021-03-25', '2024-12-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.212', 'weight': '0.045'}

	Recorder: 31463ac2b00048ac87694da1d0b49573

		Model: {'id': '31463ac2b00048ac87694da1d0b49573', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.347, 'Rank IC': 0.048, 'Rank ICIR': 0.416}, 'data_train_vec': ['2024-03-25', '2025-09-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.416', 'weight': '0.089'}

	Recorder: ff50d1d2d2844b06ac632fc0256e9010

		Model: {'id': 'ff50d1d2d2844b06ac632fc0256e9010', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.114, 'Rank IC': 0.027, 'Rank ICIR': 0.243}, 'data_train_vec': ['2025-03-25', '2025-12-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.243', 'weight': '0.052'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260325_13 615411766792646758 (Recorders: 5/5)

	Recorder: a4f81bc5c1404c459581b206af2489b9

		Model: {'id': 'a4f81bc5c1404c459581b206af2489b9', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.169, 'Rank IC': 0.027, 'Rank ICIR': 0.233}, 'data_train_vec': ['2021-03-25', '2024-12-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.233', 'weight': '0.050'}

	Recorder: 7517d3f16fd64554987776cdb6c997ca

		Model: {'id': '7517d3f16fd64554987776cdb6c997ca', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.035, 'Rank IC': 0.019, 'Rank ICIR': 0.162}, 'data_train_vec': ['2022-03-25', '2025-03-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.162', 'weight': '0.035'}

	Recorder: 6e8b0aca31ba41859d87aef04c17642b

		Model: {'id': '6e8b0aca31ba41859d87aef04c17642b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.127, 'Rank IC': 0.038, 'Rank ICIR': 0.341}, 'data_train_vec': ['2023-03-25', '2025-06-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.341', 'weight': '0.073'}

	Recorder: 3085052d05af4bdabd0a701ff14106b5

		Model: {'id': '3085052d05af4bdabd0a701ff14106b5', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.148, 'Rank IC': 0.025, 'Rank ICIR': 0.214}, 'data_train_vec': ['2024-03-25', '2025-09-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.214', 'weight': '0.046'}

	Recorder: 538ca392e3664091b4621cb28e5434a1

		Model: {'id': '538ca392e3664091b4621cb28e5434a1', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.173, 'Rank IC': 0.025, 'Rank ICIR': 0.242}, 'data_train_vec': ['2025-03-25', '2025-12-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.242', 'weight': '0.052'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260325_13 941295612906688654 (Recorders: 5/5)

	Recorder: 2d08136d08ff459bbfb9c89bc7ab391a

		Model: {'id': '2d08136d08ff459bbfb9c89bc7ab391a', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.102, 'Rank IC': 0.039, 'Rank ICIR': 0.216}, 'data_train_vec': ['2021-03-25', '2024-12-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.216', 'weight': '0.046'}

	Recorder: 6926de09c8de49268d7c66ec7fb9b045

		Model: {'id': '6926de09c8de49268d7c66ec7fb9b045', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.045, 'Rank IC': 0.014, 'Rank ICIR': 0.073}, 'data_train_vec': ['2022-03-25', '2025-03-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.073', 'weight': '0.016'}

	Recorder: 3de2219e996f460ca810a1157b69f979

		Model: {'id': '3de2219e996f460ca810a1157b69f979', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.032, 'Rank IC': 0.032, 'Rank ICIR': 0.185}, 'data_train_vec': ['2023-03-25', '2025-06-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.185', 'weight': '0.039'}

	Recorder: 0e9d9f43ea5e416580f7e2969c575473

		Model: {'id': '0e9d9f43ea5e416580f7e2969c575473', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.06, 'Rank IC': 0.041, 'Rank ICIR': 0.393}, 'data_train_vec': ['2024-03-25', '2025-09-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.393', 'weight': '0.084'}

	Recorder: 9e97b282fcf146dcb409ca58f3114ed3

		Model: {'id': '9e97b282fcf146dcb409ca58f3114ed3', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.252, 'Rank IC': 0.04, 'Rank ICIR': 0.556}, 'data_train_vec': ['2025-03-25', '2025-12-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.556', 'weight': '0.118'}
