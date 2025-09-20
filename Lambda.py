
a = lambda a,b : a+b

print(a(5,5))

square = lambda a : a*a

print(square(5))

power = lambda a,b : a ** b 
print(power(5,5))


nums = {1,2,3,4,5}
squaring = list(map(lambda x : x**2,nums))

print(squaring)


def multiplyby(n):
    return lambda a : a*n

f = multiplyby(2)
g = multiplyby(4)

print(f(10),g(10))


#this is the normal way without lamda


def multiplybya(a):
    def multi(n):
        return n * a 
    return multi

a  = multiplybya(2)
print(a(40))




