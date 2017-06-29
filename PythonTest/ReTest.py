# -*- coding:utf-8 -*-  
import re

#ma = re.match(r'\[\d*\]','[123457777]')
#print(ma.group())

#ma = re.match(r'[A-Z][a-z]*','Aasdsada1')
#print(ma.group())

#ma1 = re.match(r'[_a-zA-Z]+[_\w]+','html1')
#print(ma1.group())

#0-99
#ma1 = re.match(r'[1-9]?[0-9]','0')
#print(ma1.group())

#eamil  6-10位置的163邮箱
#ma1 = re.match(r'[a-zA-z0-9]{6,10}@163.com','abc12311122@163.com')
#print(ma1.group())

#非贪婪模式
#ma1 = re.match(r'[0-9][a-z]??','1bc')
#print(ma1.group())

#eamil  6-10位置的163邮箱  ^$开始结束匹配
#ma1 = re.match(r'^[a-zA-z0-9]{6,10}@163.com$','abc1231112@163.com')
#print(ma1.group())

#eamil  6-10位置的163邮箱  \A \Z开始结束匹配
#ma1 = re.match(r'\Aimooc[\w]*zz\Z','imoocyyyzz')
#print(ma1.group())

# | 匹配0-100
#ma1 = re.match(r'[1-9]?\d$|100','99')
#print(ma1.group())

# | 匹配163  126
#ma1 = re.match(r'[\w]{4,6}@(163|126).com','imooc@126.com')
#print(ma1.group())

# | 匹配xml   <book>python</book>
#ma1 = re.match(r'<([\w]+>)[\w]+</\1','<book>python</book>')
#print(ma1.group())

# | 匹配xml  别名  <book>python</book>
#ma1 = re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)','<book>python</book>')
#print(ma1.group())


#search（pattern ,string ,flags=0）方法 在一个字符串中查找匹配
#str1 = 'imooc videomun=1000'
#info  = re.search(r'\d+',str1)
#print(info)

#findall(pattern,stringflags=0) 找到所有匹配的列表
#str1 = "c++=100,java=90,python=80"
#info = re.findall(r'\d+',str1)
#print(info)
#iif = sum(int(x) for x in info)
#print(iif)

#sub(pattern,repl,string,count=0,flag=0) 将字符串中匹配的正则表达式部分替换掉
str2 = 'imooc videosnum = 1000'
info = re.sub(r'\d+','1001',str2)
print(info)

def add1(match):
    val = match.group()
    num = int(val)
    return  str(num)
info1 = re.sub(r'\d+',add1,str2)


#spilt(pattern,strng,maxsplit=0,flag=0) 根据匹配字符串分隔字符串，返回列表
str3 = 'imooc:c c++ java python'
info = re.split(r':| ',str3)
print(info)

str4 = 'imooc:c c++ java python,C#'
info = re.split(r':| |,',str4)
print(info)














