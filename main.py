from multiprocessing import Pool
import download
from time import sleep
import json
import login
from tqdm import tqdm
from selenium import webdriver
import urllib2
import requests
import getid
import test
# def main(key):
#     data = {"0": "-5KQ66BBWC4", "1": "-FaXLcSFjUI", "2": "-IELREHX_js"}
#     print 'prosess:%d'%key
#     download.download(data.get(str(key)))
if __name__ == "__main__":
    # print 'we are get id,please wait:'
    # getid.get_id()
    data=open('id_list.txt','r')
    #username='346925546@qq.com'
    #password='lzk941210'
    j=1
    id_data={}
    stream_list = []
    invalided_data=[]
    havedown_list=[]
    erro403_list=[]
    for i in data.readlines():
        #print 'we are working on :%d/154,please wait!'%j
        id_data[j]=i[:-1]
        #login.login(i[:-1],username,password)
        j+=1
    #print id_data
    print 'we are working on,please wait!'
    # p = Pool(2)
    # p.map(login.login,list(id_data.values()))

    login.login('-FaXLcSFjUI')

    outstream=open('outstream.txt','a')
    outerro = open('outerro.txt', 'a')
    erro403=open('erro403.txt','a')
    havedownlist=open('havedownlist.txt','a')

    #IF YOU FIRST USE,PLEASE Cancel annotation
    #GET STREAMURL AND DELETE INVALIDED VIDEO,
    for i in tqdm(id_data.values()):
        sleep(0.01)
        try:
            stream=login.getstream(i)
        except :
            invalided_data.append(i)
            outerro.write(i + '\n')
            print 'invalided_erro '+i+ ':' + 'NoneType object has no attribute group'
        else:
            stream_list.append(stream)
            outstream.write(i+':'+stream+'\n')

            try:
                download.download(i, stream)
            except:
                erro403_list.append(i)
                erro403.write(i + '\n')
                print '430erro ' + i + ':' + 'HTTP Error 403: Forbidden'
            else:
                havedown_list.append(i)
                havedownlist.write(i + '\n')
        #download.download(i,stream)
    #stream = login.getstream('55Ihr6uVIDA')
    test.add()
    print 'all down'

    # pool = Pool(2)


    # pool.map(main, (i for i in range(3)))
# if __name__=="__main__":
#     # data= json.load(open("test.json", "r"))
#     # print (list(data.values()))
#     data={"0": "-5KQ66BBWC4", "1": "-FaXLcSFjUI", "2": "-IELREHX_js"}
#     #print list(data.values())
#     # id='-5KQ66BBWC4'
#     # download.download(id)
#     p=Pool(1)
#     p.map(download.download,list(data.values()))