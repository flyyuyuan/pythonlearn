# -*- coding:utf-8 -*-  
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfdevice import PDFDevice
from urllib.request import urlopen

#获取文档对象
fp = open("simple1.pdf","rb");
#fp= urlopen("http://www.tencent.com/zh-cn/articles/8003251479983154.pdf").read().decode("utf-8")

#创建一个与文档关联的解释器
parser = PDFParser(fp)

#PDF文档的对象
doc = PDFDocument()

#链接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)

#初始化文档 无密码
doc.initialize("")

#创建PDF资源管理器
resource = PDFResourceManager()

#参数分析器
laparam =  LAParams()

#创建一个聚合器
device = PDFPageAggregator(resource,laparams = laparam)

#创建页面解释器
interpreter = PDFPageInterpreter(resource,device)

#使用文档对象得到页面的聚合
for page in doc.get_pages():
    #使用页面解析器来读取
    interpreter.process_page(page)
    
    #使用聚合器获得内容
    layout = device.get_result()

    for out in layout:
        if hasattr(out,"get_text"):
            print(out.get_text())
    
