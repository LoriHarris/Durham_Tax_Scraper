#!/usr/bin/env python
# coding: utf-8

# In[2]:



from splinter import Browser
from bs4 import BeautifulSoup
import time
import pymongo
import requests
from splinter.exceptions import ElementDoesNotExist
import pandas as pd
from flask_pymongo import PyMongo
from flask import Flask
# In[3]:





def init_browser():

    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)



# In[15]:


def tax():
    app = Flask(__name__)
    mongo = PyMongo(app, uri="mongodb://localhost:27017/tax_app")

    address = mongo.db.input.distinct('Query')
    # address = "Ripley St" 
    browser = init_browser()
    url = 'https://property.spatialest.com/nc/durham/#/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find_all('input', class_='search')
    browser.find_by_id('primary_search').first.fill(address)
    time.sleep(3)
    browser.click_link_by_partial_href('#')
    time.sleep(3)
    data = browser.url
    browser.visit(data)

    property_link1 = browser.html
    prop_link1 = BeautifulSoup(property_link1, 'html.parser')
    prop_link1
    prop_list = []
    addresses = prop_link1.findAll('div', class_="item-1")
    for address in addresses:
        prop_list.append(address.text)
    time.sleep(2)
    next_list =  browser.find_by_text('Next')
    time.sleep(2)
    while len(next_list)>0:
        try:
            next_list =  browser.find_by_text('Next')
            browser.click_link_by_partial_text('Next') 
            time.sleep(3)
            data1 = browser.url
            browser.visit(data1)

            property_link1 = browser.html
            prop_link1 = BeautifulSoup(property_link1, 'html.parser')
            prop_link1

            addresses1 = prop_link1.findAll('div', class_="item-1")
            for address1 in addresses1:
                prop_list.append(address1.text)
            for next1 in next_list:
                next_list.remove(next1)
        except:
            prop_list

    browser.click_link_by_partial_href('spatialest')
    time.sleep(3)
    prop_mailing1 = []    
    address = []
    price = []
    date = []
    while len(prop_list)>0:
        try:
            for prop in prop_list:
                browser.find_by_id('primary_search').first.fill(prop)
                time.sleep(3)
                browser.click_link_by_partial_href('#') 
                time.sleep(5)
                data = browser.url
                browser.visit(data)
                time.sleep(3)
                property_link3 = browser.html
                prop_link = BeautifulSoup(property_link3, 'html.parser')
                prop_mailing = prop_link.find('div', class_='mailing')
                prop_mailing1.append(prop)
                address.append(prop)
                prop_table = prop_link.findAll('table')[3]
                price_table = prop_table.findAll('td')[1]
                date_table = prop_table.findAll('td')[0]
                for x in price_table:
                    price.append(x)
                for y in date_table:
                    date.append(y)
                browser.click_link_by_partial_href('spatialest')
                time.sleep(3)
                prop_list.remove(prop)
                print(len(prop_list))
        except:

            prop_list.remove(prop)
            print(len(prop_list))
            browser.click_link_by_partial_href('spatialest')
            time.sleep(2)
        df1 = pd.DataFrame(columns=['Address', 'Price', 'Date'])
        df1['Address']=address
        df1['Price']=price
        df1['Date']=date
        table = df1.to_html(classes="table")
        table.replace('\n', '')
        df1.to_html('table.html')
        df = {
        'Address': address, 
        'Price': price, 
        'Date': date,
        'Table': table,
        }
        
    return df


# In[16]:



# In[14]:


# df = pd.DataFrame(columns=['Address', 'Price', 'Date'])
# df['Address']=address
# df['Price']=price
# df['Date']=date
# df


# In[ ]:


# df.to_csv('Barringer3.csv', encoding='utf-8', index=False)


# In[ ]:





# In[ ]:




