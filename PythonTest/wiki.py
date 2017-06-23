# -*- coding:utf-8 -*-  
from urllib.request import urlopen
#from urllib.request import Request
#from urllib import parse
from bs4 import BeautifulSoup
import re


resp = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")
soup = BeautifulSoup(resp,"html.parser")

data = soup.find_all("a",href=re.compile(r"^/wiki/"))
for link in data:
    if not re.search("jpg$",link["href"]):
        print(link.get_text()+"<-->"+"https://en.wikipedia.org"+link["href"])
