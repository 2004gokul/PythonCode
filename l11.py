def h(a,c):
    return c(a)
def g(a,c):
    return c(a)
w=h(5,lambda a:a*2)
g=g(w,lambda a:a+3)
print(g)
