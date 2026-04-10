# params 
 {'predict_dates': [{'start': '2026-04-10', 'end': '2026-04-10'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260410_16 338651135085769870 (Recorders: 3/5)

	Recorder: d14a5dad983648bb930ed7da8a1951fe

		Model: {'id': 'd14a5dad983648bb930ed7da8a1951fe', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.202, 'Rank IC': 0.036, 'Rank ICIR': 0.222}, 'data_train_vec': ['2023-04-10', '2025-07-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.222', 'weight': '0.080'}

	Recorder: ca7a593434fd4cfd8d85796f9e6ac5f6

		Model: {'id': 'ca7a593434fd4cfd8d85796f9e6ac5f6', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.085, 'Rank IC': 0.028, 'Rank ICIR': 0.207}, 'data_train_vec': ['2024-04-10', '2025-10-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.207', 'weight': '0.074'}

	Recorder: 5cbd61f7adcc4b98a643447410f76356

		Model: {'id': '5cbd61f7adcc4b98a643447410f76356', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.097, 'Rank IC': 0.003, 'Rank ICIR': 0.025}, 'data_train_vec': ['2025-04-10', '2026-01-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.025', 'weight': '0.009'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260410_16 781882965368106563 (Recorders: 1/5)

	Recorder: 8df95ff9a2604c56998a78a5c6e0b606

		Model: {'id': '8df95ff9a2604c56998a78a5c6e0b606', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.326, 'Rank IC': 0.044, 'Rank ICIR': 0.391}, 'data_train_vec': ['2024-04-10', '2025-10-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.391', 'weight': '0.140'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260410_13 924883936059816378 (Recorders: 3/5)

	Recorder: ea6f0f0fc0f845c381dfe531c32e92f1

		Model: {'id': 'ea6f0f0fc0f845c381dfe531c32e92f1', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.063, 'Rank IC': 0.029, 'Rank ICIR': 0.166}, 'data_train_vec': ['2021-04-10', '2025-01-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.166', 'weight': '0.060'}

	Recorder: d4408e4bce2a4560b853a77444b412c4

		Model: {'id': 'd4408e4bce2a4560b853a77444b412c4', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.108, 'Rank IC': 0.048, 'Rank ICIR': 0.269}, 'data_train_vec': ['2023-04-10', '2025-07-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.269', 'weight': '0.097'}

	Recorder: 7f78c4f60226431185dc24200ace7471

		Model: {'id': '7f78c4f60226431185dc24200ace7471', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.204, 'Rank IC': 0.023, 'Rank ICIR': 0.202}, 'data_train_vec': ['2024-04-10', '2025-10-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.202', 'weight': '0.073'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260410_13 208766614496047186 (Recorders: 5/5)

	Recorder: 0c2937e12d2745709716ad4b8c6c6066

		Model: {'id': '0c2937e12d2745709716ad4b8c6c6066', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.088, 'Rank IC': 0.021, 'Rank ICIR': 0.17}, 'data_train_vec': ['2021-04-10', '2025-01-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.170', 'weight': '0.061'}

	Recorder: 931f7781e4084220b853614f985bfef1

		Model: {'id': '931f7781e4084220b853614f985bfef1', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.017, 'Rank IC': 0.019, 'Rank ICIR': 0.167}, 'data_train_vec': ['2022-04-10', '2025-04-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.167', 'weight': '0.060'}

	Recorder: 34cc91884b6941128ca7d886a3815a05

		Model: {'id': '34cc91884b6941128ca7d886a3815a05', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.12, 'Rank IC': 0.038, 'Rank ICIR': 0.327}, 'data_train_vec': ['2023-04-10', '2025-07-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.327', 'weight': '0.117'}

	Recorder: ddd9cb3397fd42a48f51b025a6c1cc81

		Model: {'id': 'ddd9cb3397fd42a48f51b025a6c1cc81', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.055, 'Rank IC': 0.008, 'Rank ICIR': 0.064}, 'data_train_vec': ['2024-04-10', '2025-10-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.064', 'weight': '0.023'}

	Recorder: c5c6a19f6d6d49c78940ace4873cf535

		Model: {'id': 'c5c6a19f6d6d49c78940ace4873cf535', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.081, 'Rank IC': 0.003, 'Rank ICIR': 0.019}, 'data_train_vec': ['2025-04-10', '2026-01-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.019', 'weight': '0.007'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260410_13 752322029329923025 (Recorders: 3/5)

	Recorder: 59e3f335dcea43f6ad34bc52bccdba53

		Model: {'id': '59e3f335dcea43f6ad34bc52bccdba53', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.035, 'Rank IC': 0.018, 'Rank ICIR': 0.097}, 'data_train_vec': ['2021-04-10', '2025-01-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.097', 'weight': '0.035'}

	Recorder: 0786e45938dd4162b0cb6435c527c233

		Model: {'id': '0786e45938dd4162b0cb6435c527c233', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.019, 'Rank IC': 0.031, 'Rank ICIR': 0.173}, 'data_train_vec': ['2023-04-10', '2025-07-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.173', 'weight': '0.062'}

	Recorder: 6df56782832845b2b21c12f0d3f96b44

		Model: {'id': '6df56782832845b2b21c12f0d3f96b44', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.07, 'Rank IC': 0.034, 'Rank ICIR': 0.284}, 'data_train_vec': ['2024-04-10', '2025-10-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.284', 'weight': '0.102'}
