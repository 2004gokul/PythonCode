d1={'a': 10, 'b': 20}
d2 = {'b': 30, 'c': 40}
d3={}
for i,j in d1.items():
    if i not in d3:
        d3[i]=j
    else:
        d3[i]+=j
for i,j in d2.items():
    if i not in d3:
        d3[i]=j
    else:
        d3[i]+=j
print(d3)
