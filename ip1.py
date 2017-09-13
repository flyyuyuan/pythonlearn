# coding=utf-8

import os,time
import sys

print(os.system('ipconfig'))
start_Time=int(time.time())
ip_True = open('ip_True.txt','w+')
ip_False = open('ip_False.txt','w+')
IPhost = ['192.168.1.1','192.168.1.2']
count_True,count_False = 0,0
for i in IPhost:
    return1=os.system('ping -n 1 -w 1 %s'%i)
    print(return1)
    if return1:
        print ('ping %s is fail'%i)
        ip_False.write(i+'\n')
        count_False += 1
    else:
        print ('ping %s is ok'%i)
        ip_True.write(i+'\n')
        count_True += 1
ip_True.close()
ip_False.close()
end_Time = int(time.time())
print ("time(秒)：",end_Time - start_Time,"s")
print ("ping通的ip数：",count_True,"   ping不通的ip数：",count_False)
