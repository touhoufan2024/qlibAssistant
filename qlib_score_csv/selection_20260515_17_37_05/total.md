# params 
 {'predict_dates': [{'start': '2026-05-15', 'end': '2026-05-15'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260515_17 964439143198371866 (Recorders: 3/5)

	Recorder: eadfb1e8ec3b4c07bb49c93035e93c5d

		Model: {'id': 'eadfb1e8ec3b4c07bb49c93035e93c5d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.032, 'Rank IC': 0.02, 'Rank ICIR': 0.128}, 'data_train_vec': ['2022-05-15', '2025-05-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.128', 'weight': '0.057'}

	Recorder: 5dbc3332f3104d0590cc5311426d1ae9

		Model: {'id': '5dbc3332f3104d0590cc5311426d1ae9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.017, 'Rank IC': 0.022, 'Rank ICIR': 0.143}, 'data_train_vec': ['2023-05-15', '2025-08-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.143', 'weight': '0.063'}

	Recorder: 0066245dbc774fea8e2b0fd3f10c693f

		Model: {'id': '0066245dbc774fea8e2b0fd3f10c693f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.081, 'ICIR': 0.54, 'Rank IC': 0.043, 'Rank ICIR': 0.267}, 'data_train_vec': ['2025-05-15', '2026-02-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.267', 'weight': '0.118'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260515_17 339311548361081298 (Recorders: 2/5)

	Recorder: 68ea6cef8fa7456cb42be473cebaf136

		Model: {'id': '68ea6cef8fa7456cb42be473cebaf136', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.165, 'Rank IC': 0.021, 'Rank ICIR': 0.181}, 'data_train_vec': ['2023-05-15', '2025-08-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.181', 'weight': '0.080'}

	Recorder: e29e3cddd2924b7eadbc0414091c2420

		Model: {'id': 'e29e3cddd2924b7eadbc0414091c2420', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.079, 'ICIR': 0.503, 'Rank IC': 0.026, 'Rank ICIR': 0.156}, 'data_train_vec': ['2025-05-15', '2026-02-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.156', 'weight': '0.069'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260515_14 860430563390184098 (Recorders: 3/5)

	Recorder: 360790e72dec4837a4c21447eeb42bdf

		Model: {'id': '360790e72dec4837a4c21447eeb42bdf', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.022, 'Rank IC': 0.032, 'Rank ICIR': 0.172}, 'data_train_vec': ['2022-05-15', '2025-05-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.172', 'weight': '0.076'}

	Recorder: e661aab0aff34546a82f7b07df4f0afb

		Model: {'id': 'e661aab0aff34546a82f7b07df4f0afb', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.099, 'Rank IC': 0.034, 'Rank ICIR': 0.215}, 'data_train_vec': ['2023-05-15', '2025-08-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.215', 'weight': '0.095'}

	Recorder: b46154ea3fe34410bf547e229a542afc

		Model: {'id': 'b46154ea3fe34410bf547e229a542afc', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.06, 'ICIR': 0.384, 'Rank IC': 0.026, 'Rank ICIR': 0.155}, 'data_train_vec': ['2025-05-15', '2026-02-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.155', 'weight': '0.069'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260515_14 695992838154208979 (Recorders: 3/5)

	Recorder: f01a63c372a84404bf39c5b5111a00d1

		Model: {'id': 'f01a63c372a84404bf39c5b5111a00d1', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.037, 'Rank IC': 0.029, 'Rank ICIR': 0.266}, 'data_train_vec': ['2023-05-15', '2025-08-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.266', 'weight': '0.118'}

	Recorder: d3fe9737ab0c4e47bf5a66a2fdbde7ff

		Model: {'id': 'd3fe9737ab0c4e47bf5a66a2fdbde7ff', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.042, 'Rank IC': 0.016, 'Rank ICIR': 0.142}, 'data_train_vec': ['2024-05-15', '2025-11-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.142', 'weight': '0.063'}

	Recorder: 1b3b2ed532db4a379b542a40e7be4c09

		Model: {'id': '1b3b2ed532db4a379b542a40e7be4c09', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.075, 'ICIR': 0.594, 'Rank IC': 0.044, 'Rank ICIR': 0.313}, 'data_train_vec': ['2025-05-15', '2026-02-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.313', 'weight': '0.138'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260515_14 597534101208221764 (Recorders: 1/5)

	Recorder: beb148c276974ec3bb821eaa1c9e3b8d

		Model: {'id': 'beb148c276974ec3bb821eaa1c9e3b8d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.337, 'Rank IC': 0.017, 'Rank ICIR': 0.123}, 'data_train_vec': ['2025-05-15', '2026-02-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.123', 'weight': '0.054'}
