# -*- coding: utf-8 -*-
from __future__ import absolute_import
from pytube import YouTube
import requests
import split
import os
import re
import json
from bs4 import BeautifulSoup
import urlparse
import shutil
from pytube import request
from time import sleep
from tqdm import tqdm
import urllib2
import urllib
from selenium import webdriver
import download
#path='D:\phantomjs-2.1.1-windows\\bin\phantomjs.exe'
driver = webdriver.Chrome()
import getid
def login(id):
    username='your name'
    password='your password'
    session = requests.Session()
    yt='https://www.youtube.com/watch?v=%s'%id
    res=session.get(yt)
    #f=open('C:\Users\U\Desktop\lin\html\index.html','wb+')
    #f = open('C:\Users\U\Desktop\lin\html\index.html', 'r')
    #f.write(res.text)
    #print res.text
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(type(soup))
    #f.write(soup.prettify().encode('utf-8'))
    for i in soup.find_all('a',class_='sign-in-link'):
        #print i['href']
        driver.get(i['href'])
        email=driver.find_element_by_name('identifier')
        email.send_keys(username)
        next=driver.find_element_by_id('identifierNext')
        next.click()
        sleep(6)
        passw=driver.find_element_by_name('password')
        passw.send_keys(password)
        next2 = driver.find_element_by_id('passwordNext')
        next2.click()
def getstream(id):
        sleep(6)
        driver.get('https://www.youtube.com/watch?v=%s'%id)
        res2 = driver.page_source
        #driver.close()
        # soup2 = BeautifulSoup(res2, 'html.parser')
        # f.write(soup2.prettify().encode('utf-8'))

        stream=download.findstream(id,res2)

        return stream

        #download.download(id,stream)
    #login=session.post(i['href'],data=data)
    #res3=session.get(login)
    # soup3 = BeautifulSoup(login.text, 'html.parser')
    # f.write(soup3.prettify().encode('utf-8'))
# print 'we are getstream~~~~~~~~~~~\n'
#m=re.search('"url_encoded_fmt_stream_map":(".*?"),',soup.text)
# f.write(m.group(1))
#print len(m.group())
#print str(m.group(1))
