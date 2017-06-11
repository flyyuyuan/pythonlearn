#auther by yfy
#_*_coding:utf-8_*_
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
#####上面这个导入是为了解决传入utf8类型的内容时造成UnicodeDecodeError: ‘ascii’ codec can’t decode byte 0xe5 in position 108: ordinal not in range(128)这个错误，详情见这个文章http://blog.csdn.net/mindmb/article/details/7898528
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

HOST = "smtp.exmail.qq.com"
SUBJECT = u"zabbix每日报表"
TO = [ "yuanfeiyu@jlkj.cc", "240090839@qq.com" ]
FROM = "yuanfeiyu@jlkj.cc"

line1 = "这是第一行"
#邮件正文第一行内容
line2 = "这是第二行"
#邮件正文第二行内容
line3 = "这是第三行"
#邮件正文第三方内容

msg = MIMEMultipart('related')
msgtext = MIMEText("<font color=red>zabbix每日报表:<br>第一行：%s<br>第二行：%s<br>第三行：%s<br>详细内容见附件。</font>" %(line1, line2 ,line3), "html", "utf-8")
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