import configparser
import url_manager
import html_downloader
import html_parser
import html_outputer
import img_downloader
import pymysql.cursors

class SpiderMain(object):

    def __init__(self,config):
        self.config = config;
        #获取数据库连接字符串
        connection = pymysql.connect(host=config.get('db', 'host'),
                                     user=config.get('db', 'user'),
                                     password=config.get('db', 'password'),
                                     db = config.get('db', 'db'),
                                     charset=config.get('db', 'charset'))
        
        self.urls = url_manager.UrlManager(connection,config.get('db', 'isuse'))
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParse()
        self.outputer = html_outputer.HtmlOutputer()
        self.imgdownloader = img_downloader.ImgDownloader()

        
    def craw(self,root_url,max_num):
        #记录当前爬取的url
        count = 1
        
        self.urls.add_new_url(root_url)

        #若有待爬取的url
        while self.urls.has_new_url():  

            #获取需要爬取的url
            try:
                new_url = self.urls.get_new_url()
                print('craw %d:%s'%(count,new_url))

                #下载页面数据
                html_cont = self.downloader.download(new_url)

                #解析页面，获得数据和新的相关url
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                #print(new_data['pic_url'])
                self.imgdownloader.getImg(new_data)
                #将新的相关urls补充至url管理器；并进行数据的收集
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                

                #默认爬取url限制
                if count == int(max_num):
                    break;

                count = count+1
            except:
                print ('craw failed...')
                connection.close()
                
        #输出爬取的所有数据
        self.outputer.output_html()

if __name__ == "__main__":
    
    config=configparser.ConfigParser()
    config.read("spiderconfig.conf")
    
    root_url = config.get('root_url', 'url')
    max_num = config.get('root_url', 'maxnum') 
    #print ('host of ssh:', max_num)

    
    obj_spider = SpiderMain(config)
    obj_spider.craw(root_url,max_num)
    
    #print ('all sections:', config.sections())        # sections: ['db', 'ssh']
    #print ('options of [db]:', config.options('db'))  # options of [db]: ['host', 'port', 'user', 'pass']
    #print ('items of [ssh]:', config.items('ssh'))    # items of [ssh]: [('host', '192.168.1.101'), ('user', 'huey'), ('pass', 'huey')]
    #print ('host of db:', config.get('db', 'host'))    # host of db: 127.0.0.1
    #print ('host of ssh:', config.get('ssh', 'host'))   # host of ssh: 192.168.1.101


            
