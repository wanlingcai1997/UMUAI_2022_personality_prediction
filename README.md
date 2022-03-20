# Eye Tracking Based Personality Prediction

This is the implementation of our work on "Eye-Tracking based Personality Prediction with Recommendation Interfaces". If you find our repository useful in your paper, please cite our paper.

### Paper

------

- Li Chen, Wanling Cai, Dongning Yan, and Shlomo Berkovsky. 2022. *User Modeling and User-Adapted Interaction* (*UMUAI*) [Under Review]


### Code Dependency

****

**Python 3.7**

**Required Packages:** Scikit-learn, Numpy, Pandas, XGBoost, [scikit-feature](https://github.com/jundongl/scikit-feature)



### Usage

Due to the ethical consideration, we cannot share the collected user data.

We manually generate some data as example data (in the folder ``\ExampleData``) for running the models.

Below are examples of how to run our codes for predicting user personality with machine learning models.

Go to the folder  ``\personality_prediction`` and run the example script. For instance:

```py
python Main.py 
--file_ALL ../ExampleData/AllData.xlsx 
--file_LIST ../ExampleData/data_LIST.xlsx 
--file_ORG ../ExampleData/data_ORG.xlsx 
--personality_trait O 
--interface ALL 
--product ALL
--feature_selection gini_index 
--feature_selection_param 12 
--model_name AdaBoost 
--cross_validation 10 
```

Some Parameters:

- ``personality_trait``: The personality to be predicted, which can be ['O', 'C', 'E', 'A', 'N']. 
- ``interface``: The data of which recommendation interface used for prediction, which can be ['LIST', 'ORG', 'ALL']
- ``product``: The data of which product domain used for prediction, which can be ['phone', 'movie', 'hotel', 'ALL']
- ``feature_selection``: Feature selection methods, which can be ['CFS','gini_index', 'f_score', 't_score', 'fisher_score'].
- ``feature_selection_para``: The number of selected features for prediction. 
- ``model_name``: The machine learning models, which can be  [ 'AdaBoost', 'XGBoost', 'GBDT', 'RF', 'DT', 'NB', 'LR', 'SVM', 'MLP']
- ``cross_validation``: The configuration for k-fold cross*-*validation. The default is 10.