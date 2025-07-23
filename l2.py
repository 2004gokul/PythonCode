s= [("Laptop", 1000), ("Mouse", 50), ("Keyboard", 300), ("Monitor", 700)]
d=filter(lambda x:x[1]>500,s)
print(list(d))
