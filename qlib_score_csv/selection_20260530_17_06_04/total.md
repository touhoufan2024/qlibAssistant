# params 
 {'predict_dates': [{'start': '2026-05-29', 'end': '2026-05-29'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260530_16 268019715256022801 (Recorders: 4/5)

	Recorder: 46672becda914c629cef9f012acd0622

		Model: {'id': '46672becda914c629cef9f012acd0622', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.012, 'Rank IC': 0.022, 'Rank ICIR': 0.15}, 'data_train_vec': ['2021-05-28', '2025-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.150', 'weight': '0.054'}

	Recorder: 5a5012d28fee4aebaaeb48cd4b1b3449

		Model: {'id': '5a5012d28fee4aebaaeb48cd4b1b3449', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.001, 'ICIR': 0.008, 'Rank IC': 0.019, 'Rank ICIR': 0.137}, 'data_train_vec': ['2022-05-30', '2025-05-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.137', 'weight': '0.050'}

	Recorder: 6b249c24816946e7b0f773fd958ca60a

		Model: {'id': '6b249c24816946e7b0f773fd958ca60a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.31, 'Rank IC': 0.029, 'Rank ICIR': 0.196}, 'data_train_vec': ['2023-05-28', '2025-08-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.196', 'weight': '0.071'}

	Recorder: 961bf75e429e477ea89980ba9d0ccc2a

		Model: {'id': '961bf75e429e477ea89980ba9d0ccc2a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.245, 'Rank IC': 0.012, 'Rank ICIR': 0.058}, 'data_train_vec': ['2025-05-28', '2026-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.058', 'weight': '0.021'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260530_16 243545606830577628 (Recorders: 3/5)

	Recorder: 77a891bbd8874460953b5a84081326d5

		Model: {'id': '77a891bbd8874460953b5a84081326d5', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.16, 'Rank IC': 0.027, 'Rank ICIR': 0.189}, 'data_train_vec': ['2023-05-28', '2025-08-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.189', 'weight': '0.069'}

	Recorder: a84897bc391b42b6b54a640c6672d256

		Model: {'id': 'a84897bc391b42b6b54a640c6672d256', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.081, 'Rank IC': 0.009, 'Rank ICIR': 0.083}, 'data_train_vec': ['2024-05-30', '2025-11-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.083', 'weight': '0.030'}

	Recorder: bec6eafcfc6040148d43f8e5f5e20b65

		Model: {'id': 'bec6eafcfc6040148d43f8e5f5e20b65', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.076, 'ICIR': 0.34, 'Rank IC': 0.03, 'Rank ICIR': 0.135}, 'data_train_vec': ['2025-05-28', '2026-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.135', 'weight': '0.049'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260530_14 774059685242022728 (Recorders: 3/5)

	Recorder: 8ebee4b5f04b4a378cd415764449e957

		Model: {'id': '8ebee4b5f04b4a378cd415764449e957', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.043, 'Rank IC': 0.034, 'Rank ICIR': 0.223}, 'data_train_vec': ['2021-05-28', '2025-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.223', 'weight': '0.081'}

	Recorder: 67e202f2bcd641a29e2f79fa3db3d5e1

		Model: {'id': '67e202f2bcd641a29e2f79fa3db3d5e1', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.03, 'Rank IC': 0.037, 'Rank ICIR': 0.205}, 'data_train_vec': ['2022-05-30', '2025-05-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.205', 'weight': '0.074'}

	Recorder: 5267d62c389c49388f6a94bd1940ac59

		Model: {'id': '5267d62c389c49388f6a94bd1940ac59', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.228, 'Rank IC': 0.039, 'Rank ICIR': 0.263}, 'data_train_vec': ['2023-05-28', '2025-08-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.263', 'weight': '0.095'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260530_14 168958368089420228 (Recorders: 4/5)

	Recorder: 439eca0070524e7cabe406a6ff30c6c1

		Model: {'id': '439eca0070524e7cabe406a6ff30c6c1', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.064, 'Rank IC': 0.035, 'Rank ICIR': 0.304}, 'data_train_vec': ['2021-05-28', '2025-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.304', 'weight': '0.110'}

	Recorder: 6a6eeb0287454f7984034abcf4705323

		Model: {'id': '6a6eeb0287454f7984034abcf4705323', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.097, 'Rank IC': 0.031, 'Rank ICIR': 0.281}, 'data_train_vec': ['2023-05-28', '2025-08-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.281', 'weight': '0.102'}

	Recorder: a639073928034434a3a3055de9bf04c5

		Model: {'id': 'a639073928034434a3a3055de9bf04c5', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.029, 'Rank IC': 0.011, 'Rank ICIR': 0.083}, 'data_train_vec': ['2024-05-30', '2025-11-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.083', 'weight': '0.030'}

	Recorder: 2700d6c16de5468da89e21dd6cd72ee7

		Model: {'id': '2700d6c16de5468da89e21dd6cd72ee7', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.051, 'ICIR': 0.242, 'Rank IC': 0.029, 'Rank ICIR': 0.124}, 'data_train_vec': ['2025-05-28', '2026-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.124', 'weight': '0.045'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260530_14 527691856114501227 (Recorders: 3/5)

	Recorder: c1f7982d162049329b6e9f5bd8c812f4

		Model: {'id': 'c1f7982d162049329b6e9f5bd8c812f4', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.025, 'Rank IC': 0.02, 'Rank ICIR': 0.122}, 'data_train_vec': ['2021-05-28', '2025-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.122', 'weight': '0.044'}

	Recorder: 5e195bf636c7498080bf93245cbd0086

		Model: {'id': '5e195bf636c7498080bf93245cbd0086', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.036, 'Rank IC': 0.026, 'Rank ICIR': 0.168}, 'data_train_vec': ['2023-05-28', '2025-08-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.168', 'weight': '0.061'}

	Recorder: 28ff2a219f194bb8a3259e7cc8246748

		Model: {'id': '28ff2a219f194bb8a3259e7cc8246748', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.086, 'Rank IC': 0.006, 'Rank ICIR': 0.037}, 'data_train_vec': ['2025-05-28', '2026-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.037', 'weight': '0.013'}
