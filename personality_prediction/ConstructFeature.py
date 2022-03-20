import numpy as np
import pandas as pd
from Data import Data
import copy
import time
import sys 
sys.path.append("..") 
import helper


class ConstructFeature(object):

    @staticmethod
    def constructFeature():

        list_start_feat_name = 'F_start'
        list_end_feat_name = 'F_end'        
        org_start_feat_name = 'F_start'
        org_end_feat_name = 'F_end'
        
        if Data.interface == 'ALL':
            if Data.product == 'ALL':
                Data.feature_vector = Data.data_user_feature_ALL.loc[:,list_start_feat_name:list_end_feat_name]
                Data.labels = Data.data_user_label[[Data.personality_trait]]
            else:
                match_name_list = Data.data_user_feature_ALL[Data.data_user_feature_ALL['Product'] == Data.product]['name'].tolist()
                Data.feature_vector = Data.data_user_feature_ALL[Data.data_user_feature_ALL['name'].isin(match_name_list)].loc[:,list_start_feat_name:list_end_feat_name]
                Data.labels = Data.data_user_label[Data.data_user_label['name'].isin(match_name_list)][[Data.personality_trait]]
        else: 
            if Data.product == 'ALL':
                if Data.interface == 'LIST':
                    Data.feature_vector = Data.data_user_feature_LIST.loc[:,list_start_feat_name:list_end_feat_name]

                if Data.interface == 'ORG':
                    Data.feature_vector = Data.data_user_feature_ORG.loc[:,org_start_feat_name:org_end_feat_name]  

                Data.labels = Data.data_user_label[[Data.personality_trait]]

            
            else:
                if Data.interface == 'LIST':
                    match_name_list = Data.data_user_feature_LIST[Data.data_user_feature_LIST['Product'] == Data.product]['name'].tolist()
                    Data.feature_vector = Data.data_user_feature_LIST[Data.data_user_feature_LIST['name'].isin(match_name_list)].loc[:,list_start_feat_name:list_end_feat_name]
                    Data.labels = Data.data_user_label[Data.data_user_label['name'].isin(match_name_list)][[Data.personality_trait]]
                if Data.interface == 'ORG': 
                    match_name_list= Data.data_user_feature_ORG[Data.data_user_feature_ORG['Product'] == Data.product]['name'].tolist()
                    Data.feature_vector = Data.data_user_feature_ORG[Data.data_user_feature_ORG['name'].isin(match_name_list)].loc[:,org_start_feat_name:org_end_feat_name]
                    Data.labels = Data.data_user_label[Data.data_user_label['name'].isin(match_name_list)][[Data.personality_trait]]

        


        #------------------------------------------------            
        helper.print_current_time()
        print("Features For Chosen User [ %d users with the size of features vector (%d) !" % (Data.feature_vector.shape[0],Data.feature_vector.shape[1]) )
        helper.print_current_time()
        print("Labels For Chosen User [ %d users with the size of labels (%d) !" % (Data.labels.shape[0],Data.labels.shape[1]) )


        #------------------------------------------------            
        
       
        

         