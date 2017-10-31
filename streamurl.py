from selenium import webdriver
import time
from bs4 import BeautifulSoup
f=open('outstream.txt','r')
for i in f.readlines():
    id=i.split(':')[0]
    streamurl=i.split(':')[1]+':'+i.split(':')[2][:-1]
    print streamurl

