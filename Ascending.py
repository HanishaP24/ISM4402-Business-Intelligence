#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
Location = "C:/Users/Hanisha/Downloads/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[12]:


df = df.sort_values(by=['lname', 'age', 'gender'],
        ascending=[True, True, True])
df.head()


# In[ ]:




