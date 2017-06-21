from functools import reduce
class Fib(object):
    #fb=[0, 1, 1, 2, 3, 5, 8,13,21,34,55]
    #fb =[]
    def __init__(self):
        pass
    def __str__(self):
        return str(self.lt)
    def __len__(self):
        return len(self.lt)
    
    def __call__(self,num):
        if num<=0:
            fb=[]
        elif num == 1:
            fb = [0]
        elif num == 2:
            fb = [0,1] 
        else:
            fb =[0,1]
            for i in range(0,num):
                fb.append(reduce(lambda x,y: x+y,(fb[i:i+2])))
        return str(fb[0:-2])

f = Fib()
print (f(10))