# params 
 {'predict_dates': [{'start': '2026-04-20', 'end': '2026-04-20'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260420_16 483467595788066615 (Recorders: 3/5)

	Recorder: cd16c53a00d84f23af72903b2a0d233f

		Model: {'id': 'cd16c53a00d84f23af72903b2a0d233f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.306, 'Rank IC': 0.04, 'Rank ICIR': 0.26}, 'data_train_vec': ['2023-04-20', '2025-07-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.260', 'weight': '0.108'}

	Recorder: 9671ac79c4d645a99a454fafe67ad3ef

		Model: {'id': '9671ac79c4d645a99a454fafe67ad3ef', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.067, 'Rank IC': 0.034, 'Rank ICIR': 0.232}, 'data_train_vec': ['2024-04-20', '2025-10-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.232', 'weight': '0.096'}

	Recorder: 4bee36220fa9414fa0b3b614b67cc9a2

		Model: {'id': '4bee36220fa9414fa0b3b614b67cc9a2', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.235, 'Rank IC': 0.011, 'Rank ICIR': 0.111}, 'data_train_vec': ['2025-04-20', '2026-01-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.111', 'weight': '0.046'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260420_16 956248616138082038 (Recorders: 2/5)

	Recorder: 08c82561fdd04f6db55b1721c202fa45

		Model: {'id': '08c82561fdd04f6db55b1721c202fa45', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.186, 'Rank IC': 0.034, 'Rank ICIR': 0.287}, 'data_train_vec': ['2024-04-20', '2025-10-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.287', 'weight': '0.119'}

	Recorder: b4d27b30425a47ae819b75bfe7b56637

		Model: {'id': 'b4d27b30425a47ae819b75bfe7b56637', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.207, 'Rank IC': 0.016, 'Rank ICIR': 0.117}, 'data_train_vec': ['2025-04-20', '2026-01-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.117', 'weight': '0.049'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260420_14 983337132141051757 (Recorders: 3/5)

	Recorder: 3b05bdcfa6274c5da944bfad4e5c8a70

		Model: {'id': '3b05bdcfa6274c5da944bfad4e5c8a70', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.048, 'Rank IC': 0.04, 'Rank ICIR': 0.232}, 'data_train_vec': ['2023-04-20', '2025-07-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.232', 'weight': '0.096'}

	Recorder: fc4b5b1d04e9444cb84c77c2bc456e24

		Model: {'id': 'fc4b5b1d04e9444cb84c77c2bc456e24', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.157, 'Rank IC': 0.023, 'Rank ICIR': 0.201}, 'data_train_vec': ['2024-04-20', '2025-10-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.201', 'weight': '0.083'}

	Recorder: b44ed86f0b3c4975aefe4d5a31125a22

		Model: {'id': 'b44ed86f0b3c4975aefe4d5a31125a22', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.269, 'Rank IC': 0.028, 'Rank ICIR': 0.153}, 'data_train_vec': ['2025-04-20', '2026-01-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.153', 'weight': '0.064'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260420_14 485801543212418988 (Recorders: 2/5)

	Recorder: 89ff1c4592574e6881bac06661adb08e

		Model: {'id': '89ff1c4592574e6881bac06661adb08e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.032, 'Rank IC': 0.013, 'Rank ICIR': 0.106}, 'data_train_vec': ['2024-04-20', '2025-10-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.106', 'weight': '0.044'}

	Recorder: cb92e8df218941a3a71ab6bd22baa142

		Model: {'id': 'cb92e8df218941a3a71ab6bd22baa142', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.068, 'ICIR': 0.465, 'Rank IC': 0.049, 'Rank ICIR': 0.332}, 'data_train_vec': ['2025-04-20', '2026-01-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.332', 'weight': '0.138'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260420_14 714540063568117217 (Recorders: 2/5)

	Recorder: 1e46de2ddb5443c0a7baaa1da8c41782

		Model: {'id': '1e46de2ddb5443c0a7baaa1da8c41782', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.076, 'Rank IC': 0.03, 'Rank ICIR': 0.257}, 'data_train_vec': ['2024-04-20', '2025-10-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.257', 'weight': '0.107'}

	Recorder: e541ff1d0b7045b9a7b0176132ac767b

		Model: {'id': 'e541ff1d0b7045b9a7b0176132ac767b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.064, 'ICIR': 0.42, 'Rank IC': 0.019, 'Rank ICIR': 0.12}, 'data_train_vec': ['2025-04-20', '2026-01-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.120', 'weight': '0.050'}
