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
        sql="select urlname,urlhref from urls where 1=1"
        #执行sql语句
        count = cursor.execute(sql)
        print(count)
        
        #查询光标当前下一条条数据；再执行一次就是第二条
        result1 = cursor.fetchone()
        print(result1)
        print(result1[0])
        
        #查询前2条数据
        result1 = cursor.fetchmany(size=2)
        print(result1)
        
        #查询所有数据
        result = cursor.fetchall()
        print(result)
        
        #提交
        #connection.commit()
        
finally:
    connection.close()
