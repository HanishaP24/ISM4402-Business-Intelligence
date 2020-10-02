#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
Location = "C:/Users/Hanisha/Downloads/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[6]:


import numpy as np
df['Failing'] = np.where(df['grade']<80, 'yes', 'no')
df.tail(10)


# In[ ]:




