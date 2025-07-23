class vehicle:
    def __init__(self):
        self.type="vehicle"
    def move(self):
        print(self.type)
class car(vehicle):
    def __init__(self):
        super().__init__()
        self.type="car"
    def move(self):
        print(self.type)
class bike(vehicle):
    def __init__(self):
        super().__init__()
        self.type="bike"
    def move(self):
        print(self.type)
a=vehicle()
b=car()
c=bike()
a.move()
b.move()
c.move()

        
