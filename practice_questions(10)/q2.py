def even(a):
    b=[]
    for i in a:
        if i%2==0:
            b.append(i)
    c=sorted(b,reverse=True)
    return c
            


print(even([5,6,3,9,2,8,4,2]))
