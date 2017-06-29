# -*- coding:utf-8 -*-  
import re
from urllib.request import urlopen

resp = urlopen("http://www.imooc.com/").read().decode("utf-8")
listurl = re.findall(r'http://img.mukewang.com/.+?\.jpg',resp)

#print(listurl)
for url in listurl:
    f = open(url.split('/')[-1],'wb+')
    req = urlopen(url)
    buf = req.read()
    f.write(buf)
    f.close()
