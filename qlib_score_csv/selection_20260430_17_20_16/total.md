# params 
 {'predict_dates': [{'start': '2026-04-30', 'end': '2026-04-30'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260430_16 901553647828017678 (Recorders: 2/5)

	Recorder: cb0a38f3203742d386c6be428e0b121d

		Model: {'id': 'cb0a38f3203742d386c6be428e0b121d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.06, 'Rank IC': 0.013, 'Rank ICIR': 0.127}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.127', 'weight': '0.087'}

	Recorder: 1293f8a59848407286d719995bdf8d0d

		Model: {'id': '1293f8a59848407286d719995bdf8d0d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.406, 'Rank IC': 0.019, 'Rank ICIR': 0.167}, 'data_train_vec': ['2025-04-30', '2026-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.167', 'weight': '0.114'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260430_16 316548977861471618 (Recorders: 2/5)

	Recorder: 19013ec27e4d43ffb8fedf0e8f28325f

		Model: {'id': '19013ec27e4d43ffb8fedf0e8f28325f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.058, 'Rank IC': 0.01, 'Rank ICIR': 0.086}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.086', 'weight': '0.059'}

	Recorder: ff263b6b2b184f599e788a5d20123d3e

		Model: {'id': 'ff263b6b2b184f599e788a5d20123d3e', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.075, 'ICIR': 0.643, 'Rank IC': 0.035, 'Rank ICIR': 0.287}, 'data_train_vec': ['2025-04-30', '2026-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.287', 'weight': '0.196'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260430_14 719361138654614318 (Recorders: 2/5)

	Recorder: 8c0ddd4a018a47b5af651dee46613f51

		Model: {'id': '8c0ddd4a018a47b5af651dee46613f51', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.072, 'Rank IC': 0.003, 'Rank ICIR': 0.026}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.026', 'weight': '0.018'}

	Recorder: d998fcee7f3b4c1d8235784826e347f1

		Model: {'id': 'd998fcee7f3b4c1d8235784826e347f1', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.291, 'Rank IC': 0.012, 'Rank ICIR': 0.086}, 'data_train_vec': ['2025-04-30', '2026-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.086', 'weight': '0.059'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260430_14 354958427732845483 (Recorders: 2/5)

	Recorder: 225973345dd44d66b4957a9cdeb8b424

		Model: {'id': '225973345dd44d66b4957a9cdeb8b424', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.022, 'Rank IC': 0.009, 'Rank ICIR': 0.072}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.072', 'weight': '0.049'}

	Recorder: 6e6cfe15dffd495cb6a71199b47cd851

		Model: {'id': '6e6cfe15dffd495cb6a71199b47cd851', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.057, 'ICIR': 0.598, 'Rank IC': 0.03, 'Rank ICIR': 0.273}, 'data_train_vec': ['2025-04-30', '2026-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.273', 'weight': '0.187'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260430_14 435927408757148635 (Recorders: 3/5)

	Recorder: 403b3c628b234b3faca2d257ea38b023

		Model: {'id': '403b3c628b234b3faca2d257ea38b023', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.043, 'Rank IC': 0.013, 'Rank ICIR': 0.075}, 'data_train_vec': ['2021-04-30', '2025-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.075', 'weight': '0.051'}

	Recorder: 3cf1d488d1fb47c682e28ca1f36d1bee

		Model: {'id': '3cf1d488d1fb47c682e28ca1f36d1bee', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.049, 'Rank IC': 0.017, 'Rank ICIR': 0.145}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.145', 'weight': '0.099'}

	Recorder: d402d6469c464b7fb677652a16a5e4b8

		Model: {'id': 'd402d6469c464b7fb677652a16a5e4b8', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.271, 'Rank IC': 0.01, 'Rank ICIR': 0.118}, 'data_train_vec': ['2025-04-30', '2026-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.118', 'weight': '0.081'}
