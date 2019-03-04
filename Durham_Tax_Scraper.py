#!/usr/bin/env python
# coding: utf-8

# In[98]:



from splinter import Browser
from bs4 import BeautifulSoup
import time
import pymongo
import requests
from splinter.exceptions import ElementDoesNotExist
import pandas as pd


# In[161]:




def init_browser():

        executable_path = {"executable_path": "chromedriver.exe"}
        return Browser("chrome", **executable_path, headless=False)



# In[185]:


address = 'Princess Pl'
browser = init_browser()
url = 'https://property.spatialest.com/nc/durham/#/'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

results = soup.find_all('input', class_='search')
print(results)


# In[190]:


browser.find_by_id('primary_search').first.fill(address)


# In[191]:


browser.click_link_by_partial_href('#') 


# In[192]:


browser.click_link_by_partial_href("#/property")


# In[193]:


property_link = browser.html
prop_link = BeautifulSoup(property_link, 'html.parser')


# In[194]:


prop_img = prop_link.find('img', class_='img-thumbnail')['src']
prop_img


# In[195]:


prop_mailing = prop_link.find('div', class_='mailing')
prop_mailing.text


# In[196]:


sales = []
prop_table = prop_link.findAll('table')[3]
for tr in prop_table.findAll('tr'):
    for td in tr.findAll('td'):
        sales.append(td.text)
sales[0]


# In[197]:


browser.click_link_by_partial_text('sults') 


# In[198]:


property_link1 = browser.html
prop_link1 = BeautifulSoup(property_link1, 'html.parser')
prop_link1
prop_list = []
addresses = prop_link1.findAll('div', class_="item-1")
for address in addresses:
    prop_list.append(address.text)


# In[199]:


browser.click_link_by_partial_text('Next') 


# In[200]:


property_link2 = browser.html
prop_link2 = BeautifulSoup(property_link2, 'html.parser')
prop_link2

addresses = prop_link2.findAll('div', class_="item-1")
for address in addresses:
    prop_list.append(address.text)
prop_list


# In[210]:



for prop in prop_list:
    browser.find_by_id('primary_search').first.fill(prop)
    time.sleep(3)
    browser.click_link_by_partial_href('#') 
    time.sleep(5)
    browser.find_by_id('primary_search').clear()
    time.sleep(3)


# In[ ]:





# In[ ]:




