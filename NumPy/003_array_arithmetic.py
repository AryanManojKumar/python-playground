import numpy as np

#scalar arithmetic

arr1 = np.array([1,2,3,4])

print(arr1 +1)
print(arr1 -1)
print(arr1 *5)
print(arr1 /5)
print(arr1 **5)
print(arr1 - arr1 +1)


#vector arithmetic 


arr2 = np.array([18,8,25,10])



print(np.round(np.sqrt(arr2)))

areaofcircle = np.pi * arr2**2
print(np.round(areaofcircle))





print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)

arr3 = np.array([2])
result = arr2 * arr3
    

print(result)



#conditional

scores = np.array([10,20,30,4,100])

print(scores ==  100)

scores[scores < 40] = 10
print(scores)


