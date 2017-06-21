def foo():  
    a = 1  
    def bar():  
        nonlocal a
        a = a + 1  
        return a  
    return bar
c = foo()
print (c())