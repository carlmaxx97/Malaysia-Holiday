#!/usr/bin/env python
# coding: utf-8

# In[282]:


from tabula.io import read_pdf
import pandas as pd
import re


# In[283]:


file = 'http://www.kabinet.gov.my/bkpp/pdf/hari_kelepasan_am/hka_2021.pdf'
data  = read_pdf(file,pages = 'all', stream=True)
print(data)


# In[284]:


df1 = data[0].reset_index().T.reset_index().T[4]
print(df1)


# In[285]:


df2 = data[1].reset_index().T.reset_index().T[4]
print(df2)


# In[286]:


df3 = data[3].reset_index().T.reset_index().T[3]
print(df3)


# In[287]:


l1=list(df1)
l1.pop(0)


# In[288]:


l2=list(df2)
l2.pop(0)


# In[289]:


l3=list(df3)
l3.pop(0)


# In[290]:


holidays=l1+l2+l3
year="2021"
holidays = [word.replace("Januari", "January "+year) for word in holidays]
holidays = [word.replace("Februari", "February "+year) for word in holidays]
holidays = [word.replace("Mac", "March "+year) for word in holidays]
holidays = [word.replace("April", "April "+year) for word in holidays]
holidays = [word.replace("Mei", "May "+year) for word in holidays]
holidays = [word.replace("Jun", "June "+year) for word in holidays]
holidays = [word.replace("Julai", "July "+year) for word in holidays]
holidays = [word.replace("Ogos", "August "+year) for word in holidays]
holidays = [word.replace("September", "September "+year) for word in holidays]
holidays = [word.replace("Oktober", "October "+year) for word in holidays]
holidays = [word.replace("November", "November "+year) for word in holidays]
holidays = [word.replace("Disember", "December "+year) for word in holidays]
from datetime import datetime

holidays = [datetime.strptime(word, "%d %B %Y") for word in holidays]
holidays = [word.strftime("%Y-%b-%d") for word in holidays]
holidays.sort()
print(list(dict.fromkeys(holidays)))


# In[291]:


import json
json_string = json.dumps(list(dict.fromkeys(holidays)))
print(json_string)
with open('holidays.json', 'w') as f:
    json.dump(list(dict.fromkeys(holidays)), f)


# In[ ]:





# In[ ]:




