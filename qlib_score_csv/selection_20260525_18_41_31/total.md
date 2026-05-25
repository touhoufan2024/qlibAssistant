# params 
 {'predict_dates': [{'start': '2026-05-25', 'end': '2026-05-25'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260525_18 759615258211834293 (Recorders: 3/5)

	Recorder: 5e5bc49bcc5a49f2a7a635846f2c2095

		Model: {'id': '5e5bc49bcc5a49f2a7a635846f2c2095', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.076, 'Rank IC': 0.031, 'Rank ICIR': 0.22}, 'data_train_vec': ['2021-05-25', '2025-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.220', 'weight': '0.058'}

	Recorder: 92d94537e43d4f90aee7cb30ba737bf0

		Model: {'id': '92d94537e43d4f90aee7cb30ba737bf0', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.237, 'Rank IC': 0.034, 'Rank ICIR': 0.24}, 'data_train_vec': ['2023-05-25', '2025-08-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.240', 'weight': '0.063'}

	Recorder: bc4ba3a7e18d458e82d3c3947d63427a

		Model: {'id': 'bc4ba3a7e18d458e82d3c3947d63427a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.071, 'ICIR': 0.363, 'Rank IC': 0.05, 'Rank ICIR': 0.29}, 'data_train_vec': ['2025-05-25', '2026-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.290', 'weight': '0.076'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260525_18 989662224325803213 (Recorders: 3/5)

	Recorder: 81822cb4cf5040638ce7a92b391935b8

		Model: {'id': '81822cb4cf5040638ce7a92b391935b8', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.082, 'Rank IC': 0.022, 'Rank ICIR': 0.17}, 'data_train_vec': ['2023-05-25', '2025-08-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.170', 'weight': '0.045'}

	Recorder: f09a8bad4c36426ca5926afbb9188ac9

		Model: {'id': 'f09a8bad4c36426ca5926afbb9188ac9', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.173, 'Rank IC': 0.005, 'Rank ICIR': 0.041}, 'data_train_vec': ['2024-05-25', '2025-11-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.041', 'weight': '0.011'}

	Recorder: 223acaa3d5d94b33ba5a4af1ad761408

		Model: {'id': '223acaa3d5d94b33ba5a4af1ad761408', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.095, 'ICIR': 0.536, 'Rank IC': 0.052, 'Rank ICIR': 0.273}, 'data_train_vec': ['2025-05-25', '2026-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.273', 'weight': '0.072'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260525_15 604271282644500154 (Recorders: 4/5)

	Recorder: a105656fb7cf4c99b147ad199ea09754

		Model: {'id': 'a105656fb7cf4c99b147ad199ea09754', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.069, 'Rank IC': 0.034, 'Rank ICIR': 0.234}, 'data_train_vec': ['2021-05-25', '2025-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.234', 'weight': '0.061'}

	Recorder: 5228c99354c8403e9bca2f6ad53e71ca

		Model: {'id': '5228c99354c8403e9bca2f6ad53e71ca', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.036, 'Rank IC': 0.035, 'Rank ICIR': 0.197}, 'data_train_vec': ['2022-05-25', '2025-05-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.197', 'weight': '0.052'}

	Recorder: 6cd1aea167e744bcacfe5c9d7957247f

		Model: {'id': '6cd1aea167e744bcacfe5c9d7957247f', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.146, 'Rank IC': 0.036, 'Rank ICIR': 0.253}, 'data_train_vec': ['2023-05-25', '2025-08-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.253', 'weight': '0.066'}

	Recorder: 37c22715e6984382b5ced3ad0bb1a782

		Model: {'id': '37c22715e6984382b5ced3ad0bb1a782', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.072, 'ICIR': 0.368, 'Rank IC': 0.048, 'Rank ICIR': 0.253}, 'data_train_vec': ['2025-05-25', '2026-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.253', 'weight': '0.066'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260525_15 589716933095867244 (Recorders: 4/5)

	Recorder: bfd7c6a49c0841d18b50cb943b117dfe

		Model: {'id': 'bfd7c6a49c0841d18b50cb943b117dfe', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.063, 'Rank IC': 0.031, 'Rank ICIR': 0.277}, 'data_train_vec': ['2021-05-25', '2025-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.277', 'weight': '0.073'}

	Recorder: 9ecc234e305e4e50b575d055c44b99af

		Model: {'id': '9ecc234e305e4e50b575d055c44b99af', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.094, 'Rank IC': 0.036, 'Rank ICIR': 0.329}, 'data_train_vec': ['2023-05-25', '2025-08-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.329', 'weight': '0.086'}

	Recorder: 3abe422dba4246878a657eef361a0ae3

		Model: {'id': '3abe422dba4246878a657eef361a0ae3', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.015, 'Rank IC': 0.01, 'Rank ICIR': 0.079}, 'data_train_vec': ['2024-05-25', '2025-11-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.079', 'weight': '0.021'}

	Recorder: 265cf8a5550e42408cb45def661d08d2

		Model: {'id': '265cf8a5550e42408cb45def661d08d2', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.11, 'ICIR': 0.624, 'Rank IC': 0.089, 'Rank ICIR': 0.45}, 'data_train_vec': ['2025-05-25', '2026-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.450', 'weight': '0.118'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260525_15 212845049461667510 (Recorders: 2/5)

	Recorder: 55360911eb4c496497d6b06913a152f6

		Model: {'id': '55360911eb4c496497d6b06913a152f6', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.13, 'Rank IC': 0.034, 'Rank ICIR': 0.215}, 'data_train_vec': ['2023-05-25', '2025-08-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.215', 'weight': '0.056'}

	Recorder: 58bc37f2b471467d9c7b66617241a485

		Model: {'id': '58bc37f2b471467d9c7b66617241a485', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.059, 'ICIR': 0.32, 'Rank IC': 0.042, 'Rank ICIR': 0.295}, 'data_train_vec': ['2025-05-25', '2026-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.295', 'weight': '0.077'}
