from abc import abstractmethod
class shape:
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,l):
        self.l=l
        
    def area(self):
        print(3.14*self.l*self.l)
class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
        
    def area(self):
        print(2*self.l*self.b)
o1=circle(4)
o1.area()
o2=rectangle(5,6)
o2.area()

    
        
        
