#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
Location = "C:/Users/Hanisha/Downloads/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[ ]:


import statsmodels.formula.api as sm
result = sm.ols(
         formula=)

