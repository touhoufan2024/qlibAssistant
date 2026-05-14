# params 
 {'predict_dates': [{'start': '2026-05-14', 'end': '2026-05-14'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260514_17 269833250314843718 (Recorders: 3/5)

	Recorder: 9eea1bd451a041c79ed860376dd66124

		Model: {'id': '9eea1bd451a041c79ed860376dd66124', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.053, 'Rank IC': 0.021, 'Rank ICIR': 0.138}, 'data_train_vec': ['2022-05-14', '2025-05-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.138', 'weight': '0.056'}

	Recorder: 8c0c6502a4d442f597983da2a300b124

		Model: {'id': '8c0c6502a4d442f597983da2a300b124', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.138, 'Rank IC': 0.011, 'Rank ICIR': 0.075}, 'data_train_vec': ['2024-05-14', '2025-11-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.075', 'weight': '0.030'}

	Recorder: b34b615872844478802306f5d18d2027

		Model: {'id': 'b34b615872844478802306f5d18d2027', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.073, 'ICIR': 0.473, 'Rank IC': 0.037, 'Rank ICIR': 0.229}, 'data_train_vec': ['2025-05-14', '2026-02-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.229', 'weight': '0.092'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260514_17 306995201633198230 (Recorders: 3/5)

	Recorder: e666ec6968fd4f2a8e9e3510d0915d81

		Model: {'id': 'e666ec6968fd4f2a8e9e3510d0915d81', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.19, 'Rank IC': 0.027, 'Rank ICIR': 0.225}, 'data_train_vec': ['2023-05-14', '2025-08-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.225', 'weight': '0.091'}

	Recorder: 5dcf0ad0840b4c5c8c1d07fed2c6abf6

		Model: {'id': '5dcf0ad0840b4c5c8c1d07fed2c6abf6', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.127, 'Rank IC': 0.006, 'Rank ICIR': 0.057}, 'data_train_vec': ['2024-05-14', '2025-11-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.057', 'weight': '0.023'}

	Recorder: 8a25e9e7833a40fb9b03fa546e8d8a73

		Model: {'id': '8a25e9e7833a40fb9b03fa546e8d8a73', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.095, 'ICIR': 0.639, 'Rank IC': 0.046, 'Rank ICIR': 0.304}, 'data_train_vec': ['2025-05-14', '2026-02-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.304', 'weight': '0.122'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260514_14 533895014871767468 (Recorders: 3/5)

	Recorder: 2ce6540a795f4b448a9866addb9643f4

		Model: {'id': '2ce6540a795f4b448a9866addb9643f4', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.034, 'Rank IC': 0.031, 'Rank ICIR': 0.171}, 'data_train_vec': ['2022-05-14', '2025-05-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.171', 'weight': '0.069'}

	Recorder: 44193343318948018d5d3320c999d067

		Model: {'id': '44193343318948018d5d3320c999d067', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.112, 'Rank IC': 0.033, 'Rank ICIR': 0.213}, 'data_train_vec': ['2023-05-14', '2025-08-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.213', 'weight': '0.086'}

	Recorder: 06c78b4db31446749b812b09cf11fe4f

		Model: {'id': '06c78b4db31446749b812b09cf11fe4f', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.08, 'ICIR': 0.484, 'Rank IC': 0.033, 'Rank ICIR': 0.194}, 'data_train_vec': ['2025-05-14', '2026-02-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.194', 'weight': '0.078'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260514_14 389996492255507043 (Recorders: 3/5)

	Recorder: 41d79becf116476bbf7f3770a4697a9c

		Model: {'id': '41d79becf116476bbf7f3770a4697a9c', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.021, 'Rank IC': 0.027, 'Rank ICIR': 0.246}, 'data_train_vec': ['2023-05-14', '2025-08-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.246', 'weight': '0.099'}

	Recorder: a664a35cedea43459c81c8c1072b4f7b

		Model: {'id': 'a664a35cedea43459c81c8c1072b4f7b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.076, 'Rank IC': 0.019, 'Rank ICIR': 0.166}, 'data_train_vec': ['2024-05-14', '2025-11-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.166', 'weight': '0.067'}

	Recorder: ade588b186e74189888ad2172199e8da

		Model: {'id': 'ade588b186e74189888ad2172199e8da', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.073, 'ICIR': 0.528, 'Rank IC': 0.044, 'Rank ICIR': 0.277}, 'data_train_vec': ['2025-05-14', '2026-02-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.277', 'weight': '0.112'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260514_14 401852665551812653 (Recorders: 2/5)

	Recorder: 21dc5c7ce9334b5088cc19639311a7d4

		Model: {'id': '21dc5c7ce9334b5088cc19639311a7d4', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.121, 'Rank IC': 0.002, 'Rank ICIR': 0.018}, 'data_train_vec': ['2024-05-14', '2025-11-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.018', 'weight': '0.007'}

	Recorder: 801766faaf2f441b9ff30819607ca686

		Model: {'id': '801766faaf2f441b9ff30819607ca686', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.064, 'ICIR': 0.489, 'Rank IC': 0.025, 'Rank ICIR': 0.171}, 'data_train_vec': ['2025-05-14', '2026-02-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.171', 'weight': '0.069'}
