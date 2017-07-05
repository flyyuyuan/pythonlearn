import pymysql.cursors

class UrlManager(object):
       
    def __init__(self,connection,isuse):
        self.new_urls = set()
        self.old_urls = set()
        self.connection = connection
        self.usesql = isuse
        
    #向管理器添加新的url
    def add_new_url(self,url):      
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            if self.usesql=="0":
                self.new_urls.add(url)

            else:
                try:
                    #获取会话指针cursor
                    with self.connection.cursor() as cursor:
                        #创建sql语句
                        sql="insert into new_urls (url) values(%s)"
                        #执行sql语句
                        cursor.execute(sql,(url))
                        #提交
                        self.connection.commit()
        
                finally:
                    #self.connection.close()
                    #print(self.connection)
                    pass
                
    #批量添加新的url
    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
    
    #判断管理器中是否有待爬取的url
    def has_new_url(self):
        if self.usesql=="0":
            return len(self.new_urls)!=0
        else:
            with self.connection.cursor() as cursor:
                sql_select=" SELECT count(1) from new_urls;"
                result = cursor.execute(sql_select)
                return result
        
    #从管理器获得一个新的url
    def get_new_url(self):
        
        if self.usesql=="0":
            new_url= self.new_urls.pop()
            self.old_urls.add(new_url)
            return new_url

        else:
            try:
                #获取会话指针cursor
                with self.connection.cursor() as cursor:
                    #创建sql语句
                    sql_select=" select url from new_urls ORDER BY id limit 1;"
                    sql_delete=" delete from new_urls where url =%s;"
                    sql_add = " insert into old_urls (url) values(%s);"
                    #执行sql语句
                    cursor.execute(sql_select)
                    result = cursor.fetchone()
                    #print(result[0])
                    cursor.execute(sql_delete,(result[0]))
                    cursor.execute(sql_add,(result[0]))
                    #提交
                    #self.connection.commit()
        
            finally:
                #self.connection.close()
                #print(self.connection)
                pass
        
            return result[0]

    
