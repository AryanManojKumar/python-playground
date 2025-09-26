

try:
    print(x)
except:
    print("An exception occured")


x = 10 
try:
    a = int(input("enter a number"))
    b = x/a
except ValueError:
    print("this is not a valid character")
except ZeroDivisionError:
    print("can not divide by zero")
else: 
    print(int(b))




try:
    a = int(input("enter a number"))
    b = x/a
    
except Exception as e:
    print("Error type:", type(e))

else:
    print(int(b))

finally:
    print("the div was a sucess")



try:
    f =  open("test.txt")
    try:
        f.write("this is a test file used to learn filehandling in python")
    except Exception as err:
        print("something went wrong ",err)
    finally:
        f.close()
except Exception as err:
    print(err)


def agelimit(x):
    if x < 18:
        raise ValueError("Underage")

try:
    a = int(input("Enter your age: "))
    agelimit(a)
except ValueError as e:
    print("Sorry you cannot drive:", e)



def dividing(a,b):
    if  b == 0:
        raise ZeroDivisionError("dividing by zero is illegal")
    
    elif b<0:
        raise ValueError("can not divide with negative")
    
    return a/b



try:
    a = 10
    b = -10
    print(dividing(a,b))
except Exception as e:
    print("THE DIVISION WAS NOT A SUCCESS DUE TO",e)
