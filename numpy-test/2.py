import numpy as np

np_2d = np.array([[1.72,1.68,1.71,1.89,1.79],[65.4,59.2,63.6,88.4,68.7]])

print(np_2d)
print(np_2d.shape)

print("np_2d[0,2]:",np_2d[0,2])
print("np_2d[0][2]:",np_2d[0][2])

print("np_2d[:,1:3]:",np_2d[:,1:3])
print("np_2d[1,:]:",np_2d[1,:])

bmi = np_2d[1,:]/np_2d[0,:]**2
print("bmi:",bmi)

#city = [[1,2],[2,4],[4,8],[8,16],[16,32],[32,64],[64,128],[128,256],[256,512],[512,1024],[1024,2048]]
#np_city = np.array(city)

height = np.round(np.random.normal(1.75,0.20,15),2)
weight = np.round(np.random.normal(60.32,15,15),2)
np_city = np.column_stack((height,weight))

print("数据生成:",np_city)

print("平均值：",np.mean(np_city[:,1]))
print("中位数：",np.median(np_city[:,1]))
print("相关性：",np.corrcoef(np_city[:,0],np_city[:,1]))
print("标准差：",np.std(np_city[:,0]))


print("标准差：",np.std(np_city[:,0]))


np_height = np.array(height)
np_weight = np.array(weight)


