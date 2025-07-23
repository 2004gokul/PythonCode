from functools import reduce
lp=[1,3,5,5,4,5]
p=reduce(lambda x,y:x*y,lp)
print(p)
