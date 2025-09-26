day = 5

match day:
    case 1 :
        print("Monday")
    case 2 :
        print("tuesday")
    case 3 :
        print("wednesday")
    case _:
        print("the day is after wednesday")


location=[0,4]
locationinflaot=[]



for x in range (len(location)):
    if isinstance(location[x],int) :
        locationinflaot.append(float(location[x]))
    elif isinstance(location[x],float):
        locationinflaot.append(location[x])
    else :
        print("plz be from earth")
  
print(locationinflaot)

match locationinflaot:
    case [float(x),0]:
        print("the location is in Longitude",x,"and latitude 0")
    case[0,float(y)]:
        print("The location is in longitude 0 and latitude",y)
    case[float(x),float(y)]:
        print("The location is in longitude",x,"and latitude",y)
    case _:
        print("Bro is not in earth")


