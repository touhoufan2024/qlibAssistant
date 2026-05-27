# params 
 {'predict_dates': [{'start': '2026-05-27', 'end': '2026-05-27'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260527_18 879136146324118894 (Recorders: 3/5)

	Recorder: 6286ee945d4942b3bf15ccfc995a3864

		Model: {'id': '6286ee945d4942b3bf15ccfc995a3864', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.017, 'Rank IC': 0.021, 'Rank ICIR': 0.14}, 'data_train_vec': ['2022-05-27', '2025-05-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.140', 'weight': '0.043'}

	Recorder: a965a6a226074142b65c9c1fcff1e76e

		Model: {'id': 'a965a6a226074142b65c9c1fcff1e76e', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.018, 'Rank IC': 0.028, 'Rank ICIR': 0.16}, 'data_train_vec': ['2023-05-27', '2025-08-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.160', 'weight': '0.049'}

	Recorder: e813d7b1d2014e86aa94c2bf021729f8

		Model: {'id': 'e813d7b1d2014e86aa94c2bf021729f8', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.061, 'ICIR': 0.259, 'Rank IC': 0.032, 'Rank ICIR': 0.154}, 'data_train_vec': ['2025-05-27', '2026-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.154', 'weight': '0.047'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260527_18 882305119827099413 (Recorders: 3/5)

	Recorder: bcbca2a27e2b43988c53fbb3b8f254ac

		Model: {'id': 'bcbca2a27e2b43988c53fbb3b8f254ac', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.184, 'Rank IC': 0.031, 'Rank ICIR': 0.236}, 'data_train_vec': ['2023-05-27', '2025-08-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.236', 'weight': '0.073'}

	Recorder: 87ede313f27d4bd59c1e5fbc66b07aa4

		Model: {'id': '87ede313f27d4bd59c1e5fbc66b07aa4', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.11, 'Rank IC': 0.011, 'Rank ICIR': 0.107}, 'data_train_vec': ['2024-05-27', '2025-11-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.107', 'weight': '0.033'}

	Recorder: 70ea6dca2f5948218d8271176a236a59

		Model: {'id': '70ea6dca2f5948218d8271176a236a59', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.09, 'ICIR': 0.482, 'Rank IC': 0.047, 'Rank ICIR': 0.243}, 'data_train_vec': ['2025-05-27', '2026-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.243', 'weight': '0.075'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260527_16 244641469085430947 (Recorders: 4/5)

	Recorder: 0b37fab4d91744529706ee90067988e5

		Model: {'id': '0b37fab4d91744529706ee90067988e5', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.044, 'Rank IC': 0.031, 'Rank ICIR': 0.204}, 'data_train_vec': ['2021-05-27', '2025-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.204', 'weight': '0.063'}

	Recorder: 8a68bb67098f4c029cf9699db4e7a223

		Model: {'id': '8a68bb67098f4c029cf9699db4e7a223', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.076, 'Rank IC': 0.041, 'Rank ICIR': 0.23}, 'data_train_vec': ['2022-05-27', '2025-05-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.230', 'weight': '0.071'}

	Recorder: ab1edaa86d1642029e6da147dd56a239

		Model: {'id': 'ab1edaa86d1642029e6da147dd56a239', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.217, 'Rank IC': 0.043, 'Rank ICIR': 0.282}, 'data_train_vec': ['2023-05-27', '2025-08-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.282', 'weight': '0.087'}

	Recorder: 4fb31c9eec2240a98f3722ba568ef938

		Model: {'id': '4fb31c9eec2240a98f3722ba568ef938', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.057, 'ICIR': 0.291, 'Rank IC': 0.026, 'Rank ICIR': 0.13}, 'data_train_vec': ['2025-05-27', '2026-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.130', 'weight': '0.040'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260527_16 822994551517190160 (Recorders: 3/5)

	Recorder: 54d7a4aac88f4535b87ad5edf45b4866

		Model: {'id': '54d7a4aac88f4535b87ad5edf45b4866', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.06, 'Rank IC': 0.034, 'Rank ICIR': 0.292}, 'data_train_vec': ['2021-05-27', '2025-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.292', 'weight': '0.090'}

	Recorder: b4827afb948e45f7acb36b11d1846dda

		Model: {'id': 'b4827afb948e45f7acb36b11d1846dda', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.118, 'Rank IC': 0.036, 'Rank ICIR': 0.326}, 'data_train_vec': ['2023-05-27', '2025-08-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.326', 'weight': '0.100'}

	Recorder: b0fc035c40ba4f43aff984d91cb1bb2f

		Model: {'id': 'b0fc035c40ba4f43aff984d91cb1bb2f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.092, 'ICIR': 0.507, 'Rank IC': 0.067, 'Rank ICIR': 0.319}, 'data_train_vec': ['2025-05-27', '2026-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.319', 'weight': '0.098'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260527_16 430802453776792184 (Recorders: 2/5)

	Recorder: f3c78ae6640c4ad285dcabcef616c0e0

		Model: {'id': 'f3c78ae6640c4ad285dcabcef616c0e0', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.09, 'Rank IC': 0.028, 'Rank ICIR': 0.174}, 'data_train_vec': ['2023-05-27', '2025-08-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.174', 'weight': '0.053'}

	Recorder: 7f09e8cd80644962aa667158eebfdd5d

		Model: {'id': '7f09e8cd80644962aa667158eebfdd5d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.314, 'Rank IC': 0.042, 'Rank ICIR': 0.256}, 'data_train_vec': ['2025-05-27', '2026-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.256', 'weight': '0.079'}
