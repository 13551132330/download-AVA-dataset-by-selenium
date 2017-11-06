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
def usepytube(id):
    yt = 'https://www.youtube.com/watch?v=%s' % id
    res = YouTube(yt)
    video = res.streams.filter(only_video=True, subtype='mp4').all()[0]
    video.download('E:\lin\AVA\\train', '%s.mp4' % id)