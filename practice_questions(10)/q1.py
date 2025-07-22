a=[2,4,5,2,6]
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
    
l=[]
for i in b:
    l.append(i)
print(l)
