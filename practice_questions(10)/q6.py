a="2,4,5,6,78,7,88,9,768"
a=a.split(",")
a=list(map(int,a))
lp=[]
for i in a:
    if i>10:
        lp.append(i)
print(lp)
