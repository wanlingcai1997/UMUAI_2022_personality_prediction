import re
from datetime import datetime
import operator
import json
import numpy as np



def construct_feature_name_dict (feature_name_dict, feature_type, number_cur_features, current_features_name_list):
    start_feature_index = len(feature_name_dict)
    assert (number_cur_features == len(current_features_name_list))
    for i in range(number_cur_features):
        feature_index = start_feature_index + i
        feature_name = feature_type + "(" + str(current_features_name_list[i]) +")"
        feature_name_dict[feature_index]  = feature_name
    return feature_name_dict

def get_sorted_dict(dict):
    sorted_dict = {}
    tuple_list = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
    for t in tuple_list:
        sorted_dict[t[0]] = t[1]
    return sorted_dict

def store_result_json_file(file_name,data):
    path = 'result_analysis/'+file_name
    with open(path, 'w') as newfile:
        json.dump(data, newfile, indent=4, cls=NpEncoder)
    return 

def print_current_time():
    now = datetime.now()
    print("[Timestamp:", now, ']', end = '')




