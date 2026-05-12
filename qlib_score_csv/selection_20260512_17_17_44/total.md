# params 
 {'predict_dates': [{'start': '2026-05-12', 'end': '2026-05-12'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260512_16 562569983769221299 (Recorders: 4/5)

	Recorder: 20a22ed8deb54235b3f72f983f1678fb

		Model: {'id': '20a22ed8deb54235b3f72f983f1678fb', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.094, 'Rank IC': 0.013, 'Rank ICIR': 0.081}, 'data_train_vec': ['2022-05-12', '2025-05-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.081', 'weight': '0.027'}

	Recorder: 5e56641d312240f1a435f38531cbde61

		Model: {'id': '5e56641d312240f1a435f38531cbde61', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.107, 'Rank IC': 0.02, 'Rank ICIR': 0.136}, 'data_train_vec': ['2023-05-12', '2025-08-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.136', 'weight': '0.046'}

	Recorder: 387a46f3337142fc982cd14ce5798427

		Model: {'id': '387a46f3337142fc982cd14ce5798427', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.087, 'Rank IC': 0.016, 'Rank ICIR': 0.135}, 'data_train_vec': ['2024-05-12', '2025-11-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.135', 'weight': '0.045'}

	Recorder: 68baaec5fa5f47038b9ccd1bd818837e

		Model: {'id': '68baaec5fa5f47038b9ccd1bd818837e', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.056, 'ICIR': 0.42, 'Rank IC': 0.018, 'Rank ICIR': 0.145}, 'data_train_vec': ['2025-05-12', '2026-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.145', 'weight': '0.049'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260512_16 900805913649239371 (Recorders: 3/5)

	Recorder: 1552313493634ceea410696dd53bedd7

		Model: {'id': '1552313493634ceea410696dd53bedd7', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.079, 'Rank IC': 0.018, 'Rank ICIR': 0.159}, 'data_train_vec': ['2023-05-12', '2025-08-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.159', 'weight': '0.053'}

	Recorder: efc12c78f08b41b08b5c9847bde61223

		Model: {'id': 'efc12c78f08b41b08b5c9847bde61223', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.146, 'Rank IC': 0.013, 'Rank ICIR': 0.108}, 'data_train_vec': ['2024-05-12', '2025-11-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.108', 'weight': '0.036'}

	Recorder: 91e97452f7e943e0b49cd897136345c2

		Model: {'id': '91e97452f7e943e0b49cd897136345c2', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.075, 'ICIR': 0.586, 'Rank IC': 0.024, 'Rank ICIR': 0.217}, 'data_train_vec': ['2025-05-12', '2026-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.217', 'weight': '0.073'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260512_14 725607497370680570 (Recorders: 4/5)

	Recorder: d3d4910e54b346cd9a685ccf819cbce8

		Model: {'id': 'd3d4910e54b346cd9a685ccf819cbce8', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.015, 'Rank IC': 0.026, 'Rank ICIR': 0.148}, 'data_train_vec': ['2022-05-12', '2025-05-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.148', 'weight': '0.050'}

	Recorder: ece0d9cf1f394b16944d9df3a3b7d213

		Model: {'id': 'ece0d9cf1f394b16944d9df3a3b7d213', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.042, 'Rank IC': 0.027, 'Rank ICIR': 0.173}, 'data_train_vec': ['2023-05-12', '2025-08-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.173', 'weight': '0.058'}

	Recorder: 0d951f57e0d54b299c0da9a928032029

		Model: {'id': '0d951f57e0d54b299c0da9a928032029', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.114, 'Rank IC': 0.009, 'Rank ICIR': 0.074}, 'data_train_vec': ['2024-05-12', '2025-11-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.074', 'weight': '0.025'}

	Recorder: 8508974b8c64437f972d20160981fe4e

		Model: {'id': '8508974b8c64437f972d20160981fe4e', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.062, 'ICIR': 0.522, 'Rank IC': 0.023, 'Rank ICIR': 0.212}, 'data_train_vec': ['2025-05-12', '2026-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.212', 'weight': '0.071'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260512_14 239708773071956579 (Recorders: 4/5)

	Recorder: 55d97ef8659c491cb12803f63fef60ca

		Model: {'id': '55d97ef8659c491cb12803f63fef60ca', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.014, 'Rank IC': 0.02, 'Rank ICIR': 0.188}, 'data_train_vec': ['2021-05-12', '2025-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.188', 'weight': '0.063'}

	Recorder: 3000f4376d7b4f0f9a0ed916891b6487

		Model: {'id': '3000f4376d7b4f0f9a0ed916891b6487', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.017, 'Rank IC': 0.026, 'Rank ICIR': 0.225}, 'data_train_vec': ['2023-05-12', '2025-08-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.225', 'weight': '0.075'}

	Recorder: 2df79324257d490588c300bdfe30b273

		Model: {'id': '2df79324257d490588c300bdfe30b273', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.08, 'Rank IC': 0.019, 'Rank ICIR': 0.164}, 'data_train_vec': ['2024-05-12', '2025-11-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.164', 'weight': '0.055'}

	Recorder: adc818ab736e4c3db47a87871d39a839

		Model: {'id': 'adc818ab736e4c3db47a87871d39a839', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.658, 'Rank IC': 0.024, 'Rank ICIR': 0.293}, 'data_train_vec': ['2025-05-12', '2026-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.293', 'weight': '0.098'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260512_14 140987959291392384 (Recorders: 4/5)

	Recorder: 4d1f3ae23a044759afba3872af4036c3

		Model: {'id': '4d1f3ae23a044759afba3872af4036c3', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.029, 'Rank IC': 0.011, 'Rank ICIR': 0.063}, 'data_train_vec': ['2022-05-12', '2025-05-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.063', 'weight': '0.021'}

	Recorder: 60a6c74407a74376807379cafb3e5411

		Model: {'id': '60a6c74407a74376807379cafb3e5411', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.086, 'Rank IC': 0.024, 'Rank ICIR': 0.14}, 'data_train_vec': ['2023-05-12', '2025-08-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.140', 'weight': '0.047'}

	Recorder: 6340babc5ebe4b828965caaa2462ac80

		Model: {'id': '6340babc5ebe4b828965caaa2462ac80', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.071, 'Rank IC': 0.008, 'Rank ICIR': 0.061}, 'data_train_vec': ['2024-05-12', '2025-11-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.061', 'weight': '0.020'}

	Recorder: ca80646ef36147a6a45428809a5c9871

		Model: {'id': 'ca80646ef36147a6a45428809a5c9871', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.422, 'Rank IC': 0.019, 'Rank ICIR': 0.259}, 'data_train_vec': ['2025-05-12', '2026-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.259', 'weight': '0.087'}
