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



sales = np.array([[120, 150, 130, 160, 200, 180, 170,
                  140, 160, 150, 170, 180, 200, 190,
                  150, 160, 170, 180, 190, 200, 210,
                  160, 170, 180, 190, 200, 210, 220]])

print(sales.shape)

sales = sales.reshape(4,7)
print(sales,sales.shape)

total_sales = np.sum(sales)
maxday = np.argmax(sales)+1
print("total sales",total_sales,"most profitable day was",maxday)

weeks_total = np.sum(sales,axis=1)
print(weeks_total)

best_week = np.argmax(weeks_total)
print(best_week+1,"th week")


grades = np.array([
    [85, 92, 78, 90],
    [88, 76, 95, 89],
    [92, 90, 94, 91],
    [70, 65, 80, 75],
    [95, 100, 98, 99]
])



meanperstudent = np.mean(grades,axis=1)
print(meanperstudent)


topscoreperstudent = np.sum(grades,axis=1)
print(topscoreperstudent)

topper = np.argmax(topscoreperstudent)
print("the top student is ",topper+1)


