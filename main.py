from multiprocessing import Pool
import download
from time import sleep
import json
import login
from tqdm import tqdm
from selenium import webdriver
import urllib2
# def main(key):
#     data = {"0": "-5KQ66BBWC4", "1": "-FaXLcSFjUI", "2": "-IELREHX_js"}
#     print 'prosess:%d'%key
#     download.download(data.get(str(key)))
if __name__ == "__main__":
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
    '''
    #IF YOU FIRST USE,PLEASE Cancel annotation
    
    
    login.login('-FaXLcSFjUI')
    
    
    '''
    outstream=open('outstream.txt','a')
    outerro = open('outerro.txt', 'a')
    erro403=open('erro403.txt','a')
    havedownlist=open('havedownlist.txt','a')

    '''
    
    #IF YOU FIRST USE,PLEASE Cancel annotation
    #GET STREAMURL AND DELETE INVALIDED VIDEO,
    for i in tqdm(id_data.values()):
        sleep(0.01)
        try:
            stream=login.getstream(i)
        except AttributeError:
            invalided_data.append(i)
            print 'invalided_erro '+i+ ':' + 'NoneType object has no attribute group'
        else:
            stream_list.append(stream)
            outstream.write(i+':'+stream+'\n')
        #download.download(i,stream)
    for i in invalided_data:
        outerro.write(i+'\n')
        
    '''

    f = open('outstream.txt', 'r')
    for i in tqdm(f.readlines()):
        sleep(0.01)
        print '\n'
        id = i.split(':')[0]
        streamurl = i.split(':')[1]+':'+i.split(':')[2][:-1]
        #print str(streamurl)
        try:
            download.download(id, streamurl)
        except urllib2.HTTPError:
            erro403_list.append(id)
            erro403.write(id + '\n')
            print '430erro ' + id + ':' + 'HTTP Error 403: Forbidden'
        else:
            havedown_list.append(id)
            havedownlist.write(id+'\n')
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