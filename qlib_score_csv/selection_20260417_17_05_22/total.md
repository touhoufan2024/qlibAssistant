# params 
 {'predict_dates': [{'start': '2026-04-17', 'end': '2026-04-17'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260417_16 373110221315755181 (Recorders: 3/5)

	Recorder: be2edb15a0224d38a89305e3e781baf2

		Model: {'id': 'be2edb15a0224d38a89305e3e781baf2', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.162, 'Rank IC': 0.033, 'Rank ICIR': 0.21}, 'data_train_vec': ['2023-04-17', '2025-07-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.210', 'weight': '0.083'}

	Recorder: 74227b318dfa4c38a867b324ab943a40

		Model: {'id': '74227b318dfa4c38a867b324ab943a40', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.059, 'Rank IC': 0.034, 'Rank ICIR': 0.261}, 'data_train_vec': ['2024-04-17', '2025-10-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.261', 'weight': '0.103'}

	Recorder: 6eeb908d7deb47e3a6a2fdca7752361d

		Model: {'id': '6eeb908d7deb47e3a6a2fdca7752361d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.21, 'Rank IC': 0.033, 'Rank ICIR': 0.243}, 'data_train_vec': ['2025-04-17', '2026-01-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.243', 'weight': '0.096'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260417_16 418239203738553900 (Recorders: 2/5)

	Recorder: a37f79da503d4022a80b3f07ddce6764

		Model: {'id': 'a37f79da503d4022a80b3f07ddce6764', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.157, 'Rank IC': 0.031, 'Rank ICIR': 0.243}, 'data_train_vec': ['2024-04-17', '2025-10-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.243', 'weight': '0.096'}

	Recorder: 921a4b658db74d3d90cf4920cbff4f94

		Model: {'id': '921a4b658db74d3d90cf4920cbff4f94', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.379, 'Rank IC': 0.031, 'Rank ICIR': 0.244}, 'data_train_vec': ['2025-04-17', '2026-01-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.244', 'weight': '0.096'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260417_14 494904714884521928 (Recorders: 4/5)

	Recorder: 6680dda0351241898af54291e24d633f

		Model: {'id': '6680dda0351241898af54291e24d633f', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.019, 'Rank IC': 0.022, 'Rank ICIR': 0.128}, 'data_train_vec': ['2021-04-17', '2025-01-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.128', 'weight': '0.050'}

	Recorder: 608d9bcab1b24bdf850bcfca7f07a64e

		Model: {'id': '608d9bcab1b24bdf850bcfca7f07a64e', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.046, 'Rank IC': 0.038, 'Rank ICIR': 0.233}, 'data_train_vec': ['2023-04-17', '2025-07-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.233', 'weight': '0.092'}

	Recorder: b6b00ad481a147aab6fbb91da4610135

		Model: {'id': 'b6b00ad481a147aab6fbb91da4610135', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.062, 'Rank IC': 0.019, 'Rank ICIR': 0.148}, 'data_train_vec': ['2024-04-17', '2025-10-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.148', 'weight': '0.058'}

	Recorder: 4920db5edac34913ac1368045cc59121

		Model: {'id': '4920db5edac34913ac1368045cc59121', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.2, 'Rank IC': 0.021, 'Rank ICIR': 0.112}, 'data_train_vec': ['2025-04-17', '2026-01-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.112', 'weight': '0.044'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260417_14 248348368956954340 (Recorders: 2/5)

	Recorder: d142bc03130b483788f86d9c1492a49e

		Model: {'id': 'd142bc03130b483788f86d9c1492a49e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.001, 'ICIR': 0.008, 'Rank IC': 0.014, 'Rank ICIR': 0.123}, 'data_train_vec': ['2021-04-17', '2025-01-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.123', 'weight': '0.049'}

	Recorder: db28300ca6b945cfb7b0f355caf56ccd

		Model: {'id': 'db28300ca6b945cfb7b0f355caf56ccd', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.365, 'Rank IC': 0.04, 'Rank ICIR': 0.271}, 'data_train_vec': ['2025-04-17', '2026-01-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.271', 'weight': '0.107'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260417_13 417891125594863648 (Recorders: 2/5)

	Recorder: 1cb6a4d66c2749fd8fd0f5ad0088241a

		Model: {'id': '1cb6a4d66c2749fd8fd0f5ad0088241a', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.125, 'Rank IC': 0.028, 'Rank ICIR': 0.263}, 'data_train_vec': ['2024-04-17', '2025-10-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.263', 'weight': '0.104'}

	Recorder: 5a8373b07fd44a3ea6cbdfc29a162133

		Model: {'id': '5a8373b07fd44a3ea6cbdfc29a162133', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.102, 'Rank IC': 0.009, 'Rank ICIR': 0.056}, 'data_train_vec': ['2025-04-17', '2026-01-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.056', 'weight': '0.022'}
