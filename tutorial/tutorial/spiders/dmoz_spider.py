from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from tutorial.items import DmozItem

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://localhost:8008/index.html",
        "http://localhost:8008/index.aspx"
]    
  
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[contains(@class, "article-item clearfix")]')
        #sites = hxs.path('//ul/li')
        items=[]
        for site in sites:
            item = DmozItem()
            item['title'] = site.select('div[contains(@class, "article-item-title")]/a/text()').extract()[0].encode('utf-8')
            if len(site.select('div[contains(@class, "article-item-title")]/a/span/text()').extract())>0:
                item['title']+=site.select('div[contains(@class, "article-item-title")]/a/span/text()').extract()[0].encode('utf-8')
            
            item['link'] = site.select('div[contains(@class, "article-item-title")]/a/@href').extract()[0]
            item['desc'] = site.select('div[contains(@class, "content-warp")]/p/text()').extract()+site.select('div[contains(@class, "content-warp")]/p/span/text()').extract()
            #print title, link, desc
            items.append(item)
            print (item['title'], item['link'])
        return items
