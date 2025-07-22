lp=[3,45,67,8,3,67,8]
ll={}
for i in lp:
    if i in ll:
        ll[i]+=1
    else:
        ll[i]=1
print(ll)
