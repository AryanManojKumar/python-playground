


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







def decoratorwitharg(a):
    def decorator(func):
        def wrwapper(*args,**kwargs):
            if a == 1:
                print("this is the before logic if the decorators arg is one ",a)
                n = func(*args,**kwargs)
                print("this is the after logic for ",a)

            elif a==2:
                print("this is the before logic if the second decorator is used",a)
                n = func(*args,**kwargs)
                print("this is the after logic for ",a)
            return n  

        return wrwapper
    return decorator
    

@decoratorwitharg(1)
def englishsinger(a):
    for x in a:
        print(x,"is one of the best international singer")


@decoratorwitharg(2)
def indiansinger(a):
    for x in a:
        print(x,"is one of the best indian singer")


englishsinger(a=["travis scot","frank-ocean","rare-ocasion","playboy-carti"])
indiansinger(["KaranAujila","diljit","sidhumoosewala","Gurindergill"])

    









# def decoratorfunc(func):
#      print("Before the function runs")
#      func()
#      print("after the function runs")
    




# def hello():
#    print("Hellow")


# decoratorfunc(hello)
