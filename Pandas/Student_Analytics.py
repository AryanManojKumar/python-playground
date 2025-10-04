import numpy as np
import pandas as pd 

rdgen = np.random.default_rng(seed=10)



studen_marks = rdgen.integers(low=0,high=100,size=[4,10],)
print(studen_marks,np.shape(studen_marks))


df = pd.DataFrame(studen_marks,index=["Trignomatery","calculus","Physics","Chemistry"])

print(df)

avgmarks = np.mean(studen_marks,axis=0)
df.loc["avg"] = avgmarks



print(df)


totalmarksperstudent = np.sum(studen_marks,axis=0)

df.loc["total"] = totalmarksperstudent

print(df)

print("topper is the student no.",np.argmax(totalmarksperstudent))

subject_avg = np.mean(df,axis=1)

df["avg"] = subject_avg

print(df)

firstdivision = avgmarks[avgmarks>70]








