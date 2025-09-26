import numpy as np

arr = np.array([[1,2,3,4,5],
                [6,7,8,9,10]])


total = np.sum(arr)
print(total)

print(np.mean(arr))
print(np.std(arr))
print(np.min(arr))
print(np.argmin(arr))
print(np.max(arr))

arr = np.array([[1,2,3,4,5],
                [6,7,8,9,10]])


print(np.sum(arr[1]))

print(np.sum(arr,axis = 0)) #sums all the colums

print(np.sum(arr,axis = 1 )) #sum of all row

print(np.sum(arr[1])) #get sum of a specific row








