
a = [1,2,3,4,5]

it = iter(a)


# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         break


for x in (range(len(a))):
    print(next(it))

c = "hello"
a = iter(c)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))



class iterable:
    def __init__(self,starting,end):
        self.starting = starting
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.starting>self.end:
            raise StopIteration
        else:
            x = self.starting
            self.starting+=1
            return x
        
    
        



f = iterable(1,20)

for n in f:
    print(n)



class gettinglen:
    def __init__(self,*a):
        self.arr = a
        self.starting =a[0]
        self.end = len(a)

 
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.starting>self.end:
            raise StopIteration
        else:
            x = self.starting
            self.starting+=1
            return x 
        
    def length(self):
        len = 0
        for x in self.arr:
            len+=1
            
        return len
    
    def printing(self):
        for x in self.arr:
            print(x)
        
        
        


g = gettinglen(1,2,3,4,5,6,7)

print(g.length())

g.printing()
        
