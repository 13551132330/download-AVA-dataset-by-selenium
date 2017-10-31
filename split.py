# import imageio
# imageio.plugins.ffmpeg.download()
from moviepy.editor import *
import os
def split(id):
    begin=904
    while begin<=1798:
        filename='E:\lin\AVA\source\%s.mp4'%id
        splitpath='E:\lin\AVA\split\%s'%id
        print filename
        video=VideoFileClip(filename).subclip(begin+1,begin+4)
        result=CompositeVideoClip([video,])
        isExists=os.path.exists(splitpath)
        if not isExists:
            os.makedirs(splitpath)
        result.write_videofile(os.path.join(splitpath,'%d-%d.mp4'%(begin,begin+3)))
        begin+=3
