# params 
 {'predict_dates': [{'start': '2026-04-28', 'end': '2026-04-28'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260428_17 237546213101783488 (Recorders: 3/5)

	Recorder: 1930fd4daf7345a1a525e6d5d77b35e7

		Model: {'id': '1930fd4daf7345a1a525e6d5d77b35e7', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.075, 'Rank IC': 0.027, 'Rank ICIR': 0.191}, 'data_train_vec': ['2023-04-28', '2025-07-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.191', 'weight': '0.070'}

	Recorder: 7d8e5a8a4beb448c8889228948de32a5

		Model: {'id': '7d8e5a8a4beb448c8889228948de32a5', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.082, 'Rank IC': 0.017, 'Rank ICIR': 0.169}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.169', 'weight': '0.062'}

	Recorder: 0a2cb5a54aef4c58bf7a7a10cf05b468

		Model: {'id': '0a2cb5a54aef4c58bf7a7a10cf05b468', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.288, 'Rank IC': 0.036, 'Rank ICIR': 0.269}, 'data_train_vec': ['2025-04-28', '2026-01-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.269', 'weight': '0.098'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260428_17 854649938114371758 (Recorders: 3/5)

	Recorder: 04aefa898b0340b187514502613aa90b

		Model: {'id': '04aefa898b0340b187514502613aa90b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.085, 'Rank IC': 0.032, 'Rank ICIR': 0.208}, 'data_train_vec': ['2023-04-28', '2025-07-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.208', 'weight': '0.076'}

	Recorder: 52f58250f0e44597aebeab03a975dff8

		Model: {'id': '52f58250f0e44597aebeab03a975dff8', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.086, 'Rank IC': 0.013, 'Rank ICIR': 0.118}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.118', 'weight': '0.043'}

	Recorder: d8abc2fc905a4511b75a30fa35088d3a

		Model: {'id': 'd8abc2fc905a4511b75a30fa35088d3a', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.056, 'ICIR': 0.424, 'Rank IC': 0.03, 'Rank ICIR': 0.214}, 'data_train_vec': ['2025-04-28', '2026-01-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.214', 'weight': '0.078'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260428_14 429165569711613501 (Recorders: 3/5)

	Recorder: 4eace5aa4d0f477fb3c1412e8e9f5c71

		Model: {'id': '4eace5aa4d0f477fb3c1412e8e9f5c71', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.082, 'Rank IC': 0.044, 'Rank ICIR': 0.269}, 'data_train_vec': ['2023-04-28', '2025-07-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.269', 'weight': '0.098'}

	Recorder: 4c18f6f5d0ab4e3c9f45c08ca7e44b9c

		Model: {'id': '4c18f6f5d0ab4e3c9f45c08ca7e44b9c', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.078, 'Rank IC': 0.008, 'Rank ICIR': 0.072}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.072', 'weight': '0.026'}

	Recorder: ba73934d5a9849d0ac8a56dd51a06b64

		Model: {'id': 'ba73934d5a9849d0ac8a56dd51a06b64', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.148, 'Rank IC': 0.008, 'Rank ICIR': 0.043}, 'data_train_vec': ['2025-04-28', '2026-01-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.043', 'weight': '0.016'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260428_14 873119431811034962 (Recorders: 3/5)

	Recorder: d998034870fb4d3984d1e5fc17411da9

		Model: {'id': 'd998034870fb4d3984d1e5fc17411da9', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.03, 'Rank IC': 0.029, 'Rank ICIR': 0.246}, 'data_train_vec': ['2023-04-28', '2025-07-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.246', 'weight': '0.090'}

	Recorder: 2e982020a3ef46ad8a8968ce8d52afe4

		Model: {'id': '2e982020a3ef46ad8a8968ce8d52afe4', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.013, 'Rank IC': 0.009, 'Rank ICIR': 0.075}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.075', 'weight': '0.027'}

	Recorder: 5a22dca767b94483956a12617a6df297

		Model: {'id': '5a22dca767b94483956a12617a6df297', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.066, 'ICIR': 0.579, 'Rank IC': 0.043, 'Rank ICIR': 0.328}, 'data_train_vec': ['2025-04-28', '2026-01-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.328', 'weight': '0.120'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260428_14 113571789890727714 (Recorders: 3/5)

	Recorder: 05e4ada315e648e8927abc793cf39583

		Model: {'id': '05e4ada315e648e8927abc793cf39583', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.001, 'ICIR': 0.009, 'Rank IC': 0.018, 'Rank ICIR': 0.102}, 'data_train_vec': ['2021-04-28', '2025-01-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.102', 'weight': '0.037'}

	Recorder: be0b56ee0ef14d359096b58c805b16c5

		Model: {'id': 'be0b56ee0ef14d359096b58c805b16c5', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.074, 'Rank IC': 0.037, 'Rank ICIR': 0.224}, 'data_train_vec': ['2023-04-28', '2025-07-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.224', 'weight': '0.082'}

	Recorder: dd19561e60054b7498d7251219bff0a1

		Model: {'id': 'dd19561e60054b7498d7251219bff0a1', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.075, 'Rank IC': 0.024, 'Rank ICIR': 0.207}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.207', 'weight': '0.076'}
