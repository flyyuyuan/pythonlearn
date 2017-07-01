class UrlManager(object):

    def __init__(slef):
        self.new_urls = set()
        self.old_urls = set()

        
    #向管理器添加新的url
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    #批量添加新的url
    def add_new_urls(self,urls):
        if urls is none or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
    
    #判断管理器中是否有待爬取的url
    def has_new_url(self):
        return len(self.new_urls)!=0
        
    #从管理器获得一个新的url
    def get_new_url(self):
        new_url= self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url


    
