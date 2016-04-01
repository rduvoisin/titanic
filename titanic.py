
# coding: utf-8

# In[1]:

from __future__ import division
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
import operator
import matplotlib.cm as cm
import matplotlib.patches as patches
import math


# In[5]:

train  = pd.read_csv('train.csv')
train.head(50)
train.describe()


# In[6]:

train.columns


# In[7]:

train.dtypes


                
                
# In[8]:

train.head()


# In[19]:

train[(train.Sex=='male') & (train.Survived > 0)].head(10)


                
                
# In[26]:

train['Gender']=train.Sex.map({'female' : 0, 'male' : 1})
train.head(10)
survived = train[train.Survived == 1]


# In[27]:

train.mean()


# In[28]:

survived.mean()


# In[34]:

train[train.Pclass == 3].sort_values('Name').head(20)


# In[35]:

train.columns


# In[37]:

train.shape


# In[48]:

train.Pclass.describe()
train['ses']= train.Pclass
train.ses.describe()
ses_classes = train.sort_values('ses').ses.unique().tolist()
ses_classes, len(ses_classes)


# In[40]:

def get_nice_colors(n_colors):
    '''Helper for plotting colors.'''
    return cm.Accent([1 - (i/n_colors) for i in range(n_colors)])


# In[56]:

plt.close('all')
fig, ax = plt.subplots(figsize=(20,10))
t = 'Survival Rates by SES Group, 1918'
doc = 'daily_crime_rate_bycommunity.png'
proxy_patches = []
proxy_labels = []
ses_list = get_nice_colors(len(ses_classes))
plotting_ses = []
ses_dict = {1 : 'Topsy', 2 : 'Middle', 3: 'Bottomsy'}
for com in ses_classes:
    plotting_ses.append(com)
    median = train[train.ses == com].ses.median()
    proxy_labels.insert(0, "{}, {:.2f}".format(ses_dict[com], median))


train[['Survived', 'ses']].plot(ax=ax, kind='area', rot=90, color=ses_list, title=t)
plt.gcf().tight_layout()
plt.legend(proxy_patches, proxy_labels, title= 'Median Daily Rate')
plt.show()
# fig.savefig(doc)


# In[ ]:



