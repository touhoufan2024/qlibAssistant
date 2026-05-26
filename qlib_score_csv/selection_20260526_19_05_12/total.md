# params 
 {'predict_dates': [{'start': '2026-05-26', 'end': '2026-05-26'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260526_18 947819997783735560 (Recorders: 3/5)

	Recorder: e0ee30f707eb482d887043e8619c2e17

		Model: {'id': 'e0ee30f707eb482d887043e8619c2e17', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.032, 'Rank IC': 0.029, 'Rank ICIR': 0.167}, 'data_train_vec': ['2022-05-26', '2025-05-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.167', 'weight': '0.051'}

	Recorder: 615848e9b9b04fbca369242db6504a72

		Model: {'id': '615848e9b9b04fbca369242db6504a72', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.057, 'Rank IC': 0.028, 'Rank ICIR': 0.177}, 'data_train_vec': ['2023-05-26', '2025-08-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.177', 'weight': '0.054'}

	Recorder: 090b711ab1d249159414563687a92541

		Model: {'id': '090b711ab1d249159414563687a92541', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.193, 'Rank IC': 0.035, 'Rank ICIR': 0.191}, 'data_train_vec': ['2025-05-26', '2026-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.191', 'weight': '0.058'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260526_18 924221270172696759 (Recorders: 3/5)

	Recorder: 7a929ff875d1424fa6d91e622a796da7

		Model: {'id': '7a929ff875d1424fa6d91e622a796da7', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.198, 'Rank IC': 0.029, 'Rank ICIR': 0.236}, 'data_train_vec': ['2023-05-26', '2025-08-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.236', 'weight': '0.072'}

	Recorder: 6c9a0792e14d4b6f8903b1cecd0e3241

		Model: {'id': '6c9a0792e14d4b6f8903b1cecd0e3241', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.2, 'Rank IC': 0.01, 'Rank ICIR': 0.084}, 'data_train_vec': ['2024-05-26', '2025-11-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.084', 'weight': '0.026'}

	Recorder: d26f0b72d3cb4fd88a673ab28a6d1286

		Model: {'id': 'd26f0b72d3cb4fd88a673ab28a6d1286', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.085, 'ICIR': 0.451, 'Rank IC': 0.045, 'Rank ICIR': 0.217}, 'data_train_vec': ['2025-05-26', '2026-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.217', 'weight': '0.066'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260526_16 109396270003262722 (Recorders: 4/5)

	Recorder: ae3e7bd2678043a7a6ba20e0d0df2361

		Model: {'id': 'ae3e7bd2678043a7a6ba20e0d0df2361', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.044, 'Rank IC': 0.032, 'Rank ICIR': 0.214}, 'data_train_vec': ['2021-05-26', '2025-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.214', 'weight': '0.065'}

	Recorder: bfd2ce3cba104b439be03a417251a101

		Model: {'id': 'bfd2ce3cba104b439be03a417251a101', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.05, 'Rank IC': 0.037, 'Rank ICIR': 0.211}, 'data_train_vec': ['2022-05-26', '2025-05-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.211', 'weight': '0.064'}

	Recorder: 348be991fa9a414ca72df7c6a789b0da

		Model: {'id': '348be991fa9a414ca72df7c6a789b0da', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.138, 'Rank IC': 0.036, 'Rank ICIR': 0.242}, 'data_train_vec': ['2023-05-26', '2025-08-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.242', 'weight': '0.074'}

	Recorder: fba264fa22b84cc49a530beb52e0e53d

		Model: {'id': 'fba264fa22b84cc49a530beb52e0e53d', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.061, 'ICIR': 0.306, 'Rank IC': 0.034, 'Rank ICIR': 0.176}, 'data_train_vec': ['2025-05-26', '2026-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.176', 'weight': '0.053'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260526_16 998812886803208317 (Recorders: 4/5)

	Recorder: d7f6ac00662645d085d24aac68d94e6e

		Model: {'id': 'd7f6ac00662645d085d24aac68d94e6e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.059, 'Rank IC': 0.032, 'Rank ICIR': 0.278}, 'data_train_vec': ['2021-05-26', '2025-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.278', 'weight': '0.084'}

	Recorder: 47c6125a611c4ff59edf1d9bd6312a46

		Model: {'id': '47c6125a611c4ff59edf1d9bd6312a46', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.108, 'Rank IC': 0.038, 'Rank ICIR': 0.345}, 'data_train_vec': ['2023-05-26', '2025-08-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.345', 'weight': '0.105'}

	Recorder: 00100c2360de46abb49ccbe4446053f5

		Model: {'id': '00100c2360de46abb49ccbe4446053f5', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.023, 'Rank IC': 0.011, 'Rank ICIR': 0.087}, 'data_train_vec': ['2024-05-26', '2025-11-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.087', 'weight': '0.026'}

	Recorder: caf4e3257e204df4931e1a88020856d0

		Model: {'id': 'caf4e3257e204df4931e1a88020856d0', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.104, 'ICIR': 0.604, 'Rank IC': 0.081, 'Rank ICIR': 0.412}, 'data_train_vec': ['2025-05-26', '2026-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.412', 'weight': '0.125'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260526_16 257016616194600981 (Recorders: 1/5)

	Recorder: d2819d5aa3aa4b8890fb203b66c70119

		Model: {'id': 'd2819d5aa3aa4b8890fb203b66c70119', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.302, 'Rank IC': 0.038, 'Rank ICIR': 0.255}, 'data_train_vec': ['2025-05-26', '2026-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.255', 'weight': '0.077'}
