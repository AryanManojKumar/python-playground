def func():
    x=10
    print(x)

# print(x)#wont work

def func():
    x=0
    def func1():
        print(x)
    func1()

func()


x = 10

def abc():
    print(x)
    def abcd():
        print(x)
    abcd()

abc()    

def cba():
    x =20
    print(x)

print(x)
cba()

def usingglobal():
    global x 
    x = 20

usingglobal()
print(x)

