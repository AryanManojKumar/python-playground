
def factorial(a):
    if a == 0:
        return 1 
    if a == 1:
        return 1
    
    return a*factorial(a-1)



def primenmber(a):
    x=2
    while x<a-1:
        if a%x==0:
            return "not prime"
        x+=1
        
    return "prime"

