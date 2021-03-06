# -*- coding: utf-8 -*-
"""Data_Scraper_Breitbart.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15f96Y4C57yZ-OjukL5SpaGvj-f34SnHr
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
# %cd /content/gdrive/MyDrive/Breitbart Summary

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='Biden',
                                         lang='en',
                                         sources= "breitbart.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Breitbart_Biden.text", 'a'))
    time.sleep(0.33)

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='Trump',
                                         lang='en',
                                         sources= "breitbart.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Breitbart_Trump.txt", "a"))
    time.sleep(0.33)

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='pandemic',
                                         lang='en',
                                         sources= "breitbart.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Breitbart-pandemic.txt", "a"))
    time.sleep(0.33)

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='vaccine',
                                         lang='en',
                                         sources= "breitbart.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Breitbart_Vaccine.txt", "a"))
    time.sleep(0.33)

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='Ukraine',
                                         lang='en',
                                         sources= "breitbart.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Breitbart_Ukraine.txt", "a"))
    time.sleep(0.33)

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='Protest',
                                         lang='en',
                                         sources= "breitbart.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Breitbart_Protest.txt", "a"))
    time.sleep(0.33)

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='Democrat',
                                         lang='en',
                                         sources= "breitbart.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Breitbart_Democrat.txt", "a"))
    time.sleep(0.33)

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='Inflation',
                                         lang='en',
                                         sources= "breitbart.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Breitbart_Inflation.txt", "a"))
    time.sleep(0.33)

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='Republican',
                                         lang='en',
                                         sources= "breitbart.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Breitbart_Republican.txt", "a"))
    time.sleep(0.33)

newscatcherapi = NewsCatcherApiClient(x_api_key='EcTsDEjSjLEk46mk6G9XBcFWXKVIBBHi2Lfocq7IYs4')

all_articles = newscatcherapi.get_search(q='Election',
                                         lang='en',
                                         sources= "breitbart.com",
                                         page_size=10)

count = 0
articles = all_articles['articles']
for article in articles[:10]:   
    count+=1
    print(str(count) + ". " 
    + "\n\t\t" + article["summary"]\
    + "\n\n",
    file=open("Breitbart_Election.txt", "a"))
    time.sleep(0.33)