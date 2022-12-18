#!/usr/bin/env python
# coding: utf-8



import pandas as pd
import numpy as np

import seaborn as sns
from matplotlib import pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')


# # if the data is present then the below line is not required
# get_ipython().system('wget https://archive.ics.uci.edu/ml/machine-learning-databases/00562/Shill%20Bidding%20Dataset.csv')


print('Loading the dataset')

df = pd.read_csv('Shill Bidding Dataset.csv')

df.head()

df.head().T

df.dtypes



# # EDA, feature importance analysis

df.isnull().sum()

df.Class.value_counts()

df.Class.value_counts(normalize=True)

df.columns


print('selecting the req columns')
remove_cols = ['Record_ID', 'Bidder_ID', 'Class']
numerical = [ cols for cols in df.columns if cols not in remove_cols ]


# `Record_ID` and `Bidder_ID` is unique for each of the record , although there may be one of the request which maybe a  fraud one, so we are keeping the `Auction_ID`. And teh `Class` is to be removed from the list as it is a Class title.

df[numerical].nunique()


# 

# # Splitting into train, test and val
print('Splitting into train, test and val')


from sklearn.model_selection import train_test_split


df_train_full, df_test = train_test_split(df, test_size=0.2, random_state=1)


df_train, df_val = train_test_split(df_train_full, test_size=0.33, random_state=11)

y_train = df_train.Class.values
y_val = df_val.Class.values

del df_train['Class']
del df_val['Class']


# # # Feature importance
# from sklearn.metrics import mutual_info_score

# def mutual_info_churn_score(series):
#     return mutual_info_score(series, df_train_full.Class)


# mi = df_train_full[numerical].apply(mutual_info_churn_score)
# mi.sort_values(ascending=False)


# corr_remove_cols = ['Record_ID', 'Bidder_ID' ]
# corr_heatmap_col = [cols for cols in df_train_full.columns if cols not in corr_remove_cols ]


# corr_heatmap_col



# plt.figure(figsize=(13,7))

# corr_matrix = df_train_full[corr_heatmap_col].corr()
# sns.heatmap(corr_matrix, annot=True)
# plt.show()


# # Successive_Outbidding is the most important predictor of the Class targe var. Winning Ratio and Biding Ratio is somewhat correlated to each other and one of it could be removed from teh feature set to predict the target var. Adding both will have almost the same effect.

# # Training
# 
# * Logistic Regression 
# * RandomForest : https://machinelearningmastery.com/random-forest-ensemble-in-python/
# 

print('Preparing the train and val data for training')

from sklearn.feature_extraction import DictVectorizer

from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve


train_dict = df_train[numerical].to_dict(orient='records')

dv = DictVectorizer(sparse=False)
dv.fit(train_dict)

X_train = dv.transform(train_dict)

X_train.shape

print('training the data using Logistic regression')

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(solver='liblinear', random_state=1)
model.fit(X_train, y_train)

val_dict = df_val[numerical].to_dict(orient='records')
X_val = dv.transform(val_dict)

y_pred = model.predict_proba(X_val)[:, 1]


roc_auc_score(y_val, y_pred)


# recall and precision cureve to understnad the things clearly
y_pred_bin = model.predict(X_val)
roc_auc_score(y_val, y_pred_bin)

plt.figure(figsize=(5, 5))

fpr, tpr, _ = roc_curve(y_val, y_pred)
plt.plot(fpr, tpr, label='probability')

fpr, tpr, _ = roc_curve(y_val, y_pred_bin)
plt.plot(fpr, tpr, label='hard prediction')

plt.plot([0, 1], [0, 1], color='grey', linestyle='--')

plt.legend()
plt.show()



def confusion_matrix_dataframe(y_val, y_pred):
    scores = []

    thresholds = np.linspace(0, 1, 101)

    for t in thresholds:
        actual_positive = (y_val == 1)
        actual_negative = (y_val == 0)

        predict_positive = (y_pred >= t)
        predict_negative = (y_pred < t)

        tp = (predict_positive & actual_positive).sum()
        tn = (predict_negative & actual_negative).sum()

        fp = (predict_positive & actual_negative).sum()
        fn = (predict_negative & actual_positive).sum()

        scores.append((t, tp, fp, fn, tn))

    columns = ['threshold', 'tp', 'fp', 'fn', 'tn']
    df_scores = pd.DataFrame(scores, columns=columns)
    
    return df_scores

df_scores = confusion_matrix_dataframe(y_val, y_pred)
df_scores[::10]


# additing precission(p) and recall(r) column to the above table
df_scores['p'] = df_scores.tp / (df_scores.tp + df_scores.fp)
df_scores['r'] = df_scores.tp / (df_scores.tp + df_scores.fn)

# # INSPECTING THE CURVES:
# plt.plot(df_scores.threshold, df_scores.p, label='precision')
# plt.plot(df_scores.threshold, df_scores.r, label='recall')

# plt.legend()
# plt.show()


# # NOTE: teh intersection is moslty at 0.57 where we have the most optimal values for precision and recall.



fraud_bid = y_pred > 0.57



(y_val == fraud_bid).mean()


# to keep a test data point to check the model after saving and loading it again
train_dict[1534], y_train[1534]


# # Deploying the model
# 
# 1. Saving and loading the model
# 1. Web services: introduction to Flask
# 1. Serving the churn model with Flask
# 1. Python virtual environment: Pipenv
# 1. Environment management: Docker
# 

# ## Saving and loading the model

# ### Save the model
print('Saving the created model')

import pickle

C=1 # just for the sake of keeping the models similar. Should be changea according to the model used.
output_file = f'model_C={C}.bin'

with open(output_file, 'wb') as f_out: 
    pickle.dump((dv, model), f_out)

print(f'Saving the model as {output_file} in the current dir')


