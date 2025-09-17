a = "Hello"
b = " its 'me'"

print(a+b)

c = """baby i lose my mind
no one noticed no one noticed 
come on dont leave it cant be that easy mate"""


print(c)

d = "and she cried over nothing"

# n = len(d)

# for i in range(len(d)):
#     print(d[i])

print("")
for x in "Tv girl":
    print(x)


j = """and there was nothing  i can do
to stop her from cutting
her beatiful blue hair off"""

print("blue" in j)#results in bool

f = "mrbeast"

if f in j:
    print("Yes",f,"is in the paragraph")


if f not in j:
    print(f,"is not inside tha para")



k = "  lewish hamilton  "
print(k[0:-1])
print(k.upper())
print(k.strip())

print(k.replace("l","h"))
print(k.split())


l = "  i just"
u = "  wanna be urs   "
c = l+u
print(c.strip())

m = 505
txt =f"am going back to {float(m)} "
print(txt)


k = " hello \" darkness\" my friend "
print(k.strip())