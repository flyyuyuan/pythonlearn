import pandas as pd

brics = pd.read_csv("brics.csv",index_col=0)

#print(brics)

#打印列
#print(brics["country"])
#print(brics.country)
#添加列
brics['on_earth'] = [True,True,True,True,True]
brics['density'] = brics.population / brics.area * 1000000

#获取行
#print(brics.loc['BR'])

#获取元素
print(brics.loc['CH','catital'])
print(brics.loc['CH']['catital'])
print(brics.catital.CH)
print(brics["catital"]["CH"])
#print(brics)
