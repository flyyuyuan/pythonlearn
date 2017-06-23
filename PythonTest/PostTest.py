# -*- coding:utf-8 -*-  
from urllib.request import urlopen
from urllib.request import Request
from urllib import parse


req = Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")
PostData = parse.urlencode([
    ("StartStation","977abb69-413a-4ccf-a109-0272c24fd490"),
    ("EndStation","e8fc2123-2aaf-46ff-ad79-51d4002a1ef3"),
    ("SearchDate","2017/06/22"),
    ("SearchTime","14:00"),
    ("SearchWay","DepartureInMandarin")
    ])
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36")
req.add_header("Origin", "http://www.thsrc.com.tw")

resp = urlopen(req,data =PostData.encode(encoding='utf_8', errors='strict') )
print(resp.read().decode('utf-8'))
