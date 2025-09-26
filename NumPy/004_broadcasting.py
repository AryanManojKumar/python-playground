#the dimension has same size 
    #or
#one of the dimension is 1

import numpy as np


arr1 = np.array([[1,2,3,4]])

arr2 = np.array([[1],[2],[3],[4]])


#they have 1 row and 1 column so they'll broadcast

print(np.shape(arr1))
print(np.shape(arr2))

print(arr1+arr2)



arr3 = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
arr4 = np.array([[1],[2],[3],[4]])

#this is a 4x4 and 4x1 so it'll broadcast 
print(np.shape(arr3))
print(np.shape(arr4))
print(arr3*arr4)


arr5 = np.array([[1,5],[2,5],[3,5],[4,5]])
print(np.shape(arr5))

# print(arr5*arr3) this will not work cause arr5 is 1X2

print(arr5*arr4)


arr6 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

arr7 = np.array([[1,2,3,4,5,6,7,8,9,10]])

print(np.shape(arr6),np.shape(arr7))

print(arr6 * arr7)