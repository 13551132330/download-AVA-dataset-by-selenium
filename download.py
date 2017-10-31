# -*- coding: utf-8 -*-
from __future__ import absolute_import
from selenium import webdriver
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
def delete(id):
    file = 'E:\lin\AVA\source\%s.mp4'%id
    if os.path.exists(file):
        os.remove(file)
        print 'deleted:%s.mp4'%id
    else:
        print 'no such file:%s' % file
def findstream(id,soup):
    print 'we are getstream~~~~~~~~~~~'
    # yt='https://www.youtube.com/watch?v=%s'%id
    # res=requests.get(yt)
    #f=open('C:\Users\U\Desktop\lin\html\index.html','wb+')
    # f = open('C:\Users\U\Desktop\lin\html\index.html', 'r')
    # f.write(res.text)
    # print res.text
    # soup = BeautifulSoup(res.text, 'html.parser')
    # print(type(soup))
    # f.write(soup.prettify().encode('utf-8'))
    # print 'we are getstream~~~~~~~~~~~\n'
    m=re.search('"url_encoded_fmt_stream_map":(".*?"),',soup)
    #f.write(m.group(1))
    #print len(m.group())
    #print str(m.group(1))
    # print str(m.group(1)).split('url=')[-1].split('\\')[0]
    # req2=requests.get(str(m.group(1)).split('url=')[-1].split('\\')[0],stream=True)
    # f=open('a.mp4','wb')
    # shutil.copyfileobj(req2.raw,f)
    # f.close()
    jd=json.loads(m.group(1))
    #print jd
    a=urlparse.parse_qs(jd)
    #print a
    if ',' in a['url'][0]:
        print 'name:%s\n'%id+'streamURL:'+a['url'][0].split(',')[0]+'\n'
        return a['url'][0].split(',')[0]
    else:
        print 'name:%s\n' % id + 'streamURL:' + a['url'][0] + '\n'
        return a['url'][0]
def download(id,streamURL):
    print 'VIDEO_URL:%s'%streamURL
    print 'loading %s ,please do not close...........'%id
    req2=requests.get(streamURL,stream=True)
    headers = request.get(streamURL, headers=True)
    #print headers['content-length']
    if os.path.exists('E:\lin\AVA\source\%s.mp4'%id) and int(headers['content-length'])==int(os.path.getsize('E:\lin\AVA\source\%s.mp4' % id)):
        print '%s exists,do next'%id
    else:
        f=open('E:\lin\AVA\source\%s.mp4'%id,'wb')
        print 'downloading %s  %dMB,please do not close pycharm:'%(id,int(headers['content-length'])/(1024*1024))
        for i in range(int(headers['content-length'])/(2*1024*1024)):
            sleep(1)
            i+=1
        shutil.copyfileobj(req2.raw,f)
        print '%s down!'%id
    # for i in yt.streams.filter(only_video=True,subtype='mp4').all():
    #     print i
    #download=yt.streams.filter(only_video=True,subtype='mp4').all()[0]
    # print download
    #download.download('E:\lin\AVA\source','%s.mp4'%id)
    # split.split(id)
    # print '%s split down'%id
    # delete(id)

# id='-FaXLcSFjUI'
# #id='-5KQ66BBWC4'
# download(id)
