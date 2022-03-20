import numpy as np
import pandas as pd
import json
import helper
import copy

def load_whole_data(file_ALL, file_LIST, file_ORG):  
    data_ALL = pd.read_excel(file_ALL)
    data_ORG = pd.read_excel(file_ORG)
    data_LIST = pd.read_excel(file_LIST)

    data_ALL = data_ALL.fillna(data_ALL.mean())
    data_ORG = data_ORG.fillna(data_ORG.mean())
    data_LIST = data_LIST.fillna(data_LIST.mean())

    # print(data_ORG.describe())
    data_name_label_ALL = data_ALL[['name', 'O', 'C', 'E', 'A', 'N']]
    data_name_label_LIST = data_LIST[['name', 'O', 'C', 'E', 'A', 'N']]
    data_name_label_ORG = data_ORG[['name', 'O', 'C', 'E', 'A', 'N']]

    data_user_feature_ALL = pd.concat([data_ALL[['name']], data_ALL[['Product']],data_ALL.loc[:,  'F_start':'F_end']],axis=1)
    data_user_feature_LIST = pd.concat([data_LIST[['name']],  data_LIST[['Product']],  data_LIST.loc[:,  'F_start':'F_end']],axis=1)
    data_user_feature_ORG = pd.concat([data_ORG[['name']], data_ORG[['Product']],data_ORG.loc[:, 'F_start':'F_end']],axis=1)

    helper.print_current_time()
    print('The shape of data label: ' + str(data_name_label_ALL.shape))
    print('The shape of data - name + feature (ALL): ' + str(data_user_feature_ALL.shape))
    print('The shape of data - name + feature (LIST): ' + str(data_user_feature_LIST.shape))
    print('The shape of data - name + feature (ORG): ' + str(data_user_feature_ORG.shape))
    
    return data_name_label_ALL,data_name_label_LIST, data_name_label_ORG , data_user_feature_ALL, data_user_feature_LIST, data_user_feature_ORG


def construct_label_index_dict (labels):
    label_indext_dict = {}
    indext_label_dict = {}
    index = 0
    for label in labels:
        label_indext_dict[label] = index
        indext_label_dict[index] = label
        index += 1
        
    return label_indext_dict, indext_label_dict