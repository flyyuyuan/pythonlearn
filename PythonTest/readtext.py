# -*- coding:utf-8 -*-  
from urllib.request import urlopen



resp = urlopen("https://en.wikipedia.org/robots.txt").read().decode("utf-8")
print(resp)
