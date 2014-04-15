from jobman import DD, flatten

model_config = DD({
        # One hidden layer Autoencoder
        'AE' : DD({
        
            'mlp' : DD({
                    'rand_seed'             : ((123, 1000000), int)
                    }), # end mlp
            
            'log' : DD({
                    'experiment_id'         : 'AE15_Scale',
                    'description'           : 'This_autoencoder_has_Scale_preprocessing_with_Sigmoid_internal_units',
                    'save_outputs'          : True,
                    'save_hyperparams'      : True,
                    'save_model'            : True,
                    'send_to_database'      : 'Database_Name.db'
                    }), # end log
            
            'learning_rule' : DD({
                    'max_col_norm'          : ((1, 10), int),
                    'learning_rate'         : ((0.001, 0.1), float),
                    'momentum'              : ((0.001, 0.1), float),
                    'momentum_type'         : 'normal',
                    'weight_decay'          : 0,
                    'cost'                  : 'entropy',
                    'stopping_criteria'     : DD({
                                                'max_epoch'         : 100,
                                                'epoch_look_back'   : 10,
                                                'cost'              : 'entropy',
                                                'percent_decrease'  : 0.001
                                                }) # end stopping_criteria
                    }), # end learning_rule
                    
            #===========================[ Dataset ]===========================#            
#             'dataset' : DD({
#                     'type'                  : 'Mnist',
#                     'train_valid_test_ratio': [8, 1, 1],
#                     'preprocessor'          : 'Scale',
# #                     'preprocessor'          : 'Standardize',
#                     'batch_size'            : 100,
#                     'num_batches'           : None,
#                     'iter_class'            : 'SequentialSubsetIterator',
#                     'rng'                   : None
#                     }), # end dataset
                        
            'dataset' : DD({
                    'type'                  : 'P276',
                    'feature_size'          : 2049,
                    'train_valid_test_ratio': [8, 1, 1],
                    'preprocessor'          : 'Scale',
#                     'preprocessor'          : 'GCN',
#                     'preprocessor'          : 'Standardize',
                    'batch_size'            : ((32, 200), int),
                    'num_batches'           : None,
                    'iter_class'            : 'SequentialSubsetIterator',
                    'rng'                   : None
                    }), # end dataset
                    
            #============================[ Layers ]===========================#               
            'hidden_layer' : DD({
                    'name'                  : 'hidden_layer',
                    'type'                  : 'Sigmoid',
                    'dim'                   : 500,
                    'dropout_below'         : None
                    }), # end hidden_layer
            
            'output_layer' : DD({
                    'name'                  : 'output_layer',
                    'type'                  : 'Sigmoid',
#                      dim not needed as output dim = input dim
#                     'dim'                   : None,
                    'dropout_below'         : None
                    }) # end output_layer
            }) # end autoencoder
    }) # end model_config
    