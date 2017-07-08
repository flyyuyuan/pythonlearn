import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.dates as mdate

year = [1950,1970,1990,2010]
population = [2.519,3.692,5.263,6.972]

year = [1800,1850,1900]+year
population = [1.0,1.262,1.650]+population

fig1 = plt.figure(figsize=(8, 5), dpi=80)
ax1 = fig1.add_subplot(1,1,1)
#ax1.xaxis.set_major_formatter(mdate.DateFormatter('%Y'))#设置时间标签显示格式
plt.xticks(year)
#plt.fill_between(year,population,0,color='green')
#线图
plt.plot(year,population,color='blue', linewidth=2.5, linestyle="-")
#散点图
#plt.scatter(year,pop)

zhfont = FontProperties(fname=r'c:\windows\fonts\simsun.ttc',size=14)
plt.xlabel('year')
plt.ylabel('population')

plt.title('世界人口爆炸',fontproperties=zhfont)

plt.yticks([0,2,4,6,8,10],
           ['0','2B','4B','6B','8B','10B'])#y轴的刻度和对应的单位


#plt.xlim(1800 * 1.1, 2015)
#plt.ylim(C.min() * 1.1, C.max() * 1.1)

plt.show()
