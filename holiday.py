#!/usr/bin/env python
# coding: utf-8

# In[4]:
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('tabula-py')
install('pandas')

# In[5]:


import tabula as tb
import pandas as pd
import re


# In[188]:


file = 'http://www.kabinet.gov.my/bkpp/pdf/hari_kelepasan_am/hka_2021.pdf'
data  = tb.read_pdf(file,pages = 'all', stream=True)


# In[169]:


df1 = data[0].reset_index().T.reset_index().T[4]


# In[170]:


df2 = data[1].reset_index().T.reset_index().T[4]


# In[171]:


df3 = data[3].reset_index().T.reset_index().T[3]


# In[172]:


l1=list(df1)
l1.pop(0)


# In[173]:


l2=list(df2)
l2.pop(0)


# In[174]:


l3=list(df3)
l3.pop(0)


# In[176]:


holidays=l1+l2+l3
print(list(dict.fromkeys(holidays)))


# In[184]:


import json
json_string = json.dumps(list(dict.fromkeys(holidays)))
print(json_string)


# In[187]:


with open('holidays.json', 'w') as f:
    json.dump(list(dict.fromkeys(holidays)), f)

