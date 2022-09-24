#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.getcwd()


# In[2]:


os.chdir('/Users//ergin/OneDrive/Masaüstü/hello_ds')


# In[3]:


os.getcwd()


# In[4]:


import pandas as pd


# In[5]:


first_period_accidents = pd.read_csv("accidents_2005_to_2007.csv")


# In[6]:


second_period_accidents = pd.read_csv("accidents_2009_to_2011.csv")


# In[7]:


third_period_accidents = pd.read_csv("accidents_2012_to_2014.csv")


# In[8]:


first_period_accidents


# In[9]:


second_period_accidents


# In[10]:


third_period_accidents


# In[11]:


first_period_accidents.describe()


# In[12]:


second_period_accidents.describe()


# In[13]:


third_period_accidents.describe()


# In[14]:


total_accidents_selection = [first_period_accidents, second_period_accidents, third_period_accidents]
total_accidents = pd.concat(total_accidents_selection)


# In[15]:


total_accidents


# In[ ]:




