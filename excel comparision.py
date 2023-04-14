#!/usr/bin/env python
# coding: utf-8

# # Dependencies

# In[1]:


from pathlib import Path # core python module

import pandas as pd
import xlwings as xw # Xlwings allows you to interact with microsoft excel.This can read, write to excel sheet


# # filename

# In[4]:


before_patching = "/Users/ruthwikranganath/Downloads/beforepatching.xlsx"
after_patching = "/Users/ruthwikranganath/Downloads/afterpatching.xlsx"


# # Loading Dataframe

# In[5]:


df_before = pd.read_excel(before_patching)
df_before.head(5)


# In[6]:


df_after = pd.read_excel(after_patching)
df_after.head(5)


# In[7]:


df_before.shape


# In[8]:


df_after.shape


# In[9]:


df_before.shape == df_after.shape


# In[11]:


diff1 = df_after.compare(df_before, align_axis = 1)
diff1


# In[15]:


diff2 = df_before.compare(df_after, keep_shape=True, keep_equal=True)
diff2


diff = df_before.compare(df_after, align_axis=1)
diff.to_excel('/Users/ruthwikranganath/Downloads/diff.xlsx')


# In[ ]:hi




