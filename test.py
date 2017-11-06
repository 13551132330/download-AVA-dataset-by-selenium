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
def add():
    data=open('erro403.txt','r')
    havedownlist = open('havedownlist.txt', 'a')
    id_data={}
    j=0
    for i in data.readlines():
        # print 'we are working on :%d/154,please wait!'%j
        id_data[j] = i[:-1]
        # login.login(i[:-1],username,password)
        j += 1
    for id in id_data.values():
        path='E:\lin\AVA\\train\%s.mp4'%id
        if os.path.exists(path):
            print '%s is exist ,do next'%id
        else:
            yt='https://www.youtube.com/watch?v=%s'%id
            res=YouTube(yt)
            video=res.streams.filter(only_video=True,subtype='mp4').all()[0]
            video.download('E:\lin\AVA\\train','%s.mp4'%id)
            havedownlist.write(id+'\n')