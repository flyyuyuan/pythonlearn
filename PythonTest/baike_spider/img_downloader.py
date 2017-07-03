# -*- coding:utf-8 -*-  
import re
from urllib.request import urlopen

class ImgDownloader(object):

    def getImg(self,url):
        if url is None:
            return None
        
        resp = urlopen(url)

        if resp.getcode()!=200:
            return None
        #print (url)
        f = open(url.split('/')[-1],'wb+')
        req = urlopen(url)
        buf =req.read()
        f.write(buf)
        f.close()
