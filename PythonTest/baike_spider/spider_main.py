import url_manager
import html_downloader
import html_parser
import html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParse()
        self.outputer = html_outputer.HtmlOutputer()

        
    def craw(self,root_url):
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

                #将新的相关urls补充至url管理器；并进行数据的收集
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                #默认爬取url限制
                if count ==1000:
                    break;

                count = count+1
            except:
                print ('craw failed...')
        #输出爬取的所有数据
        self.outputer.output_html()

if __name__ == "__main__":
    root_url = 'http://baike.baidu.com/item/Python'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)


            
