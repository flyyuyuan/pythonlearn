import numpy as np

lst=[[1,3,5],[2,4,6]]

print(type(lst))

np_lst = np.array(lst)

print(type(np_lst))
print(np_lst)

np_lst = np.array(lst,dtype=np.float)
print(np_lst)

print(np_lst.shape)
print('维度：'+str(np_lst.ndim))
print('数据类型：'+str(np_lst.dtype))
print('每个字节大小：'+str(np_lst.itemsize))
print('多少个元素：'+str(np_lst.size))
print('随机数randint[1-5之间],一共3个：'+str(np.random.randint(1,5,3)))
print('随机数rand：'+str(np.random.rand(2,4)))
print('形成2行4列的正态分布RandN：'+str(np.random.randn(2,4)))
print('在10，20,30随机choice：'+str(np.random.choice([10,20,30])))
print('在10，20,30随机choice：'+str(np.random.choice([10,20,30])))

print('生成20个1-10的beta分布数据：'+str(np.random.beta(1,10,20)))

print('等差数列arange(1,11)：'+str(np.arange(1,11)))
print('等差数列arange(1,11),搞成2行5列：'+str(np.arange(1,11).reshape(2,5)))

lst = np.arange(1,11).reshape(2,5)
print('指数函数 exp:',np.exp(lst))
print('指数函数 exp2:',np.exp2(lst))
