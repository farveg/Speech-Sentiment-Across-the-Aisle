# -*- coding: utf-8 -*-
"""Data_Scraper_Fox.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1quufa5UAMhfkx7qcFKzRosmhN018hOGw
"""

! pip install newscatcherapi
from newscatcherapi import NewsCatcherApiClient
import csv
import time
import os.path
import shutil

from google.colab import drive
drive.mount('/content/gdrive')

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/gdrive/MyDrive/Fox Summary

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='Biden',
                                         lang='en',
                                         sources= "foxnews.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Fox_Biden.text", 'a'))
    time.sleep(0.33)

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='Trump',
                                         lang='en',
                                         sources= "foxnews.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Fox_Trump.text", 'a'))
    time.sleep(0.33)

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='pandemic',
                                         lang='en',
                                         sources= "foxnews.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Fox_Pandemic.text", 'a'))
    time.sleep(0.33)

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='vaccine',
                                         lang='en',
                                         sources= "foxnews.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Fox_Vaccine.text", 'a'))
    time.sleep(0.33)

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='Ukraine',
                                         lang='en',
                                         sources= "foxnews.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Fox_Ukraine.text", 'a'))
    time.sleep(0.33)

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='Protest',
                                         lang='en',
                                         sources= "foxnews.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Fox_Protest.text", 'a'))
    time.sleep(0.33)

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='Democrat',
                                         lang='en',
                                         sources= "foxnews.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Fox_Democrat.text", 'a'))
    time.sleep(0.33)

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='Inflation',
                                         lang='en',
                                         sources= "foxnews.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Fox_Inflation.text", 'a'))
    time.sleep(0.33)

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='Republican',
                                         lang='en',
                                         sources= "foxnews.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Fox_Republican.text", 'a'))
    time.sleep(0.33)

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='Election',
                                         lang='en',
                                         sources= "foxnews.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Fox_Election.text", 'a'))
    time.sleep(0.33)