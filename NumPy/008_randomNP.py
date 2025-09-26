import numpy as np

Rgenerator = np.random.default_rng()

print(Rgenerator.integers(1,7))

print(Rgenerator.integers(low=1,high=100,size=2))

print(Rgenerator.integers(1,101,(2,4)))


seedgenrator = np.random.default_rng(seed=452)
#seed are used to reproduce the same randomness so will get the same result with a specific seed

print(seedgenrator.integers(1,50))
print(seedgenrator.integers(1,50,2))


print(Rgenerator.uniform(-1,1)) #you can generate float using uniform

arr = np.array([1,2,3,4,5])

Rgenerator.shuffle(arr)
print(arr)


fruits = np.array(["apple","bananan","pineapple"])
choice = Rgenerator.choice(fruits)
fruits = Rgenerator.choice(fruits,size=(2,2))
print(choice)
print(fruits)