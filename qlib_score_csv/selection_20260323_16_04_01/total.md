# params 
 {'predict_dates': [{'start': '2026-03-23', 'end': '2026-03-23'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260323_14 897418937149029200 (Recorders: 3/5)

	Recorder: 29d0f3b3c7df4c74bd06694c9b6e19e6

		Model: {'id': '29d0f3b3c7df4c74bd06694c9b6e19e6', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.055, 'Rank IC': 0.023, 'Rank ICIR': 0.152}, 'data_train_vec': ['2021-03-23', '2024-12-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.152', 'weight': '0.035'}

	Recorder: cd6a6b4f140f470b8e29fac51194246a

		Model: {'id': 'cd6a6b4f140f470b8e29fac51194246a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.165, 'Rank IC': 0.058, 'Rank ICIR': 0.37}, 'data_train_vec': ['2024-03-23', '2025-09-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.370', 'weight': '0.084'}

	Recorder: 1a4f5f3f997d4add8be3137817c64f2b

		Model: {'id': '1a4f5f3f997d4add8be3137817c64f2b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.137, 'Rank IC': 0.038, 'Rank ICIR': 0.285}, 'data_train_vec': ['2025-03-23', '2025-12-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.285', 'weight': '0.065'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260323_14 747271722629975990 (Recorders: 2/5)

	Recorder: 7f1a86a4df1342cb9bd5d98d8a0cbff1

		Model: {'id': '7f1a86a4df1342cb9bd5d98d8a0cbff1', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.067, 'Rank IC': 0.031, 'Rank ICIR': 0.192}, 'data_train_vec': ['2021-03-23', '2024-12-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.192', 'weight': '0.044'}

	Recorder: 14e0528743b34bc1a8dbcc50b8d9c52c

		Model: {'id': '14e0528743b34bc1a8dbcc50b8d9c52c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.268, 'Rank IC': 0.044, 'Rank ICIR': 0.383}, 'data_train_vec': ['2024-03-23', '2025-09-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.383', 'weight': '0.087'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260323_12 614901156375732029 (Recorders: 3/5)

	Recorder: c164cf36ad2b48b6849fef3319d64163

		Model: {'id': 'c164cf36ad2b48b6849fef3319d64163', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.106, 'Rank IC': 0.032, 'Rank ICIR': 0.188}, 'data_train_vec': ['2021-03-23', '2024-12-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.188', 'weight': '0.043'}

	Recorder: 43d9b3977bc84314b809fe47fc14bd11

		Model: {'id': '43d9b3977bc84314b809fe47fc14bd11', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.011, 'Rank IC': 0.039, 'Rank ICIR': 0.218}, 'data_train_vec': ['2023-03-23', '2025-06-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.218', 'weight': '0.050'}

	Recorder: 6900c415015d4e11a04fe166a9d3543a

		Model: {'id': '6900c415015d4e11a04fe166a9d3543a', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.263, 'Rank IC': 0.044, 'Rank ICIR': 0.378}, 'data_train_vec': ['2024-03-23', '2025-09-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.378', 'weight': '0.086'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260323_12 897375108427233154 (Recorders: 5/5)

	Recorder: 98222f47dba94ed58325c22850eb0b88

		Model: {'id': '98222f47dba94ed58325c22850eb0b88', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.16, 'Rank IC': 0.026, 'Rank ICIR': 0.231}, 'data_train_vec': ['2021-03-23', '2024-12-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.231', 'weight': '0.053'}

	Recorder: a695ef16d6ed46cbb5b74a9a9878421a

		Model: {'id': 'a695ef16d6ed46cbb5b74a9a9878421a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.061, 'Rank IC': 0.02, 'Rank ICIR': 0.174}, 'data_train_vec': ['2022-03-23', '2025-03-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.174', 'weight': '0.040'}

	Recorder: 0826e7cf36334dd1943d8d0bf17de24f

		Model: {'id': '0826e7cf36334dd1943d8d0bf17de24f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.122, 'Rank IC': 0.038, 'Rank ICIR': 0.344}, 'data_train_vec': ['2023-03-23', '2025-06-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.344', 'weight': '0.079'}

	Recorder: 713c59038ace462eab63d7a21197390f

		Model: {'id': '713c59038ace462eab63d7a21197390f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.126, 'Rank IC': 0.021, 'Rank ICIR': 0.18}, 'data_train_vec': ['2024-03-23', '2025-09-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.180', 'weight': '0.041'}

	Recorder: a6a3f5d849de4c159c8f83263a6fde45

		Model: {'id': 'a6a3f5d849de4c159c8f83263a6fde45', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.162, 'Rank IC': 0.026, 'Rank ICIR': 0.269}, 'data_train_vec': ['2025-03-23', '2025-12-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.269', 'weight': '0.061'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260323_11 948710344825594835 (Recorders: 3/5)

	Recorder: 299bf7437b284dd7944a35e954f7b993

		Model: {'id': '299bf7437b284dd7944a35e954f7b993', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.067, 'Rank IC': 0.033, 'Rank ICIR': 0.196}, 'data_train_vec': ['2021-03-23', '2024-12-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.196', 'weight': '0.045'}

	Recorder: 3bb5a118203546b7989d80ef1bc28e53

		Model: {'id': '3bb5a118203546b7989d80ef1bc28e53', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.251, 'Rank IC': 0.048, 'Rank ICIR': 0.454}, 'data_train_vec': ['2024-03-23', '2025-09-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.454', 'weight': '0.104'}

	Recorder: 3ff4596475ce499aaa0545d4824f4ce7

		Model: {'id': '3ff4596475ce499aaa0545d4824f4ce7', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.251, 'Rank IC': 0.022, 'Rank ICIR': 0.365}, 'data_train_vec': ['2025-03-23', '2025-12-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.365', 'weight': '0.083'}
