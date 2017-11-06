import download
import login
import urllib

path = 'E:\lin\AVA\\train'
id='QCLQYnt3aMo'
filename='%s\%s.mp4'%(path,id)
stream=login.getstream(id)
#download.download('HJ4Hcq3YX4k',stream)
urllib.urlretrieve(stream,filename)