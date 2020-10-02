#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
Location = "C:/Users/Hanisha/Downloads/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[7]:


import numpy as np
df['Busy'] = np.where((df['excercise']>3) & (df['hours']>17), 'yes', 'no')
df.tail(10)


# In[ ]:




