#ordered means they can be indexed 

a =[1,2,3]
print(a)

b=[1,"b",4.20]
print(b)

print(b[1])

c=[1,2,3,4,5,6]
print(c[::5])

c.append(100) #add at end
print(c[6])

c.insert(4,50)
print(c[4])

c.remove(50)
print(c)

e = [1,2,3]
f = [4,5,6]

print(e+f)
print(e*2)
if 3 in e:
    g = True
else :
    g = False

print(g)


guns = ["ak","m16","awp","aug"]

for russia in guns:
    print(russia)

for i in range(len(guns)):
    print(i,guns[i])

for i, usa in enumerate(guns):
    print(usa)


nums = [1,2,3,4,5,6,7,8,9]
even=[]

print(nums)
for x in nums:
    if x%2==0:
        even.append(x)

print(even)

odd =[k for k in nums if k%2!=0]
print(odd)


isdivideableby4 = [f for f in nums if f%4==0 ]
print(isdivideableby4)

uppercase =[f.upper() for f in guns]
print(uppercase)

nums2 =[9,8,7,6,5,4,3,2,1]
print(nums2)

nums2.sort()
print(nums2)
nums.sort(reverse=True)
print(nums)

guns.reverse()
print(guns)

csgo_guns = [guns.copy()]
print(csgo_guns)

z =[1,2,2,3,4]
print(z)

q =[5,6,7,8]

l = z+q
print(l)