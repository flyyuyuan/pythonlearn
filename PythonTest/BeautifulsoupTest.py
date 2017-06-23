from bs4 import BeautifulSoup
import re
html_doc = """
<html><head><title>The Dormouse's story<a>hello</a></title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://examplescom/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, "html.parser")
#print(soup.prettify())
print("\n head:%s \n title:%s" % (soup.head.get_text(),soup.title.get_text()))
print("\n soup.p:%s " % soup.p)
print("\n class title:%s " % soup.p['class'])

print("\n soup.a:%s " % soup.a)
#print("\n soup.find_all('a'):%s " % soup.find_all('a'))
print("\nLink标签内容：")
for link in soup.find_all('a'):
    print(link.string)
print("\n id='link3':%s " % soup.find(id="link3"))
print("\n id='link3'的内容:%s " % soup.find(id="link3").get_text())

print("\n获取class为story的内容：")
print(soup.find("p",{"class":"story"}).get_text())

print("\n 获取所有内容:%s " % soup.get_text())

print("\n ---------正则表达式---------")
print("\n ---所有以b开头的标签---")
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
print("\n ---所有名字中包含”t”的标签---")
for tag in soup.find_all(re.compile("t")):
    print(tag.name)
print("\n ---所有名字中包含”http://example.com/elsie”的标签---")
data = soup.find_all("a",href=re.compile(r"^http://example\.com"))
print(data)

