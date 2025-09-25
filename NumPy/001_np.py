import numpy as np

print(np.__version__)

arr = np.array([1,2,3,4])

print(type(arr)) 

arr = arr * 5 
print(arr)



print(arr.ndim)


arrays2d = np.array([["A","B","C"],["D","E","F"],["G","H","I"]])

print(arrays2d.ndim)

array3d = np.array([[[1,2,3],[4,5,6],[7,8,9]],
                    [[10,11,12],[13,14,15],[16,17,18]],
                    [[19,20,21],[22,23,24],[25,26,27]]])
print(arrays2d.ndim)
print(array3d.shape)


array3dalpha = np.array([[["A","B","C"],["D","E","F"],["G","H","I"]],
                    [["J","k","L"],["M","N","o"],["P","Q","R"]],
                    [["S","T","U"],["V","w","X"],["Y","Z","_"]]])


aryan = array3dalpha[0,0,0]+array3dalpha[1,2,2]+array3dalpha[2,2,0]+array3dalpha[0,0,0]+array3dalpha[1,1,1]

print(aryan)