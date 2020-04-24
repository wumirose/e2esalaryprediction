#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
url = 'http://localhost:5000/predict_api'

r = requests.post(url, json = {'experience': 2, 'test_score': 9, 'interview_score': 6})

print(r.json())


# In[ ]:




