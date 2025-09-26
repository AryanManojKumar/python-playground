import numpy as np

students = np.array([[18,19,20,21,35,67],[68,43,11,19,12,44]])

gen_z = students[students <18]

print(gen_z)

millennials = students[(students<30) & (students>18)]
print(millennials)

senior = students[students>30]
print(senior)

evenages = students[students%2==0]
print(evenages)

odds = students[students%2!= 0]
print(odds)

print(students[np.where(students>18)])

a = np.argmax(students)
print(a)

adults = np.where(students>21,students,-1 )
print(adults)

adults = students[students>21]
print(adults)