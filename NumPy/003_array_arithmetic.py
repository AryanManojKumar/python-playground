import numpy as np

# #scalar arithmetic

# arr1 = np.array([1,2,3,4])

# print(arr1 +1)
# print(arr1 -1)
# print(arr1 *5)
# print(arr1 /5)
# print(arr1 **5)
# print(arr1 - arr1 +1)


# #vector arithmetic 


# arr2 = np.array([18,8,25,10])



# print(np.round(np.sqrt(arr2)))

# areaofcircle = np.pi * arr2**2
# print(np.round(areaofcircle))





# print(arr1 + arr2)
# print(arr1 - arr2)
# print(arr1 * arr2)

# arr3 = np.array([2])
# result = arr2 * arr3
    

# print(result)



# #conditional

# scores = np.array([10,20,30,4,100])

# print(scores ==  100)

# scores[scores < 40] = 10
# print(scores)





score = np.array([45, 67, 89, 100, 23, 56, 100, 72, 49, 95])

 
for x in np.where(score == 100):
    print(x)

a = score[score >=60]
passes = 0
print(a)

for x in a:
   passes+=1

print("the amount of student passed",passes)


score[score<60] = 0
print(score)
    

for x in  range (len(score)):
    y = 0
    while y<len(score):
        if score[y]>score[x]:
            temp = score[x]
            score[x] = score[y]
            score[y] = temp

        y+=1

print(score)


print("highest score index  =",len(score)-1,score[len(score)-1])


score1 = np.array([45, 67, 89, 100, 23, 56, 100, 72, 49, 95])

print(np.where(score1==100))

maxscore = np.max(score1)
maxindex = np.argmax(score1)

minscore = np.min(score1)
minindex = np.argmin(score1)

print(maxscore,maxindex)
print(minscore,minindex)

