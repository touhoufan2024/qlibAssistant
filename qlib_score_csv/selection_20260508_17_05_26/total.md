# params 
 {'predict_dates': [{'start': '2026-05-08', 'end': '2026-05-08'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260508_16 341634995784520172 (Recorders: 2/5)

	Recorder: 412ad2f797164ea283c96bd355803ffa

		Model: {'id': '412ad2f797164ea283c96bd355803ffa', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.131, 'Rank IC': 0.039, 'Rank ICIR': 0.239}, 'data_train_vec': ['2023-05-08', '2025-08-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.239', 'weight': '0.090'}

	Recorder: ce7763b509544a58a5167d5f95833b8d

		Model: {'id': 'ce7763b509544a58a5167d5f95833b8d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.235, 'Rank IC': 0.02, 'Rank ICIR': 0.146}, 'data_train_vec': ['2025-05-08', '2026-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.146', 'weight': '0.055'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260508_16 411498709957841207 (Recorders: 2/5)

	Recorder: e0b66afe979c4fa694be8aec7b155db9

		Model: {'id': 'e0b66afe979c4fa694be8aec7b155db9', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.159, 'Rank IC': 0.019, 'Rank ICIR': 0.157}, 'data_train_vec': ['2024-05-08', '2025-11-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.157', 'weight': '0.059'}

	Recorder: 0411137d66114b73936ac0b0c57de78a

		Model: {'id': '0411137d66114b73936ac0b0c57de78a', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.075, 'ICIR': 0.508, 'Rank IC': 0.02, 'Rank ICIR': 0.146}, 'data_train_vec': ['2025-05-08', '2026-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.146', 'weight': '0.055'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260508_14 587873585376078697 (Recorders: 4/5)

	Recorder: 1ba36a0b8331413fb4d56af8318a22c0

		Model: {'id': '1ba36a0b8331413fb4d56af8318a22c0', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.011, 'Rank IC': 0.028, 'Rank ICIR': 0.161}, 'data_train_vec': ['2022-05-08', '2025-05-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.161', 'weight': '0.061'}

	Recorder: cf305aefab7f4dcbb4f52e05625f6af7

		Model: {'id': 'cf305aefab7f4dcbb4f52e05625f6af7', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.026, 'Rank IC': 0.029, 'Rank ICIR': 0.172}, 'data_train_vec': ['2023-05-08', '2025-08-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.172', 'weight': '0.065'}

	Recorder: 75b5b0325ed6429c9c221ce6e0c0967c

		Model: {'id': '75b5b0325ed6429c9c221ce6e0c0967c', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.015, 'Rank IC': 0.012, 'Rank ICIR': 0.096}, 'data_train_vec': ['2024-05-08', '2025-11-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.096', 'weight': '0.036'}

	Recorder: 54373756076649b494601b9d11e5d431

		Model: {'id': '54373756076649b494601b9d11e5d431', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.069, 'ICIR': 0.559, 'Rank IC': 0.026, 'Rank ICIR': 0.211}, 'data_train_vec': ['2025-05-08', '2026-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.211', 'weight': '0.079'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260508_14 445682694774166720 (Recorders: 4/5)

	Recorder: 96afa9e38e0549ebaa23c3cb5f6ccde2

		Model: {'id': '96afa9e38e0549ebaa23c3cb5f6ccde2', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.03, 'Rank IC': 0.019, 'Rank ICIR': 0.17}, 'data_train_vec': ['2021-05-08', '2025-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.170', 'weight': '0.064'}

	Recorder: 9acce8c433444a82b10a3c1f989303f0

		Model: {'id': '9acce8c433444a82b10a3c1f989303f0', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.012, 'Rank IC': 0.026, 'Rank ICIR': 0.209}, 'data_train_vec': ['2022-05-08', '2025-05-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.209', 'weight': '0.079'}

	Recorder: d6637959e7a348c58795f0390520de7c

		Model: {'id': 'd6637959e7a348c58795f0390520de7c', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.058, 'Rank IC': 0.02, 'Rank ICIR': 0.181}, 'data_train_vec': ['2024-05-08', '2025-11-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.181', 'weight': '0.068'}

	Recorder: ca7e059c27a647bd97cc1b13329129cd

		Model: {'id': 'ca7e059c27a647bd97cc1b13329129cd', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.479, 'Rank IC': 0.019, 'Rank ICIR': 0.159}, 'data_train_vec': ['2025-05-08', '2026-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.159', 'weight': '0.060'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260508_14 914827972550727364 (Recorders: 3/5)

	Recorder: ce028f96472242688ee1cc127fa815df

		Model: {'id': 'ce028f96472242688ee1cc127fa815df', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.015, 'Rank IC': 0.022, 'Rank ICIR': 0.131}, 'data_train_vec': ['2023-05-08', '2025-08-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.131', 'weight': '0.049'}

	Recorder: 9e54ca2f55664d40a44a5f4ddb070e00

		Model: {'id': '9e54ca2f55664d40a44a5f4ddb070e00', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.027, 'Rank IC': 0.012, 'Rank ICIR': 0.099}, 'data_train_vec': ['2024-05-08', '2025-11-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.099', 'weight': '0.037'}

	Recorder: 182ebc5afe2947b6930c08b0b9aab0b3

		Model: {'id': '182ebc5afe2947b6930c08b0b9aab0b3', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.072, 'ICIR': 0.622, 'Rank IC': 0.042, 'Rank ICIR': 0.382}, 'data_train_vec': ['2025-05-08', '2026-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.382', 'weight': '0.144'}
