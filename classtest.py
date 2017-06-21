import functools
class Person(object):
    pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

sorted_ignore_case = functools.partial(sorted,key=Person().name)

L1 = [p1, p2, p3]
L2 = sorted_ignore_case(L1)
print(L2)
#print (L2[0].name)
#print (L2[1].name)
#print (L2[2].name)