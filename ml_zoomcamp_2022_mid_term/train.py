#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np


#from pandas_profiling import ProfileReport
import seaborn as sns
from matplotlib import pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')

import pickle


# # Data Preparartion

print(f'Data preparation started')
df_train_full = pd.read_csv('train.csv')


# takes too much time
# # The data profiling is okay but it has too much description to work with
# profile = ProfileReport(df_train_full)
# profile


df_train_full.head().T


df_train_full.dtypes


df_train_full['OUTCOME'].unique()



df_train_full['OUTCOME'] = df_train_full['OUTCOME'].astype(int)


#df_train_full.dtypes


#converting the columns names without spaces
df_train_full.columns = df_train_full.columns.str.lower().str.replace(' ', '_')

# converting the string values in columns by removing the space between them
string_columns = list(df_train_full.dtypes[df_train_full.dtypes == 'object'].index)

for col in string_columns:
    df_train_full[col] = df_train_full[col].str.lower().str.replace(' ', '_')




#df_train_full.head().T



df_train_full.dtypes[df_train_full.dtypes == 'object']



# separating into categroical and numerical variables
categorical = ['age', 'gender', 'driving_experience', 'education', 'income', 'vehicle_ownership', 
               'married', 'children', 'postal_code', 'speeding_violations', 'duis', 'past_accidents', 
               'vehicle_year', 'type_of_vehicle']
numerical = [ col for col in df_train_full.columns if col not in categorical]

(len(categorical) + len(numerical) ) == len(df_train_full.columns) #checking if any of the colums are left out

numerical.remove('outcome')

print(f'Data preparation ended')

# # Splitting the data into train,val as test data is already present
# 

print(f'Splitting into train and val set started')

from sklearn.model_selection import train_test_split

train_df, val_df = train_test_split(df_train_full, test_size=0.2, random_state=1)


# test_df = pd.read_csv('test.csv') no testing is done here


# len(train_df), len(val_df), len(test_df)

y_train = train_df.outcome.values
y_val = val_df.outcome.values


del train_df['outcome']
del val_df['outcome']

print(f'Splitting into train and val set ended')

# # Training the model
print(f'Training the model started')

# In[27]:


from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve


# In[28]:


columns = categorical + numerical


# In[29]:


if('outcome' in columns):
    print('yes')
else:
    print('no')



C=1.0


# In[31]:


train_dicts = train_df[columns].to_dict(orient='records')
dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(train_dicts)


# In[38]:


# train_dicts[1534], y_train[1534]


# In[32]:


model = LogisticRegression(solver='liblinear', C=1.0, max_iter=1000)
model.fit(X_train, y_train)


# In[33]:


val_dicts = val_df[columns].to_dict(orient='records')
X_val = dv.transform(val_dicts)

y_pred = model.predict_proba(X_val)[:, 1]


# In[34]:


#y_pred


# In[35]:


#roc_auc_score(y_val, y_pred)
print(f'Training the model ended')


## Save the model
print(f'Saving the model started')

output_file = f'model_C={C}.bin'


with open(output_file, 'wb') as f_out: 
    pickle.dump((dv, model), f_out)

print(f'Model saved to current path as "{output_file}"')

print(f'Saving the model ended')
