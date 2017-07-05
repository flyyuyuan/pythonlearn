import numpy as np
height = [1.72,1.68,1.71,1.89,1.79]
weight = [65.4,59.2,63.6,88.4,68.7]



np_height = np.array(height)
np_weight = np.array(weight)

#print("height:",height)
#print("weight:",weight)
#print("np_height:",np_height)
#print("np_weight:",np_weight)

h2 = [x * x for x in height]

i=0
bmi=[]
while (i<len(h2)):
    if(i==len(h2)):
        break
    bmi.append(weight[i]/h2[i])
    i=i+1
#print(bmi)

bmi = np_weight/np_height**2
print(bmi)
#[ 22.10654408  20.97505669  21.75028214  24.7473475   21.44127836]

#numpy只允许有一种数据类型，若内部不同，全部转为string
np1 = np.array([1.0,2.0,'is',True])
print(np1)

#区别和list的相加
print("list相加:",weight+height)

print("numpy_list相加:",np_weight+np_height)

#选取子集
print('bmi[1]:',bmi[1])
print('bmi[bmi>22]',bmi[bmi>22])

#查看类型
print('type(np_height):',type(np_height))
