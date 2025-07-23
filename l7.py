class a:
    def __init__(self):
        self.A=800
class b:
    def __init__(self):
        self.B=900
class c(a,b):
    def __init__(self):
        a.__init__(self)
        b.__init__(self)
    def show(self):
        self.c=self.A+self.B
        print(self.c)
obj=c()
obj.show()
print(c.mro())
        
    
