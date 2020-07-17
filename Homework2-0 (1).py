#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
import pylab
from seaborn import heatmap
from sklearn.preprocessing import OneHotEncoder
from scipy import stats
from scipy.stats import shapiro
import pylab as py
import statsmodels.api as sm
import statsmodels.stats.api as sms


# In[52]:


os.getcwd()


# In[53]:


os.chdir("C:\\Users\\User\\Desktop")


# In[54]:


data = pd.read_csv("hmelq.csv") 


# In[55]:


data.info()


# In[56]:


data.dtypes


# In[57]:


data.shape


# In[58]:


data.head()


# In[59]:


data= data.dropna()
data.shape


# In[60]:


data.corr()


# In[61]:


from seaborn import heatmap
sns.set_palette("RdBu")
correlation=data.corr()
sns.heatmap(correlation)
plt.show


# In[62]:


data.ninq.describe()


# In[63]:


sns.countplot(x="bad", data=data)


# In[64]:


sns.catplot(x="bad", y="ninq", data=data , kind="box")


# In[65]:


pd.crosstab(data["ninq"], data["bad"],normalize="columns")


# In[66]:


stats.probplot(data.loan, dist= "norm", plot = pylab)


# In[67]:


stats.probplot(data.value, dist= "norm", plot = pylab)


# In[68]:


sns.catplot(x="bad", y="value", data=data , kind="box")


# In[148]:


sns.scatterplot(x="value", y="mortdue", data=data, hue="bad")


# In[70]:


sns.scatterplot(x="loan", y="value", data=data, hue="reason")


# In[71]:


fig, ax= plt.subplots()
ax.hist(data.reason, label="Reason")
ax.set_xlabel("Reason")
ax.set_ylabel("Number of Applicants")
plt.show


# In[72]:


sns.catplot(x="reason", y="value", data=data , kind="box")


# In[ ]:





# In[73]:


sns.countplot(x="job", data=data)


# In[74]:


sns.catplot(x="job", y="loan", data=data , kind="box")


# In[75]:


sns.scatterplot(x="loan", y="yoj", data=data, hue="reason")


# In[76]:


sns.scatterplot(x="ninq", y="debtinc", data=data, hue="reason")


# In[77]:


sns.catplot(x="bad", y="loan", data=data , kind="box")


# In[78]:


a = data.groupby('bad')['loan'].apply(list)


# In[79]:


g = data.groupby('bad')


# In[80]:


for bad, bad_data in g:
    print(bad)
    print(bad_data)


# In[ ]:





# In[84]:


dataA = g.get_group(0)
dataB = g.get_group(1)


# In[98]:


a = pd.DataFrame(dataA)
b = pd.DataFrame(dataB)
a.head()


# In[99]:


b.head()


# In[94]:


shapiro(dataA['loan'])


# In[86]:


shapiro(dataB['loan'])


# In[89]:


stats.ttest_ind(dataA.loan, dataB.loan)


# In[100]:


sns.catplot(x="bad", y="mortdue", data=data , kind="box")


# In[101]:


shapiro(dataA['mortdue'])


# In[102]:


shapiro(dataB['mortdue'])


# In[104]:


stats.ttest_ind(dataA.mortdue, dataB.mortdue)


# In[105]:


sns.catplot(x="bad", y="value", data=data , kind="box")


# In[144]:


data.value.describe()


# In[106]:


shapiro(dataA['value'])


# In[107]:


shapiro(dataB['value'])


# In[108]:


stats.ttest_ind(dataA.value, dataB.value)


# In[110]:


pd.crosstab(data["job"], data["bad"],normalize="columns")


# In[111]:


pd.crosstab(data["bad"], data["job"],normalize="columns")


# In[112]:


sns.catplot(x="job", kind="count", data=dataA)


# In[113]:


sns.catplot(x="job", kind="count", data=dataB)


# In[114]:


sns.catplot(x="bad", y="debtinc", data=data , kind="box")


# In[115]:


data.debtinc.describe()


# In[116]:


data.yoj.describe()


# In[118]:


sns.catplot(x="bad", y="yoj", data=data , kind="box")


# In[131]:


sns.catplot(x="reason", kind="count", data=dataA, palette='rainbow')


# In[132]:


pd.crosstab(data["reason"], data["bad"],normalize="columns")


# In[133]:


sns.catplot(x="reason", kind="count", data=dataB, palette='rainbow')


# In[135]:


stats.levene(dataA.loan,dataB.loan)


# In[136]:


stats.levene(dataA.value,dataB.value)


# In[137]:


stats.levene(dataA.mortdue,dataB.mortdue)


# In[138]:


shapiro(dataB['debtinc'])


# In[139]:


shapiro(dataA['debtinc'])


# In[140]:


stats.levene(dataA.loan,dataB.loan)


# In[141]:


stats.ttest_ind(dataA.debtinc, dataB.debtinc)


# In[147]:


pd.crosstab(data["reason"], data["bad"],normalize="columns")


# In[ ]:




