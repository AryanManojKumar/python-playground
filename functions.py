def basicfunction():
    print("Hello")

basicfunction()

def sayinghellotopresident(name):
    print("hello mr president",name,"!")

sayinghellotopresident("Karan aujila")

def wedding(bride , groom):
    print("The marriage is between",groom,"and",bride)

wedding("Ap dillion","karan aujila")

def adding(a,b):
    return a+b

print(adding(5,5))

def howmanynumber(*a):
    j = 0
    for x in (range(len(a))):
        j+=1
    print("total number of argument passed",j)
howmanynumber(10,20,30,40)


def multi(factor,*nums):
    result=[]
    for x in nums:
        result.append(factor*x)
    return result

print(multi(5,4,3,2,1))


def arbikey(**kids):
    print("hello",kids["name"],"ur age must be ",kids["age"])

arbikey(name="talwinder",age="40")


def emptyfunc():
    pass

emptyfunc()


def factorial(a):
    if a == 0:
        return 1
    if a == 1:
        return 1
    
    return a * factorial(a-1)

print(factorial(5))