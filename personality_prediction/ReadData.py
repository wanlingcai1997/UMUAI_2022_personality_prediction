import numpy as np
import pandas as pd
from Data import Data
import json
import copy
from sklearn.preprocessing import MultiLabelBinarizer
import sys 
sys.path.append("..") 
import load_data
import helper
class ReadData(object):

    @staticmethod
    def readData():
        if Data.file_ALL != None and Data.file_LIST != None and Data.file_LIST != None:
            #------------------------------------------------
            helper.print_current_time()
            print("Read Data")
            #------------------------------------------------

            # Store data into a DataFrame
            data_name_label_ALL,data_name_label_LIST, data_name_label_ORG, Data.data_user_feature_ALL, Data.data_user_feature_LIST, Data.data_user_feature_ORG = load_data.load_whole_data(
                Data.file_ALL, Data.file_LIST, Data.file_ORG)            
            if Data.interface == 'ALL':
                Data.data_user_label = data_name_label_ALL
            elif Data.interface == 'LIST':
                Data.data_user_label = data_name_label_LIST
            elif Data.interface == 'ORG':
                Data.data_user_label = data_name_label_ORG

            helper.print_current_time()
            print("Number of All Users : %d" % len(Data.data_user_label))
            #------------------------------------------------
        
