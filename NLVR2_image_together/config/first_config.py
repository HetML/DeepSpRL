'''
Institution: Tulane University
Name: Chen Zheng
Date: 10/23/2018
Purpose: It is the global config file.
'''

CONFIG = {
    'hidden_size': 128,
    'embed_size': 64,
    'batch_size': 64,
    'lstm_num_layer': 1,

    'feature_length': 10,
    'MAX_LENGTH': 20,
    'SOS_token': 0,
    'EOS_token': 1,
    'n_iters': 100,
    'print_every': 10,
    'plot_every': 100,
    'learning_rate': 0.001,
    'TRAIN_DIR': '../data/train.json',
    'TEST_DIR': '../data/test.json',
    'save_checkpoint_dir': '../check_point/match_2.pt',
    'save_train_result_dir': '../result/train/bi_match_result_1.txt',
    'save_test_result_dir': '../result/test/bi_match_result_1.txt',
    # 'save_train_result_dir': '../result/train/transform_result_1.txt',
    # 'save_test_result_dir': '../result/test/transform_result_1.txt',
    'TENSORBOARD_DIR': '../tensorboard/1.json',

    # 'MODEL': 'NLVR',
    # 'MODEL': 'MATCHING',
    # 'MODEL': 'BI-MATCHING',
    # 'MODEL': 'TRANSFORMER',
    # 'MODEL': 'TRANSFORMER-TRANSFORMER-MATCHING',
    'MODEL': 'TRANSFORMER-TRANSFORMER-MATCHING-CNN',
    # 'MODEL': 'TRANSFORMER3',
    'TOPK': 20,
}
