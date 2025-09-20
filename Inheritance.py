class vechile:
    def __init__(self,brand,topspeed):
        self.brand = brand
        self.topspeed = topspeed

    def showinfo(self):
        print("is from ",self.brand,"has a top speed of ",self.topspeed,"kmph")

    
class car(vechile):
    def __init__(self,brand,topspeed,seats):
        super().__init__(brand,topspeed)
        self.seats = seats
    
    def seating(self):
        print("this car has around",self.seats,"seats")
    
    def honk(self):
        print(self.brand,"goes beep beep")
        

class bike(vechile):
    def __init__(self, brand, topspeed,type):
        super().__init__(brand, topspeed)
        self.brand = brand
        self.topspeed = topspeed
        self.type = type
    
    def whattype(self):
        print("this bike from",self.brand,"is a",self.type,"type")

    def rev(self):
        print(self.brand,"goes vrom vrom")


pajero = car("mitshubishi",250,4)
roadster = bike("yezdi",topspeed=300,type="cruiser")

pajero.showinfo() 
pajero.seating()
pajero.honk()

roadster.showinfo()
roadster.whattype()
roadster.rev()
        




       