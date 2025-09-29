import pandas as pd
import numpy as np

info = {
    "name":["apdillion","diljit_doshaj"],
    "ocupation":["singer","performer"],
    "net-worth":[42000,6000],
}

df =pd.DataFrame(info)

print(df)


sales = np.array([[[1,2,3,4],[1,2,3,4]],
                  [[6,7,8,9],[10,11,12,13]]])

print(np.shape(sales))



block1 = pd.DataFrame(sales[0],columns=["a","b","c","d"])
print(block1)

block2 = pd.DataFrame(sales[1],columns=["d",'e',"f","g"])
print(block2)

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.concatenate((block1,block2)))



arr  = np.array([1,2,3,4,5,6])
print(pd.DataFrame(arr,columns=["Num"]))
print(pd.Series(arr))


days = {
    "monday":["workout","eat","study"],
    "tuesday":["workout","eat","study"],
    "wednesday":["workout","eat","study"],
    "thursday":["workout","eat","study"],
}

f = pd.DataFrame(days)
print(f)