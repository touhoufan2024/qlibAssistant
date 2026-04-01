# params 
 {'predict_dates': [{'start': '2026-04-01', 'end': '2026-04-01'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260401_16 960941072682530443 (Recorders: 3/5)

	Recorder: 452a4b9a18d44d23818610fa101bf1e6

		Model: {'id': '452a4b9a18d44d23818610fa101bf1e6', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.208, 'Rank IC': 0.052, 'Rank ICIR': 0.304}, 'data_train_vec': ['2023-04-01', '2025-06-30'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.304', 'weight': '0.091'}

	Recorder: c50af00224944f518d45531ee5ece733

		Model: {'id': 'c50af00224944f518d45531ee5ece733', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.135, 'Rank IC': 0.05, 'Rank ICIR': 0.356}, 'data_train_vec': ['2024-04-01', '2025-09-30'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.356', 'weight': '0.107'}

	Recorder: 4de72d39aaea4cc1b5c5ea5063126171

		Model: {'id': '4de72d39aaea4cc1b5c5ea5063126171', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.14, 'Rank IC': 0.009, 'Rank ICIR': 0.069}, 'data_train_vec': ['2025-04-01', '2025-12-31'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.069', 'weight': '0.021'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260401_16 438498877204158437 (Recorders: 3/5)

	Recorder: 0a68ad62c0194ee18e01a23ad3806da7

		Model: {'id': '0a68ad62c0194ee18e01a23ad3806da7', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.039, 'Rank IC': 0.027, 'Rank ICIR': 0.158}, 'data_train_vec': ['2021-04-01', '2024-12-31'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.158', 'weight': '0.047'}

	Recorder: c0d475067ca54865ad67cf265391f555

		Model: {'id': 'c0d475067ca54865ad67cf265391f555', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.001, 'ICIR': 0.007, 'Rank IC': 0.044, 'Rank ICIR': 0.228}, 'data_train_vec': ['2023-04-01', '2025-06-30'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.228', 'weight': '0.068'}

	Recorder: d60b382008394e178f14eb69c3fb3579

		Model: {'id': 'd60b382008394e178f14eb69c3fb3579', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.142, 'Rank IC': 0.03, 'Rank ICIR': 0.256}, 'data_train_vec': ['2024-04-01', '2025-09-30'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.256', 'weight': '0.077'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260401_13 103890204974505992 (Recorders: 4/5)

	Recorder: c800268311014905afdfa070a5e94c8b

		Model: {'id': 'c800268311014905afdfa070a5e94c8b', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.117, 'Rank IC': 0.039, 'Rank ICIR': 0.214}, 'data_train_vec': ['2021-04-01', '2024-12-31'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.214', 'weight': '0.064'}

	Recorder: 2d7a8f3e56ba433397aee5c3a341908f

		Model: {'id': '2d7a8f3e56ba433397aee5c3a341908f', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.113, 'Rank IC': 0.055, 'Rank ICIR': 0.297}, 'data_train_vec': ['2023-04-01', '2025-06-30'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.297', 'weight': '0.089'}

	Recorder: 7ee77c6df978441882c563933f037f26

		Model: {'id': '7ee77c6df978441882c563933f037f26', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.241, 'Rank IC': 0.035, 'Rank ICIR': 0.335}, 'data_train_vec': ['2024-04-01', '2025-09-30'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.335', 'weight': '0.101'}

	Recorder: c061729ae6204855b0aeca82edbc0f90

		Model: {'id': 'c061729ae6204855b0aeca82edbc0f90', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.034, 'Rank IC': 0.008, 'Rank ICIR': 0.071}, 'data_train_vec': ['2025-04-01', '2025-12-31'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.071', 'weight': '0.021'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260401_13 669135515868926254 (Recorders: 4/5)

	Recorder: a8d3af2fa83849ae998660ef4debb931

		Model: {'id': 'a8d3af2fa83849ae998660ef4debb931', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.101, 'Rank IC': 0.023, 'Rank ICIR': 0.185}, 'data_train_vec': ['2021-04-01', '2024-12-31'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.185', 'weight': '0.056'}

	Recorder: 97d052133ecf4c59975705e162ecab1f

		Model: {'id': '97d052133ecf4c59975705e162ecab1f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.024, 'Rank IC': 0.02, 'Rank ICIR': 0.172}, 'data_train_vec': ['2022-04-01', '2025-03-31'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.172', 'weight': '0.052'}

	Recorder: 547e76598646433a8b58b66f4d550f8a

		Model: {'id': '547e76598646433a8b58b66f4d550f8a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.116, 'Rank IC': 0.039, 'Rank ICIR': 0.325}, 'data_train_vec': ['2023-04-01', '2025-06-30'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.325', 'weight': '0.098'}

	Recorder: d05c49b92a4a49bcac7f129797cb50e9

		Model: {'id': 'd05c49b92a4a49bcac7f129797cb50e9', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.054, 'Rank IC': 0.003, 'Rank ICIR': 0.025}, 'data_train_vec': ['2025-04-01', '2025-12-31'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.025', 'weight': '0.008'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260401_13 456338133106256009 (Recorders: 2/5)

	Recorder: 9a8603b781364cfe9c5b3629dc651099

		Model: {'id': '9a8603b781364cfe9c5b3629dc651099', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.118, 'Rank IC': 0.034, 'Rank ICIR': 0.181}, 'data_train_vec': ['2021-04-01', '2024-12-31'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.181', 'weight': '0.054'}

	Recorder: 5f795ad180004268aa71e63a097085d1

		Model: {'id': '5f795ad180004268aa71e63a097085d1', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.12, 'Rank IC': 0.014, 'Rank ICIR': 0.155}, 'data_train_vec': ['2025-04-01', '2025-12-31'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.155', 'weight': '0.047'}
