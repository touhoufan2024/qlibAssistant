# params 
 {'predict_dates': [{'start': '2026-05-21', 'end': '2026-05-21'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260521_18 800252696621921120 (Recorders: 3/5)

	Recorder: 4eb7fa77584b4215af2fce08fa10f544

		Model: {'id': '4eb7fa77584b4215af2fce08fa10f544', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.035, 'Rank IC': 0.018, 'Rank ICIR': 0.133}, 'data_train_vec': ['2022-05-21', '2025-05-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.133', 'weight': '0.049'}

	Recorder: a738529c2b06474c9cf4cbc8d712f16b

		Model: {'id': 'a738529c2b06474c9cf4cbc8d712f16b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.077, 'Rank IC': 0.024, 'Rank ICIR': 0.141}, 'data_train_vec': ['2023-05-21', '2025-08-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.141', 'weight': '0.052'}

	Recorder: e9a8b7c38b8f4458904e6e6980dc7f99

		Model: {'id': 'e9a8b7c38b8f4458904e6e6980dc7f99', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.256, 'Rank IC': 0.014, 'Rank ICIR': 0.088}, 'data_train_vec': ['2025-05-21', '2026-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.088', 'weight': '0.032'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260521_18 184582489258408847 (Recorders: 3/5)

	Recorder: bb0e47fadaa64d6a9ac924951593bb91

		Model: {'id': 'bb0e47fadaa64d6a9ac924951593bb91', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.081, 'Rank IC': 0.02, 'Rank ICIR': 0.156}, 'data_train_vec': ['2023-05-21', '2025-08-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.156', 'weight': '0.057'}

	Recorder: df9a091ce571489b8a49d98eda244e9a

		Model: {'id': 'df9a091ce571489b8a49d98eda244e9a', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.194, 'Rank IC': 0.01, 'Rank ICIR': 0.097}, 'data_train_vec': ['2024-05-21', '2025-11-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.097', 'weight': '0.036'}

	Recorder: bc31ad8ef3c4457cbc5c715a81686c58

		Model: {'id': 'bc31ad8ef3c4457cbc5c715a81686c58', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.066, 'ICIR': 0.378, 'Rank IC': 0.022, 'Rank ICIR': 0.117}, 'data_train_vec': ['2025-05-21', '2026-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.117', 'weight': '0.043'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260521_16 721367603410045542 (Recorders: 4/5)

	Recorder: 21e8439939f44db0ba96e5d2a8841c95

		Model: {'id': '21e8439939f44db0ba96e5d2a8841c95', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.035, 'Rank IC': 0.029, 'Rank ICIR': 0.196}, 'data_train_vec': ['2021-05-21', '2025-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.196', 'weight': '0.072'}

	Recorder: c45efa3a82a24054a00f122e2505e822

		Model: {'id': 'c45efa3a82a24054a00f122e2505e822', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.056, 'Rank IC': 0.039, 'Rank ICIR': 0.213}, 'data_train_vec': ['2022-05-21', '2025-05-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.213', 'weight': '0.078'}

	Recorder: 48307bf872a6407f96be0876ee8af06b

		Model: {'id': '48307bf872a6407f96be0876ee8af06b', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.142, 'Rank IC': 0.036, 'Rank ICIR': 0.251}, 'data_train_vec': ['2023-05-21', '2025-08-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.251', 'weight': '0.092'}

	Recorder: d240afc6ddb94e2abbc6086e76644a59

		Model: {'id': 'd240afc6ddb94e2abbc6086e76644a59', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.297, 'Rank IC': 0.014, 'Rank ICIR': 0.081}, 'data_train_vec': ['2025-05-21', '2026-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.081', 'weight': '0.030'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260521_15 268408527220321266 (Recorders: 3/5)

	Recorder: 301febdc104f49509c41f34930739b63

		Model: {'id': '301febdc104f49509c41f34930739b63', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.06, 'Rank IC': 0.029, 'Rank ICIR': 0.264}, 'data_train_vec': ['2021-05-21', '2025-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.264', 'weight': '0.097'}

	Recorder: 9606c6d502ec4ffe859d0909e6ffb4ea

		Model: {'id': '9606c6d502ec4ffe859d0909e6ffb4ea', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.074, 'Rank IC': 0.033, 'Rank ICIR': 0.314}, 'data_train_vec': ['2023-05-21', '2025-08-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.314', 'weight': '0.115'}

	Recorder: 0b818b5272de4ea187d2c4a0d6ac8fbc

		Model: {'id': '0b818b5272de4ea187d2c4a0d6ac8fbc', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.069, 'ICIR': 0.457, 'Rank IC': 0.044, 'Rank ICIR': 0.253}, 'data_train_vec': ['2025-05-21', '2026-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.253', 'weight': '0.093'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260521_15 836667866428706056 (Recorders: 2/5)

	Recorder: ae44bcb9ed4245e6a569821bd7904ed2

		Model: {'id': 'ae44bcb9ed4245e6a569821bd7904ed2', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.095, 'Rank IC': 0.032, 'Rank ICIR': 0.222}, 'data_train_vec': ['2023-05-21', '2025-08-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.222', 'weight': '0.081'}

	Recorder: f9717348215c4bbd97e90470c71c61cc

		Model: {'id': 'f9717348215c4bbd97e90470c71c61cc', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.307, 'Rank IC': 0.028, 'Rank ICIR': 0.201}, 'data_train_vec': ['2025-05-21', '2026-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.201', 'weight': '0.074'}
