#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd 
import numpy as np 
import random
from IPython.display import Image
from IPython.core.display import HTML
from pandas.io.json import json_normalize

get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes')
import folium 
print('Libraries imported.')


# In[9]:


source = requests.get("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M").text
soup = BeautifulSoup(source, 'lxml')

table = soup.find("table")
table_rows = table.tbody.find_all("tr")

res = []
for tr in table_rows:
    td = tr.find_all("td")
    row = [tr.text for tr in td]
    
    if row != [] and row[1] != "Not assigned":
        if "Not assigned" in row[2]: 
            row[2] = row[1]
        res.append(row)

df = pd.DataFrame(res, columns = ["PostalCode", "Borough", "Neighborhood"])
df.head()


# In[14]:


df["Neighborhood"] = df["Neighborhood"].str.replace("\n","")
df = df.groupby(["PostalCode", "Borough"])["Neighborhood"].apply(", ".join).reset_index()
df.head(10)


# In[ ]:





# In[ ]:





# In[ ]:




