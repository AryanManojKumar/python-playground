
x = 5
y = x 
print(y)

#this is a comment \

f = 5
f ="five"
print(f)

z = float(3)
print(z)

j = str('hi')
print(j , type(j))

a=b=c ="yellow"
print(a+b)
print(b)
print(c)

city = ["tokyo","singapore","beiging"]
japan,sg,china  = city
print(china,japan)
print(china+sg)

one = 1
five = "one"
print(one,five)

f ="this is a global variable"
def firstfunction():
    print(f)

firstfunction()

h = "nice"

def secondfunction():
    h ="good enough"
    global j
    j="meh"
    print("pythong is "+h)

secondfunction()

print("python is "+h)
print("python is ",j)



