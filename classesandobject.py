class car:
    def __init__(self,a):
        self.a = a
       
   

    def pow(self,other):
        print(self.a**other.a)

    def add(self,other):
        print(self.a+other.a)
    
      





bmw = car(3)
hyundai = car(5)

bmw.add(hyundai)
bmw.pow(bmw)