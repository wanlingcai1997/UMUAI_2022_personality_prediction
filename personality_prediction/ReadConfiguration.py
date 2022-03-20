# ReadConfiguration.py
from Data import Data
import argparse

class ReadConfiguration(object):
    
    @staticmethod
    def readConfiguration():
        parser = argparse.ArgumentParser(description='Read some configuration.....')
        # -----------------------------------------------------------------------------------------------
        # ------                                   Data                                            ------
        # -----------------------------------------------------------------------------------------------
        parser.add_argument('--file_ALL', nargs='?', help='input ALL data')
        parser.add_argument('--file_LIST', nargs='?', help='input LIST data')
        parser.add_argument('--file_ORG', nargs='?', help='input ORG data')

        

        # -----------------------------------------------------------------------------------------------
        # ------                       Feature Related Configuration                               ------                                 
        # -----------------------------------------------------------------------------------------------

        parser.add_argument('--personality_trait', nargs='?', help='experimental configuration about personalit_trait')

        # feature construction
        parser.add_argument('--interface', nargs='?', help='experimental configuration about interface')
        parser.add_argument('--product', nargs='?', help='experimental configuration about product')
    


        # feature selection
        parser.add_argument('--feature_selection', nargs='?', help='whether or not to operate feature selection')
        parser.add_argument('--feature_selection_param', nargs='?', default=0, help='whether or not to operate feature selection')
        
   
        # -----------------------------------------------------------------------------------------------
        # ------                         Model Related Configuration                               ------                                 
        # -----------------------------------------------------------------------------------------------

        parser.add_argument('--model_name', nargs='?', help='input model name')

        #  --------------------------------- Model Parameters -------------------------------------------

        # -----------------------------------------------------------------------------------------------

        # -----------------------------------------------------------------------------------------------
        # ------                                    Evaluation                                     ------                                 
        # -----------------------------------------------------------------------------------------------

        # cross-validation
        parser.add_argument('--cross_validation', type=int, default=3, help='k-fold cross_validation')



      
        # ===============================================================================================
        # ====================          Store Configurations    =========================================                          
        # ===============================================================================================                          


        args = parser.parse_args()

        # -----------------------------------------------------------------------------------------------
        # ------                                   Data                                            ------
        # -----------------------------------------------------------------------------------------------
        Data.file_ALL = args.file_ALL
        Data.file_LIST = args.file_LIST
        Data.file_ORG = args.file_ORG




        # -----------------------------------------------------------------------------------------------
        # ------                       Feature Related Configuration                               ------                                 
        # -----------------------------------------------------------------------------------------------




        Data.personality_trait = args.personality_trait
        Data.interface = args.interface
        Data.product = args.product


        Data.feature_selection = args.feature_selection
        Data.feature_selection_param = args.feature_selection_param


        # -----------------------------------------------------------------------------------------------
        # ------                         Model Related Configuration                               ------                                 
        # -----------------------------------------------------------------------------------------------
        
        Data.model_name = args.model_name

        #  --------------------------------- Model Parameters -------------------------------------------

        # -----------------------------------------------------------------------------------------------

        # -----------------------------------------------------------------------------------------------
        # ------                                    Evaluation                                     ------                                 
        # -----------------------------------------------------------------------------------------------


        Data.cross_validation = args.cross_validation


        
        # ===============================================================================================
        # ====================          Print Configurations    =========================================                          
        # ===============================================================================================

      
        
        
        print ('-------------------------------------------')
        print ('------------ Configurations ---------------')
        print ('-------------------------------------------')
        print ('file_ALL: %s' % Data.file_ALL)
        print ('file_LIST: %s' % Data.file_LIST)
        print ('file_ORG: %s' % Data.file_ORG)
		
        

        print ('personality_trait: %s' % Data.personality_trait)
        print ('interface: %s' % Data.interface)
        print ('product: %s' % Data.product)

        print ('feature_selection: %s' % Data.feature_selection)
        print ('feature_selection_param: %s' % Data.feature_selection_param)
        
        print ('model_name: %s' % Data.model_name)



        print ('cross_validation: %d' % Data.cross_validation)
