# script.py

# Step1: preprocess_data.py



import os



def execute_script (script,  fs_param_script, model_script,  personality_trait_script, interface_script, product_script,result_script):

    s = script + fs_param_script+ model_script + personality_trait_script + interface_script + product_script + result_script
    print(s)
    # input()
    os.system(s)

    return s

file_ALL = '../Data/WholeData.xlsx'
file_LIST = '../Data/data_LIST.xlsx' 
file_ORG = '../Data/data_ORG.xlsx' 

# personality_trait_opt = ['C']
# interface_opt = ['ORG']
# product_opt = ['hotel']


personality_trait_opt = ['A']
interface_opt = ['ALL']
# interface_opt = ['ALL']
product_opt = ['ALL']
product_selection_feature = 'with'
# product_selection_feature = 'without'




feature_selection = 'gini_index'  # 'gini_index', 'fisher_score', 'f_score', 't_score'
# feature_selection_param = [5, 10, 15, 20]
feature_selection_param = [6]# list(range(1,40, 2))

# feature normalization
feature_normalization = 0

model_name = ['AdaBoost' ] # 'SVM', 'NB_M'
# model_name = ['LR']

cross_validation = 10

result_folder = ''
if product_selection_feature == 'with':
    result_folder = ''
if product_selection_feature == 'without':
    result_folder = 'result_w_o_psf'


script_list = []

script = 'python Main.py '
script += '--file_ALL %s ' % file_ALL
script += '--file_LIST %s ' % file_LIST
script += '--file_ORG %s ' % file_ORG

script += '--cross_validation %s ' % cross_validation
script += '--fs_product_selection_feature %s ' % product_selection_feature

script += '--feature_selection %s ' % feature_selection
script += '--feature_normalization %s ' % feature_normalization

for fs_param in feature_selection_param:
    fs_param_script = '--feature_selection_param %s ' % str(fs_param)
    for model in model_name:
        model_script = '--model_name %s ' % model
        for personality_trait in personality_trait_opt:
            personality_trait_script = '--personality_trait %s ' % personality_trait
            for interface in interface_opt:
                interface_script = '--interface %s ' % interface

                for product in product_opt:
                    product_script = '--product %s ' % product
                    result_script = ''
                    # result_script = '> %smodel_%s_trait_%s_interface_%s_product_%s_fs_%s_para_%s_norm_%d_cv_%d.txt' % (result_folder, model, personality_trait, interface, product, feature_selection, str(fs_param),feature_normalization, cross_validation)
                    script_list.append(execute_script(script,  fs_param_script, model_script, personality_trait_script, interface_script, product_script,result_script))
        			

print("Total script: %d pieces." % len(script_list))