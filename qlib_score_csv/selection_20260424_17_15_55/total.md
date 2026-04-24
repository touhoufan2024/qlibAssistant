# params 
 {'predict_dates': [{'start': '2026-04-24', 'end': '2026-04-24'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260424_16 640431422994292870 (Recorders: 3/5)

	Recorder: 1f3d470976984f71a7c436d88944210c

		Model: {'id': '1f3d470976984f71a7c436d88944210c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.204, 'Rank IC': 0.054, 'Rank ICIR': 0.343}, 'data_train_vec': ['2023-04-24', '2025-07-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.343', 'weight': '0.165'}

	Recorder: 3a4ea264535441c287ff91f90e6decbf

		Model: {'id': '3a4ea264535441c287ff91f90e6decbf', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.157, 'Rank IC': 0.018, 'Rank ICIR': 0.144}, 'data_train_vec': ['2024-04-24', '2025-10-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.144', 'weight': '0.069'}

	Recorder: 66106dee868b4ec8a55e83f6cfcf130d

		Model: {'id': '66106dee868b4ec8a55e83f6cfcf130d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.172, 'Rank IC': 0.013, 'Rank ICIR': 0.073}, 'data_train_vec': ['2025-04-24', '2026-01-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.073', 'weight': '0.035'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260424_16 243182061252622866 (Recorders: 2/5)

	Recorder: 8a58e7b777854403b273c037c8fa1324

		Model: {'id': '8a58e7b777854403b273c037c8fa1324', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.26, 'Rank IC': 0.032, 'Rank ICIR': 0.277}, 'data_train_vec': ['2024-04-24', '2025-10-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.277', 'weight': '0.133'}

	Recorder: 97df49adefc043e1af1a4b0f7948bfe3

		Model: {'id': '97df49adefc043e1af1a4b0f7948bfe3', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.423, 'Rank IC': 0.012, 'Rank ICIR': 0.094}, 'data_train_vec': ['2025-04-24', '2026-01-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.094', 'weight': '0.045'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260424_14 900254022338788387 (Recorders: 2/5)

	Recorder: 6976e8b0f77b43ebba47bb8a129dc1f5

		Model: {'id': '6976e8b0f77b43ebba47bb8a129dc1f5', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.065, 'Rank IC': 0.045, 'Rank ICIR': 0.249}, 'data_train_vec': ['2023-04-24', '2025-07-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.249', 'weight': '0.119'}

	Recorder: d3e97aaa2fa24f3d938fe6cba1f61b57

		Model: {'id': 'd3e97aaa2fa24f3d938fe6cba1f61b57', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.076, 'Rank IC': 0.013, 'Rank ICIR': 0.105}, 'data_train_vec': ['2024-04-24', '2025-10-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.105', 'weight': '0.050'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260424_14 435784834236014029 (Recorders: 2/5)

	Recorder: a1348239753b4f3a99014bb439eb4bfa

		Model: {'id': 'a1348239753b4f3a99014bb439eb4bfa', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.017, 'Rank IC': 0.008, 'Rank ICIR': 0.065}, 'data_train_vec': ['2024-04-24', '2025-10-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.065', 'weight': '0.031'}

	Recorder: e51592e6e91a4c039e217c9aa6dcf062

		Model: {'id': 'e51592e6e91a4c039e217c9aa6dcf062', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.436, 'Rank IC': 0.022, 'Rank ICIR': 0.161}, 'data_train_vec': ['2025-04-24', '2026-01-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.161', 'weight': '0.077'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260424_14 843706657573616925 (Recorders: 3/5)

	Recorder: b780392317b34a5fb6d3aaa50b9f2c48

		Model: {'id': 'b780392317b34a5fb6d3aaa50b9f2c48', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.07, 'Rank IC': 0.041, 'Rank ICIR': 0.237}, 'data_train_vec': ['2023-04-24', '2025-07-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.237', 'weight': '0.114'}

	Recorder: 47baeca7ebfe41f5941cfcb630fc51a3

		Model: {'id': '47baeca7ebfe41f5941cfcb630fc51a3', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.111, 'Rank IC': 0.032, 'Rank ICIR': 0.306}, 'data_train_vec': ['2024-04-24', '2025-10-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.306', 'weight': '0.147'}

	Recorder: 4100a73d46724b9283b6b94ffbe2f36b

		Model: {'id': '4100a73d46724b9283b6b94ffbe2f36b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.25, 'Rank IC': 0.005, 'Rank ICIR': 0.031}, 'data_train_vec': ['2025-04-24', '2026-01-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.031', 'weight': '0.015'}
