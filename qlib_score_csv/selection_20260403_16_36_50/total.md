# params 
 {'predict_dates': [{'start': '2026-04-03', 'end': '2026-04-03'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260403_16 125038909126571750 (Recorders: 3/5)

	Recorder: 04d3755cbb854288a2ef5f4f5f8ce407

		Model: {'id': '04d3755cbb854288a2ef5f4f5f8ce407', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.077, 'Rank IC': 0.027, 'Rank ICIR': 0.153}, 'data_train_vec': ['2021-04-03', '2025-01-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.153', 'weight': '0.047'}

	Recorder: e8998f6c23884489a3cdcc1938fee532

		Model: {'id': 'e8998f6c23884489a3cdcc1938fee532', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.204, 'Rank IC': 0.048, 'Rank ICIR': 0.324}, 'data_train_vec': ['2023-04-03', '2025-07-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.324', 'weight': '0.099'}

	Recorder: 17b64d7f93ff4c998525adf8d680b75f

		Model: {'id': '17b64d7f93ff4c998525adf8d680b75f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.13, 'Rank IC': 0.047, 'Rank ICIR': 0.392}, 'data_train_vec': ['2024-04-03', '2025-10-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.392', 'weight': '0.119'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260403_16 764359730976145055 (Recorders: 3/5)

	Recorder: 3704bbc3df1d478fbf1146a487b45542

		Model: {'id': '3704bbc3df1d478fbf1146a487b45542', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.027, 'Rank IC': 0.029, 'Rank ICIR': 0.178}, 'data_train_vec': ['2021-04-03', '2025-01-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.178', 'weight': '0.054'}

	Recorder: b96fdb9947704868b5729fd389c50726

		Model: {'id': 'b96fdb9947704868b5729fd389c50726', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.063, 'Rank IC': 0.052, 'Rank ICIR': 0.305}, 'data_train_vec': ['2023-04-03', '2025-07-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.305', 'weight': '0.093'}

	Recorder: 7e0c64e5b8084ba6b859b5e66b234f0d

		Model: {'id': '7e0c64e5b8084ba6b859b5e66b234f0d', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.181, 'Rank IC': 0.027, 'Rank ICIR': 0.234}, 'data_train_vec': ['2024-04-03', '2025-10-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.234', 'weight': '0.071'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260403_13 598296739202265186 (Recorders: 3/5)

	Recorder: 8c587e58389344dc871d36a7ed0213dc

		Model: {'id': '8c587e58389344dc871d36a7ed0213dc', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.115, 'Rank IC': 0.041, 'Rank ICIR': 0.216}, 'data_train_vec': ['2021-04-03', '2025-01-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.216', 'weight': '0.066'}

	Recorder: 7e7af6c6301c4516b94a7d8b906886ae

		Model: {'id': '7e7af6c6301c4516b94a7d8b906886ae', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.081, 'Rank IC': 0.049, 'Rank ICIR': 0.291}, 'data_train_vec': ['2023-04-03', '2025-07-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.291', 'weight': '0.089'}

	Recorder: 861e6fdbe7b04802be601a8391e9f119

		Model: {'id': '861e6fdbe7b04802be601a8391e9f119', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.262, 'Rank IC': 0.032, 'Rank ICIR': 0.312}, 'data_train_vec': ['2024-04-03', '2025-10-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.312', 'weight': '0.095'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260403_13 525042617102264866 (Recorders: 3/5)

	Recorder: 15d0807ba8dd4870a16812271e2f453d

		Model: {'id': '15d0807ba8dd4870a16812271e2f453d', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.106, 'Rank IC': 0.024, 'Rank ICIR': 0.199}, 'data_train_vec': ['2021-04-03', '2025-01-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.199', 'weight': '0.061'}

	Recorder: 8f2cd3cebc7b490aac5a3042d50b375c

		Model: {'id': '8f2cd3cebc7b490aac5a3042d50b375c', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.028, 'Rank IC': 0.021, 'Rank ICIR': 0.177}, 'data_train_vec': ['2022-04-03', '2025-04-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.177', 'weight': '0.054'}

	Recorder: f7250332dc794904bbadd0d2e6b7cdaf

		Model: {'id': 'f7250332dc794904bbadd0d2e6b7cdaf', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.097, 'Rank IC': 0.039, 'Rank ICIR': 0.33}, 'data_train_vec': ['2023-04-03', '2025-07-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.330', 'weight': '0.100'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260403_13 239247772677205538 (Recorders: 1/5)

	Recorder: bdb3b99e426048b98895a3f093aba2af

		Model: {'id': 'bdb3b99e426048b98895a3f093aba2af', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.043, 'Rank IC': 0.031, 'Rank ICIR': 0.175}, 'data_train_vec': ['2022-04-03', '2025-04-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.175', 'weight': '0.053'}
