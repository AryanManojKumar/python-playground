import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

newarr =  arr.reshape(2,4)

print(newarr)

newarr = arr.reshape(2,4)
print(newarr)

arr = np.array([1,2,3,4,5,6,7,8,9,10])

newarr = arr.reshape(10,1)
print(newarr)


newarr = arr.reshape(2,1,5)
print(newarr)


array3d = np.array([[[1,2,3],[3,4,5]],
                    [[6,7,8],[8,9,10]]])
print(array3d.shape)


newarr = array3d.reshape(1,12)
print(newarr)