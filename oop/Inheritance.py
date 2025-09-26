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
        




class emoplyee :
    def __init__(self,name,yearofjoining,salary):
        self.name = name
        self.yearofjoining = yearofjoining
        self.salary = salary

    def work(self):
        print(self.name,"is working")

    def employeeinfo(self):
        print(self.name,"salary is ",self.salary,"and has been working from",self.yearofjoining,"years")

class manager(emoplyee):
    def __init__(self, name, yearofjoining, salary):
        super().__init__(name, yearofjoining, salary)   
    
    def work(self):
        print(self.name,"is managing the team")

    def holdmeating(self):
        print("holding meeting")
    

class developer(emoplyee):
    def __init__(self, name, yearofjoining, salary):
        super().__init__(name, yearofjoining, salary)

    def work(self):
        print(self.name,"is writing the code")

    def debug(self):
        print(self.name,"is debuging the code")

    
class intern(emoplyee):
    def __init__(self, name, yearofjoining, salary):
        super().__init__(name, yearofjoining, salary)

    def work(self):
        print(self.name,"is learning")

    def askingquestion(self):
        print(self.name,"is asking quesiton")
       


for x in (manager("apdillion",12,"18lpa"),developer("aryan",13,"40lpa"),intern("karan_aujila",0.5,"3lpa")):
    x.employeeinfo()
    x.work()