#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
import pylab
from seaborn import heatmap
from sklearn.preprocessing import OneHotEncoder
from scipy import stats
import pylab as py
import statsmodels.api as sm
import statsmodels.stats.api as sms


# In[2]:


os.getcwd()


# In[5]:


os.chdir("C:\\Users\\User\\Desktop")


# In[6]:


data = pd.read_csv("hmelq.csv")


# In[7]:


data.info()


# In[8]:


data.dtypes


# In[9]:


data.shape


# In[10]:


data.head()


# In[12]:


data= data.dropna()
data.shape


# In[ ]:





# In[34]:


sns.countplot(x="bad", data=data)


# In[17]:


sns.catplot(x="bad", y="loan", data=data , kind="box")


# In[18]:


stats.probplot(data.loan, dist= "norm", plot = pylab)


# In[19]:


sns.catplot(x="bad", y="value", data=data , kind="box")


# In[21]:


sns.scatterplot(x="loan", y="mortdue", data=data, hue="bad")


# In[51]:


sns.scatterplot(x="loan", y="value", data=data, hue="reason")


# In[52]:


fig, ax= plt.subplots()
ax.hist(data.reason, label="Reason")
ax.set_xlabel("Reason")
ax.set_ylabel("Number of Applicants")
plt.show


# In[56]:


sns.catplot(x="reason", y="value", data=data , kind="box")


# In[33]:


sns.countplot(x="job", data=data)


# In[47]:


from seaborn import heatmap
sns.set_palette("RdBu")
correlation=data.corr()
sns.heatmap(correlation)
plt.show


# In[ ]:




