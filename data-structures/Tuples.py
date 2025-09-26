
#immutable 

guns = ("vandal","oding","op")

print(guns)

oneiteam = ("single",)

print(guns[0],guns[:2])

# guns[0]="phantom" this will show error

operator = tuple(f for  f in  guns if f == "op")
print(operator)

person = ("aryan",21,"SDE1")
name,age,job = person
print(name,age,job)

cordinates = (10.5,5.4)

location={
    "home" : cordinates
}

print(location)