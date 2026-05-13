# params 
 {'predict_dates': [{'start': '2026-05-13', 'end': '2026-05-13'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260513_17 581210342362774742 (Recorders: 2/5)

	Recorder: 7f460279a72b41d1aad5abae9502403a

		Model: {'id': '7f460279a72b41d1aad5abae9502403a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.02, 'Rank IC': 0.004, 'Rank ICIR': 0.032}, 'data_train_vec': ['2024-05-13', '2025-11-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.032', 'weight': '0.013'}

	Recorder: 8966ef6e081a4e84885945387e784577

		Model: {'id': '8966ef6e081a4e84885945387e784577', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.085, 'ICIR': 0.779, 'Rank IC': 0.047, 'Rank ICIR': 0.425}, 'data_train_vec': ['2025-05-13', '2026-02-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.425', 'weight': '0.167'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260513_17 785741092655592797 (Recorders: 3/5)

	Recorder: c14dd79f64124ad38ac423118584caf7

		Model: {'id': 'c14dd79f64124ad38ac423118584caf7', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.179, 'Rank IC': 0.024, 'Rank ICIR': 0.206}, 'data_train_vec': ['2023-05-13', '2025-08-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.206', 'weight': '0.081'}

	Recorder: c3ffd67d85ac48a4b3563aa48c1832f6

		Model: {'id': 'c3ffd67d85ac48a4b3563aa48c1832f6', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.197, 'Rank IC': 0.003, 'Rank ICIR': 0.025}, 'data_train_vec': ['2024-05-13', '2025-11-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.025', 'weight': '0.010'}

	Recorder: d19b3611df35435f84dbe784416a04a7

		Model: {'id': 'd19b3611df35435f84dbe784416a04a7', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.097, 'ICIR': 0.678, 'Rank IC': 0.045, 'Rank ICIR': 0.325}, 'data_train_vec': ['2025-05-13', '2026-02-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.325', 'weight': '0.128'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260513_15 745722252153148892 (Recorders: 3/5)

	Recorder: 0ebfb2abff314ac3a0cdcab09e58e86a

		Model: {'id': '0ebfb2abff314ac3a0cdcab09e58e86a', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.056, 'Rank IC': 0.027, 'Rank ICIR': 0.18}, 'data_train_vec': ['2023-05-13', '2025-08-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.180', 'weight': '0.071'}

	Recorder: 2bfe6941872f488c8078959c772b5ffe

		Model: {'id': '2bfe6941872f488c8078959c772b5ffe', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.034, 'Rank IC': 0.003, 'Rank ICIR': 0.026}, 'data_train_vec': ['2024-05-13', '2025-11-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.026', 'weight': '0.010'}

	Recorder: 6a36dacd3fcd458fa0ba1a6f6190f73c

		Model: {'id': '6a36dacd3fcd458fa0ba1a6f6190f73c', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.082, 'ICIR': 0.686, 'Rank IC': 0.037, 'Rank ICIR': 0.304}, 'data_train_vec': ['2025-05-13', '2026-02-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.304', 'weight': '0.120'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260513_15 149677632421386747 (Recorders: 3/5)

	Recorder: da443c9a35a849e4bc0aca9d2661cbe2

		Model: {'id': 'da443c9a35a849e4bc0aca9d2661cbe2', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.017, 'Rank IC': 0.026, 'Rank ICIR': 0.234}, 'data_train_vec': ['2023-05-13', '2025-08-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.234', 'weight': '0.092'}

	Recorder: 7e93d944a2a14258b68dfb4ff1b86858

		Model: {'id': '7e93d944a2a14258b68dfb4ff1b86858', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.124, 'Rank IC': 0.024, 'Rank ICIR': 0.21}, 'data_train_vec': ['2024-05-13', '2025-11-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.210', 'weight': '0.083'}

	Recorder: 1ef4b52d8f954efd945dac9add9ed9cd

		Model: {'id': '1ef4b52d8f954efd945dac9add9ed9cd', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.072, 'ICIR': 0.608, 'Rank IC': 0.045, 'Rank ICIR': 0.366}, 'data_train_vec': ['2025-05-13', '2026-02-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.366', 'weight': '0.144'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260513_14 341509640666702656 (Recorders: 1/5)

	Recorder: 1f8a58146fcf4c9a904a65646abd1fd5

		Model: {'id': '1f8a58146fcf4c9a904a65646abd1fd5', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.407, 'Rank IC': 0.022, 'Rank ICIR': 0.209}, 'data_train_vec': ['2025-05-13', '2026-02-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.209', 'weight': '0.082'}
