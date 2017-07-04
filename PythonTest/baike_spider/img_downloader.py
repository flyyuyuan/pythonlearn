# -*- coding:utf-8 -*-  
import re
from urllib.request import urlopen

class ImgDownloader(object):

    def getImg(self,data):
        if data['pic_url'] is None:
            return None
        
        resp = urlopen(data['pic_url'])

        if resp.getcode()!=200:
            return None
        #print (url)
        f = open(data['pic_url'].split('/')[-1],'wb+')
        req = urlopen(data['pic_url'])
        buf =req.read()
        f.write(buf)
        f.close()
