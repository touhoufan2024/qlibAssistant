# params 
 {'predict_dates': [{'start': '2026-04-14', 'end': '2026-04-14'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260415_16 560430297798786732 (Recorders: 2/5)

	Recorder: d9ba13a8fe204b438f120157a6772bde

		Model: {'id': 'd9ba13a8fe204b438f120157a6772bde', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.044, 'Rank IC': 0.035, 'Rank ICIR': 0.214}, 'data_train_vec': ['2023-04-15', '2025-07-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.214', 'weight': '0.057'}

	Recorder: 3a896eb0e85f49e3b6eb96017b82f851

		Model: {'id': '3a896eb0e85f49e3b6eb96017b82f851', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.056, 'ICIR': 0.403, 'Rank IC': 0.052, 'Rank ICIR': 0.373}, 'data_train_vec': ['2025-04-15', '2026-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.373', 'weight': '0.100'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260415_16 725184221710853490 (Recorders: 2/5)

	Recorder: 91731feee1e0490aab4515dbfba6a923

		Model: {'id': '91731feee1e0490aab4515dbfba6a923', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.251, 'Rank IC': 0.035, 'Rank ICIR': 0.337}, 'data_train_vec': ['2024-04-15', '2025-10-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.337', 'weight': '0.090'}

	Recorder: 2df02a38ddad41f5ad984b0d4e04f89c

		Model: {'id': '2df02a38ddad41f5ad984b0d4e04f89c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.28, 'Rank IC': 0.035, 'Rank ICIR': 0.219}, 'data_train_vec': ['2025-04-15', '2026-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.219', 'weight': '0.059'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260415_14 909960342661476752 (Recorders: 4/5)

	Recorder: 8f2d75d7bee14cdcb214ef043b5017df

		Model: {'id': '8f2d75d7bee14cdcb214ef043b5017df', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.034, 'Rank IC': 0.025, 'Rank ICIR': 0.148}, 'data_train_vec': ['2021-04-15', '2025-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.148', 'weight': '0.040'}

	Recorder: cadb812ca1004cb1aecf71d48c10b59e

		Model: {'id': 'cadb812ca1004cb1aecf71d48c10b59e', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.084, 'Rank IC': 0.049, 'Rank ICIR': 0.293}, 'data_train_vec': ['2023-04-15', '2025-07-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.293', 'weight': '0.079'}

	Recorder: 256fe7f6405a4c479163a4e02c0ef458

		Model: {'id': '256fe7f6405a4c479163a4e02c0ef458', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.149, 'Rank IC': 0.026, 'Rank ICIR': 0.207}, 'data_train_vec': ['2024-04-15', '2025-10-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.207', 'weight': '0.056'}

	Recorder: fc10e23787b14bd19bd135fe68c295f7

		Model: {'id': 'fc10e23787b14bd19bd135fe68c295f7', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.245, 'Rank IC': 0.032, 'Rank ICIR': 0.173}, 'data_train_vec': ['2025-04-15', '2026-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.173', 'weight': '0.046'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260415_14 186362564323872367 (Recorders: 4/5)

	Recorder: f81be58450354af18e972d5eb8348152

		Model: {'id': 'f81be58450354af18e972d5eb8348152', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.052, 'Rank IC': 0.018, 'Rank ICIR': 0.164}, 'data_train_vec': ['2021-04-15', '2025-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.164', 'weight': '0.044'}

	Recorder: 5516282435884f0084794f91c6e06ef0

		Model: {'id': '5516282435884f0084794f91c6e06ef0', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.061, 'Rank IC': 0.036, 'Rank ICIR': 0.307}, 'data_train_vec': ['2023-04-15', '2025-07-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.307', 'weight': '0.082'}

	Recorder: ca5bc1afdaca40a1bc1e96c1a5947094

		Model: {'id': 'ca5bc1afdaca40a1bc1e96c1a5947094', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.075, 'Rank IC': 0.015, 'Rank ICIR': 0.128}, 'data_train_vec': ['2024-04-15', '2025-10-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.128', 'weight': '0.034'}

	Recorder: 9564009ef4ac4785b9afd79e0c9b8b34

		Model: {'id': '9564009ef4ac4785b9afd79e0c9b8b34', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.075, 'ICIR': 0.479, 'Rank IC': 0.059, 'Rank ICIR': 0.362}, 'data_train_vec': ['2025-04-15', '2026-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.362', 'weight': '0.097'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260415_14 679275826995309284 (Recorders: 3/5)

	Recorder: 70e58335b20b4407bc0474ff6f97813e

		Model: {'id': '70e58335b20b4407bc0474ff6f97813e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.096, 'Rank IC': 0.044, 'Rank ICIR': 0.272}, 'data_train_vec': ['2023-04-15', '2025-07-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.272', 'weight': '0.073'}

	Recorder: a5a8fef86fb7451db6c62993ac27dc21

		Model: {'id': 'a5a8fef86fb7451db6c62993ac27dc21', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.045, 'Rank IC': 0.038, 'Rank ICIR': 0.338}, 'data_train_vec': ['2024-04-15', '2025-10-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.338', 'weight': '0.091'}

	Recorder: de7ff93cb542484590e69b98f3c58f50

		Model: {'id': 'de7ff93cb542484590e69b98f3c58f50', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.297, 'Rank IC': 0.028, 'Rank ICIR': 0.19}, 'data_train_vec': ['2025-04-15', '2026-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.190', 'weight': '0.051'}
