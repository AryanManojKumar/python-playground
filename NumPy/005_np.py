import numpy as np

arr = np.array([1,2,3,4,5,6,7])#7,6,5,4,3,2,1
k=2


arr = arr[::-1]
temp = arr[k:]
arr =arr[:k]
arr = arr[::-1]
temp = temp[::-1]

rotateright=np.concatenate((arr,temp))


print(rotateright)