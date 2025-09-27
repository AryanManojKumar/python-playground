
from abc import ABC,abstractmethod


class payment(ABC):
  
    @abstractmethod
    def pay(self):
        return
    
class cardpayment(payment):
  
    def pay(self):
        return"Paying",self.ammount,"through card"
    

class cashpayment(payment):
 
    def pay(self):
        return"paying",self.ammount,"through cash"
   

guru = cardpayment(100)

print(guru.pay())





class car(ABC):
    def __init__(self,model):
        self.model = model

    @abstractmethod
    def price(self):
        pass
    


class koenigsegg(car):
    def __init__(self, model):
        super().__init__(model)

    def price(self):
        return "a million dollar"


class Bayerische(car):
    def __init__(self, model):
        super().__init__(model)

    def price(self):
        return "100k"
    

buy = Bayerische("m3 comp")

print("the price for an ",buy.model,"is",buy.price)