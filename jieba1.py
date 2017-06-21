# -*- coding: utf-8 -*-
import jieba
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import os
import PIL.Image as Image
import numpy as np

# 读取文本内容
with open('bigdata4.txt','rb') as f:
    text = f.read()
    f.close()
jieba.load_userdict("cu.txt")

#首先使用 jieba 中文分词工具进行分词
wordlist = jieba.cut(text, cut_all=False)      
# cut_all, True为全模式，False为精确模式

wordlist_space_split = ' '.join(wordlist)
d = os.path.dirname(__file__)
alice_coloring = np.array(Image.open(os.path.join(d,'timg.png')))
font = 'C:/Users/Windows/fonts/STKAITI.TTF'
my_wordcloud = WordCloud(font_path=font, 
                         background_color='white',         # 设置背景颜色
                         max_words=250,                      # 设置最大显示的字数
                         mask=alice_coloring,                # 设置背景图片
                         max_font_size=150,                  # 设置字体最大值
                         random_state=42                     # 设置有多少种随机生成状态，即有多少种配色方案
                         ).generate(wordlist_space_split)

image_colors = ImageColorGenerator(alice_coloring)

plt.show(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)            # 以图片的形式显示词云
plt.axis('off')                     # 关闭坐标轴
plt.show()

my_wordcloud.to_file(os.path.join(d, 'ydyl_gb_colors_cloud.png'))