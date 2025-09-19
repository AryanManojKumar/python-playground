a = 5

while a < 10:
    print(a)
    a=a+1

#while true gives infinite loop
f=0
while True:
    print(f)
    f+=1
    
    if f == 4:
        break

g = 0

while g<10:
    
    g+=1
    if g ==3:
        continue
    print(g)
else:
    print("g is now greater then 10")

    