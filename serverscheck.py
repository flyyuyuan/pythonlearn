# -*- coding:utf-8 -*-
# use sched to timing
import time
import os
#import sched
import sys
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
# 初始化sched模块的scheduler类
# 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
#schedule = sched.scheduler(time.time, time.sleep)

def ip_ping():
    print ('------------ ***** ------------')
    print ('------------ start ------------')
    print ('------------ ***** ------------')
    start_Time=int(time.time())
    ip_True = open('ip_True.txt','w+')
    ip_False = open('ip_False.txt','w+')
    IPhost = ['192.168.10.201','192.168.31.162']#59.175.146.61
    IPhosterror=[]
    count_True,count_False = 0,0
    for i in IPhost:
        return1=os.system('ping -n 1 -w 1 %s'%i)
        time.sleep(5)
        if return1:
            print ('--------- %s is fail---------'%i)
            ip_False.write(i+'\n')
            count_False += 1
            IPhosterror.append(i)
        else:
            print ('--------- %s is ok----------'%i)
            ip_True.write(i+'\n')
            count_True += 1
    ip_True.close()
    ip_False.close()
    end_Time = int(time.time())
    #print ("ping执行时间:",datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),"  执行时常(秒)：",end_Time - start_Time,"s")
    #print ("ping通的ip数：",count_True,"   ping不通的ip数：",count_False)
	
    again = 1
    again_num = 6
    if len(IPhosterror)>0:
        for wrongip in IPhosterror:
            while again<again_num:
                r=os.system('ping -n 1 -w 1 %s'%wrongip)
                if r:
                    print ("---------重试：",wrongip,"   失败，次数：",again)
                    again=again+1
                else:
                    print ("---------重试：",wrongip,"   成功，次数：",again)
                    IPhosterror.remove(wrongip)
                    break
                time.sleep(6)
            again=1
    if len(IPhosterror)>0:		
        send_mail(' + '.join(IPhosterror),again_num)
    print ('------------ **** ------------')
    print ('------------ end ------------')
    print ('------------ **** ------------')
		
def send_mail(errorip,num):
    HOST = "smtp.exmail.qq.com"
    SUBJECT = u"服务器告警（自动化运维工具）"
    TO = [ "yuanfeiyu@jlkj.cc", "240090839@qq.com" ]
	#lilei@jlkj.cc
    FROM = "yuanfeiyu@jlkj.cc"

    line1 = errorip
    #邮件正文第一行内容
    line2 = "出现异常"+str(num)+"次，"
    #邮件正文第二行内容
    line3 = "请及时处理"
    #邮件正文第三方内容

    msg = MIMEMultipart('related')
    msgtext = MIMEText("<font color=red>服务器告警:<br>IP：%s<br> &nbsp;&nbsp;&nbsp; %s<br> &nbsp;&nbsp;&nbsp %s<br>详细内容见附件。</font>" %(line1, line2 ,line3), "html", "utf-8")
    msg.attach(msgtext)

    msg['Subject'] = SUBJECT
    msg['From'] = FROM
    msg['To'] = ",".join(TO)
    try:
        server = smtplib.SMTP()
        server.connect(HOST)
        server.starttls()
        server.login("yuanfeiyu@jlkj.cc", "123qweASD")
        server.sendmail(FROM, TO, msg.as_string())
        server.quit()
        print ("邮件发送成功！")
    except Exception as e:
        print ("失败：" + str(e))

def main(inc = 15):	
    while True: 
        ip_ping()
        time.sleep(inc) 
'''
# 被周期性调度触发的函数
def execute_command(cmd, inc):
    ip_ping()
    schedule.enter(inc, 0, execute_command, (cmd, inc))


def main(cmd, inc=60):
    # enter四个参数分别为：间隔事件、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，
    # 给该触发函数的参数（tuple形式）
    schedule.enter(0, 0, execute_command, (cmd, inc))
    schedule.run()

'''
# 每60秒查看下网络连接情况
if __name__ == '__main__':
    main()
