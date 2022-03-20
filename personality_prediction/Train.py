# Train.py
import numpy as np
import pandas as pandas
import json
from Data import Data
import sklearn_model
from sklearn.feature_selection import GenericUnivariateSelect
from sklearn.preprocessing import MinMaxScaler
from sklearn.multiclass import OneVsRestClassifier
from skfeature.function.statistical_based import CFS, f_score, t_score
from skfeature.function.similarity_based import fisher_score
from skfeature.function.statistical_based import gini_index

import sys
sys.path.append("..") 
import helper
# from CFSmethod import CFS

class Train():
    
	@staticmethod
	def train():
		
		X = Data.feature_vector.to_numpy()
		Y = Data.labels.to_numpy().ravel()

		num_fea = int(Data.feature_selection_param)
		if Data.feature_selection == 'none':
			print(X.shape)

		elif Data.feature_selection == 'gini_index':
			# obtain the score of each feature on the training set	
			score = gini_index.gini_index(X,Y)
			# rank features in descending order according to score
			idx = gini_index.feature_ranking(score)

			print(idx.shape)
			print(idx)
			# obtain the dataset on the selected features
			X = X[:, idx[0:num_fea]]
			print(X.shape)

		elif Data.feature_selection == 'CFS':
			idx = CFS.cfs(X,Y)
			print("number of CFS selected features: %d" % len(idx))
			print(idx.shape)
			print(idx)
			
			# obtain the dataset on the selected features
			X = X[:, idx]
			print(X.shape)
			
		elif Data.feature_selection == 'fisher_score':
			# obtain the score of each feature on the training set
			score = fisher_score.fisher_score(X, Y)
			# rank features in descending order according to score
			idx = fisher_score.feature_ranking(score)
			print(idx.shape)
			print(idx)
			# obtain the dataset on the selected features
			X = X[:, idx[0:num_fea]]
			print(X.shape)



		elif Data.feature_selection == 'f_score':
			# obtain the f-score of each feature
			score = f_score.f_score(X, Y)
			# rank features in descending order according to score
			idx = f_score.feature_ranking(score)
			print(idx.shape)
			print(idx)
			# obtain the dataset on the selected features
			X = X[:, idx[0:num_fea]]
			print(X.shape)


		elif Data.feature_selection == 't_score':
			# obtain the t-score of each feature
			score = t_score.t_score(X, Y)
			# rank features in descending order according to score
			idx = t_score.feature_ranking(score)
			print(idx.shape)
			print(idx)
			# obtain the dataset on the selected features
			X = X[:, idx[0:num_fea]]
			print(X.shape)

		else:
			# define feature selection
			fs_method = Data.feature_selection
			fs_param = float(Data.feature_selection_param)
			if fs_method == 'k_best' or fs_method == 'percentile':
				fs_param = int(Data.feature_selection_param)
			
			fs = GenericUnivariateSelect(score_func=f_classif, mode=fs_method, param=fs_param)
			# apply feature selection
			X = fs.fit_transform(X, Y)
			print(X.shape)


		# data_feature_names = Data.feature_vector.columns
		# print(data_feature_names)
		# Train.extract_informative_features(idx, data_feature_names)

		if len(X) /  Data.cross_validation < 2:
			Data.cross_validation = 5
		# print(Data.cross_validation)
		
		sklearn_model.model_train_and_evaluate( Data.model_name, X, Y, Data.cross_validation)
    
	@staticmethod
	def extract_informative_features(idx, data_feature_names):
		informative_features_dict = {}
		num = 0
		for i in idx:
			num += 1 
			informative_features_dict[num] = data_feature_names[i]

		print(informative_features_dict)

		file_name = 'features/fs_%s_pt_%s_interface_%s_product_%s_feature.json' % (Data.feature_selection, Data.personality_trait, Data.interface, Data.product)
		with open(file_name, 'w') as fs:
			json.dump(informative_features_dict, fs, indent=4)

		