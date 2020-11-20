#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
df = pd.read_csv (r'C:\Users\Hanisha\Downloads\axisdata.csv')
print (df)


# In[5]:


df['Cars Sold'].mean()


# In[6]:


df['Cars Sold'].max()


# In[7]:


df['Cars Sold'].min()


# In[11]:


pd.pivot_table(df,
 values=['Cars Sold'],
 index=['Gender'])


# In[36]:


df.loc[df['Cars Sold']>3].mean()
      


# In[37]:


df['Years Experience'].mean()


# In[39]:


df.loc[df['CarsSold']>3]
df['Years Experience'].mean()


# In[50]:


df = df.sort_values((by=['SalesTraining']='Y',
                    ascending=[True]))
df.head()


# In[65]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "C:/Users/Hanisha/Downloads/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[67]:


df.hist(column="Hours Worked", by="Gender")


# In[68]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
dataframe = pd.DataFrame({'Col':
 np.random.normal(size=200)})
plt.scatter(dataframe.index, dataframe['Col'])


# In[ ]:




