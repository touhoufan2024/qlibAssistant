# params 
 {'predict_dates': [{'start': '2026-04-22', 'end': '2026-04-22'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260422_16 936102175272895992 (Recorders: 2/5)

	Recorder: 3ac26f6d235940a0a4570d89c286a068

		Model: {'id': '3ac26f6d235940a0a4570d89c286a068', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.248, 'Rank IC': 0.047, 'Rank ICIR': 0.277}, 'data_train_vec': ['2023-04-22', '2025-07-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.277', 'weight': '0.147'}

	Recorder: 7bb51710754c4157a9ee3d38b5f6ada9

		Model: {'id': '7bb51710754c4157a9ee3d38b5f6ada9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.074, 'ICIR': 0.578, 'Rank IC': 0.031, 'Rank ICIR': 0.211}, 'data_train_vec': ['2025-04-22', '2026-01-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.211', 'weight': '0.112'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260422_16 139029381433555883 (Recorders: 2/5)

	Recorder: b9720d0f2d3e42c29b595279e2825d58

		Model: {'id': 'b9720d0f2d3e42c29b595279e2825d58', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.226, 'Rank IC': 0.037, 'Rank ICIR': 0.29}, 'data_train_vec': ['2024-04-22', '2025-10-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.290', 'weight': '0.154'}

	Recorder: 9f58d9d19bff42658b507dba4170c3e4

		Model: {'id': '9f58d9d19bff42658b507dba4170c3e4', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.36, 'Rank IC': 0.024, 'Rank ICIR': 0.165}, 'data_train_vec': ['2025-04-22', '2026-01-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.165', 'weight': '0.087'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260422_14 161933332149898231 (Recorders: 3/5)

	Recorder: a2e18ee038cb4fa1ab6afdee9f3e20b8

		Model: {'id': 'a2e18ee038cb4fa1ab6afdee9f3e20b8', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.032, 'Rank IC': 0.044, 'Rank ICIR': 0.243}, 'data_train_vec': ['2023-04-22', '2025-07-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.243', 'weight': '0.129'}

	Recorder: a22e9630c46c4cbfb74d6a10eef4486d

		Model: {'id': 'a22e9630c46c4cbfb74d6a10eef4486d', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.101, 'Rank IC': 0.022, 'Rank ICIR': 0.178}, 'data_train_vec': ['2024-04-22', '2025-10-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.178', 'weight': '0.094'}

	Recorder: 186db80a578b4bbaa6011c9e3978bec4

		Model: {'id': '186db80a578b4bbaa6011c9e3978bec4', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.254, 'Rank IC': 0.016, 'Rank ICIR': 0.085}, 'data_train_vec': ['2025-04-22', '2026-01-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.085', 'weight': '0.045'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260422_14 200031567566321226 (Recorders: 1/5)

	Recorder: 7670d5144d61418cb957b7b43d6ba086

		Model: {'id': '7670d5144d61418cb957b7b43d6ba086', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.051, 'ICIR': 0.406, 'Rank IC': 0.033, 'Rank ICIR': 0.245}, 'data_train_vec': ['2025-04-22', '2026-01-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.245', 'weight': '0.130'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260422_14 154868203075505251 (Recorders: 1/5)

	Recorder: dd2f275a6f6841fe96d12e49e8710891

		Model: {'id': 'dd2f275a6f6841fe96d12e49e8710891', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.322, 'Rank IC': 0.033, 'Rank ICIR': 0.192}, 'data_train_vec': ['2025-04-22', '2026-01-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.192', 'weight': '0.102'}
