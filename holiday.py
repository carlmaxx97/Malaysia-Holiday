#!/usr/bin/env python
# coding: utf-8

# In[55]:


import urllib.request
import sys
from datetime import date

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
api = sys.argv[1]
url = "https://www.googleapis.com/calendar/v3/calendars/en.malaysia%23holiday@group.v.calendar.google.com/events?key="+api
headers={'User-Agent':user_agent,} 

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read() # The data u need


# In[53]:


import json

todos = json.loads(data)
l = []
for todo in todos['items']:
    l.append(todo['start']['date'])
l=list(dict.fromkeys(l))
l.sort()
l=list(filter(lambda k: str(date.today().year) in k, l))

with open('holidays.json', 'w') as f:
    json.dump(l, f)
    

