# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
import codecs
import json
import pymysql

class TutorialPipeline(object):
    def __init__(self):
        self.file = codecs.open('items.json', 'w', encoding='utf-8')
        
        self.conn = pymysql.connect(host="localhost",user="root",password="root",db="wikiurl")
        self.conn.set_charset("utf8")
        
    def process_item(self, item, spider):
        #下面代码插入数据库
        title = item["title"]
        link = item["link"]
        content = item["content"]

        sql = "insert into scrapytest(title,link,content) values ('" + title + "','" + link + "','" + content + "');"
        
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        #下面插入json
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"#不使用默认的ascii编码
        self.file.write(line)
        #return item

    def spider_closed(self, spider):
        self.file.close()
        self.conn.close()