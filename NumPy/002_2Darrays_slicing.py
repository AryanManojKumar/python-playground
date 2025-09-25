import numpy as np

arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])





print(arr.ndim)
print(arr.shape)

slicing = arr[1:4]
print(slicing)


print(arr[::2]) #this is a how big the slicing will take steps for every 2 elements will be printed

print(arr[1:3])

print(arr[::-1]) #this will print the array in reverse 


print(arr[3,2:4])




a = len(arr-1)-2

print(arr[a])


print(arr[:a+1]) 

print(arr[:len(arr-1)-1:])


arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])



print(arr[1:3,2:])

print(arr[:,1:])

print(arr[:,2])

