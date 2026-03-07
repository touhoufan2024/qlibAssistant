# params 
 {'predict_dates': [{'start': '2026-03-06', 'end': '2026-03-06'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'stock_list': ['SH601699', 'SH601318'], 'model_filter': ['.*'], 'rec_filter': None}



 # model info 

Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260307_17 936797184718326142 (Recorders: 5/5)

	Recorder: 836627a53fb249f4953397e68d4e4410

		Model: {'id': '836627a53fb249f4953397e68d4e4410', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': -0.0, 'ICIR': -0.002, 'Rank IC': 0.014, 'Rank ICIR': 0.099}, 'data_train_vec': ['2021-03-07', '2024-12-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}

	Recorder: fa6d0a0db719411f8ce0dce82a2a8942

		Model: {'id': 'fa6d0a0db719411f8ce0dce82a2a8942', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': -0.009, 'ICIR': -0.05, 'Rank IC': 0.015, 'Rank ICIR': 0.079}, 'data_train_vec': ['2022-03-07', '2025-03-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}

	Recorder: 2e52d768428d46ebad33d689399a94e6

		Model: {'id': '2e52d768428d46ebad33d689399a94e6', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': -0.032, 'ICIR': -0.231, 'Rank IC': -0.008, 'Rank ICIR': -0.049}, 'data_train_vec': ['2023-03-07', '2025-06-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}

	Recorder: b469787b390244cbb1fc18610e0d0607

		Model: {'id': 'b469787b390244cbb1fc18610e0d0607', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.024, 'Rank IC': 0.019, 'Rank ICIR': 0.158}, 'data_train_vec': ['2024-03-07', '2025-09-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}

	Recorder: ed4cdceba84d4208ae7048928ff1454b

		Model: {'id': 'ed4cdceba84d4208ae7048928ff1454b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.063, 'ICIR': 0.425, 'Rank IC': 0.057, 'Rank ICIR': 0.452}, 'data_train_vec': ['2025-03-07', '2025-12-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260307_15 526640513409782119 (Recorders: 5/5)

	Recorder: 8718c610be1f4f12973d8037f0085562

		Model: {'id': '8718c610be1f4f12973d8037f0085562', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.072, 'Rank IC': 0.028, 'Rank ICIR': 0.16}, 'data_train_vec': ['2021-03-07', '2024-12-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}

	Recorder: 9cc9811fe6c74309bac7e13843deba1d

		Model: {'id': '9cc9811fe6c74309bac7e13843deba1d', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': -0.005, 'ICIR': -0.026, 'Rank IC': 0.016, 'Rank ICIR': 0.087}, 'data_train_vec': ['2022-03-07', '2025-03-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}

	Recorder: 130506a639444a8eb3020bd1c018bd14

		Model: {'id': '130506a639444a8eb3020bd1c018bd14', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': -0.04, 'ICIR': -0.249, 'Rank IC': -0.007, 'Rank ICIR': -0.037}, 'data_train_vec': ['2023-03-07', '2025-06-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}

	Recorder: 90846009c22e4090832fda13d82a29db

		Model: {'id': '90846009c22e4090832fda13d82a29db', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.131, 'Rank IC': 0.019, 'Rank ICIR': 0.146}, 'data_train_vec': ['2024-03-07', '2025-09-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}

	Recorder: 2d6a5caa3b6a49ddb35a35fafcabec54

		Model: {'id': '2d6a5caa3b6a49ddb35a35fafcabec54', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.067, 'ICIR': 0.433, 'Rank IC': 0.069, 'Rank ICIR': 0.545}, 'data_train_vec': ['2025-03-07', '2025-12-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260307_15 385483874491468802 (Recorders: 5/5)

	Recorder: dcfe5b327d5848d3bb4b4fae23bb8c66

		Model: {'id': 'dcfe5b327d5848d3bb4b4fae23bb8c66', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.098, 'Rank IC': 0.014, 'Rank ICIR': 0.098}, 'data_train_vec': ['2021-03-07', '2024-12-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}

	Recorder: ca266e6048844d41a8f89dd99968f4b9

		Model: {'id': 'ca266e6048844d41a8f89dd99968f4b9', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.137, 'Rank IC': 0.021, 'Rank ICIR': 0.17}, 'data_train_vec': ['2022-03-07', '2025-03-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}

	Recorder: 76b1e8c9b12f45acb9ecf2fbb6c033b0

		Model: {'id': '76b1e8c9b12f45acb9ecf2fbb6c033b0', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.116, 'Rank IC': 0.015, 'Rank ICIR': 0.104}, 'data_train_vec': ['2023-03-07', '2025-06-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}

	Recorder: c9ef5adcf4504d4088d916d43b05ed84

		Model: {'id': 'c9ef5adcf4504d4088d916d43b05ed84', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.246, 'Rank IC': 0.021, 'Rank ICIR': 0.179}, 'data_train_vec': ['2024-03-07', '2025-09-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}

	Recorder: 30865b6d19af4ef7b0f02ed08d4c72e4

		Model: {'id': '30865b6d19af4ef7b0f02ed08d4c72e4', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.063, 'ICIR': 0.615, 'Rank IC': 0.04, 'Rank ICIR': 0.476}, 'data_train_vec': ['2025-03-07', '2025-12-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260307_15 204530792627898320 (Recorders: 5/5)

	Recorder: 06986749eccc47fab39aecb54a611b83

		Model: {'id': '06986749eccc47fab39aecb54a611b83', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.06, 'Rank IC': 0.023, 'Rank ICIR': 0.125}, 'data_train_vec': ['2021-03-07', '2024-12-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}

	Recorder: c75212c8894a463a8069f8d369e7b592

		Model: {'id': 'c75212c8894a463a8069f8d369e7b592', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': -0.007, 'ICIR': -0.041, 'Rank IC': 0.019, 'Rank ICIR': 0.101}, 'data_train_vec': ['2022-03-07', '2025-03-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}

	Recorder: c9cce0d3004f4c18adf5d79f9d349b98

		Model: {'id': 'c9cce0d3004f4c18adf5d79f9d349b98', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': -0.049, 'ICIR': -0.321, 'Rank IC': -0.012, 'Rank ICIR': -0.067}, 'data_train_vec': ['2023-03-07', '2025-06-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}

	Recorder: 44f16bdb149c4a4eb9650e5aa0305642

		Model: {'id': '44f16bdb149c4a4eb9650e5aa0305642', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': -0.009, 'ICIR': -0.074, 'Rank IC': 0.003, 'Rank ICIR': 0.02}, 'data_train_vec': ['2024-03-07', '2025-09-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}

	Recorder: b13508b22ebd48a792164d8c58c2103a

		Model: {'id': 'b13508b22ebd48a792164d8c58c2103a', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.257, 'Rank IC': 0.053, 'Rank ICIR': 0.408}, 'data_train_vec': ['2025-03-07', '2025-12-06'], 'train_time_vec': ['2026-03-07', '2026-03-07']}
