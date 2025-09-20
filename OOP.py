
class guns:
    def __init__(self,name,damage):
        self.name = name
        self.damage = damage
        pass

    def showinfo(self):
        name = self.name
        damagae = self.damage
        print("the name of the gun is ",name)
        print("the gun can take ",damagae,"this much damage")

    def __add__(self,other):
        a = self.damage
        b = other
        return a +b 




vandal = guns(name="Vandal",damage=104)
phantom = guns("phantom",100)
odin = guns("odin",200)

vandal.showinfo()
phantom.showinfo()

def accumulateddamage(*guns):
    f =  0
    for a in guns :
        f = f + a.damage
    return f






print("accumulated damage =",accumulateddamage(vandal,phantom,odin))

