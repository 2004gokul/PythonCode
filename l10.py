def fun(a,b,x):
    return x(a,b)
def switch(a):
    match a:
        case 1:
           
            return fun(2,4,lambda a,b:a+b)
        case 2:
           
            return fun(2,4,lambda a,b:a-b)
        case 3:
           
            return fun(2,4,lambda a,b:a*b)
        case 4:
           
            return fun(2,4,lambda a,b:a/b)
print(switch(3))
