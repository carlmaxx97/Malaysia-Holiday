#!/usr/bin/env python
# coding: utf-8

# In[55]:


import urllib.request
import sys
from datetime import date

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
api = sys.argv[1]
url = "https://calendarific.com/api/v2/holidays?&api_key="+api+"&country=MY&year="+str(date.today().year)
headers={'User-Agent':user_agent,} 

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read() # The data u need


# In[53]:


import json
todos = json.loads(data)
l = []
for todo in todos['response']['holidays']:
        l.append(todo['date']['iso'][0:10])
with open('holidays.json', 'w') as f:
    json.dump(l, f)
    

