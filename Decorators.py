


def decorator(func):
    def wrapper():
        print("Before the function logic")
        func()
        print("After the function logic")
    return wrapper


@decorator
def helloows():
    print("hello")


helloows()



def logger(func):
  
    def wrapper(a):
        print("Before the function is called")
        func(a)
        print("after the function is called")
    return wrapper
    

@logger
def grettingPresident(name):
    print("Hello mr president",name)

@logger
def grettingmadampresident(name):
    print("hello madam president",name)


grettingPresident("karan_aujila")
grettingmadampresident("Ap dillion")






def anynumberofarg(func):
    def manyarg(*args,**kwargs):
        print("before the function is called")
        func(*args,**kwargs)
        print("after the function is being called")
    return manyarg

@anynumberofarg
def sayinghellotoeveryon(a):
    
        for x in a:
            print("hello mr president",x)
 

sayinghellotoeveryon(a=["karan aujila","ap dillion","talwinder","frank-ocean"])








# def decoratorfunc(func):
#      print("Before the function runs")
#      func()
#      print("after the function runs")
    




# def hello():
#    print("Hellow")


# decoratorfunc(hello)
