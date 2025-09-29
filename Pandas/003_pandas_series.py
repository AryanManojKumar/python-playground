import pandas as pd
import numpy as np

a = [1,2,3,4]

b = pd.Series(a)
print(b)

print(b[0])
 

days = {
    "monday":"study",
    "tuesday":"study",
    "wednesday":"study",
    "thursday":"study",
}


print(pd.Series(days))

arr = np.array([["a","b","c"],["d","e","f"],["g",'h',"i"],["j","k","l"]])

table = pd.DataFrame(arr,columns=["one","two","three"])
print(table)