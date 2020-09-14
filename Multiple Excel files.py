#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd
import numpy as np
import glob

all_data = pd.DataFrame(columns=['CallingNumber', 'DayOfWeek', 'TimeofDay', 'CallDuration', 'ReasonForCall', 'AnsweringAgent'])
for f in glob.glob("datasets/datasets/weekdate*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df, ignore_index=True)
all_data.descibe()


# In[ ]:




