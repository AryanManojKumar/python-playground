class car :
    def __init__(self,a):
        self.carname = a
        
    def move(self):
        print(self.carname," moves on land")

class boat:
    def __init__(self,a):
        self.boatname = a
    def move(self):
        print(self.boatname," moves on water")

class plane:
    def __init__(self,a):
        self.planename = a
    def move(self):
        print(self.planename," moves in air")




#this creates an object/instance for the method and loops through it )
for x in (car("verna"),boat("titanic"),plane("airbus")):
    x.move()



    
    def animal_making_sound(animal):
        print(animal.sound())


    class dog:
        def sound(self):
            return"woof"
        
    class cat:
        def sound(self):
            return"meow"
        

    a = dog()
    b = cat()

    for x in (a,b):
        animal_making_sound(x)