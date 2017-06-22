import pymysql.cursors
#获取数据库连接字符串
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='root',
                             db = 'wikiurl',
                             charset='utf8mb4')
try:
    #获取会话指针cursor
    with connection.cursor() as cursor:
        #创建sql语句
        sql="insert into urls (urlname,urlhref) values(%s,%s)"
        #执行sql语句
        cursor.execute(sql,("baidu","www.baidu.com"))
        #提交
        connection.commit()
        
finally:
    connection.close()
