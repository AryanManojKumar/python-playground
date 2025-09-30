import pandas as pd
import numpy as np

print(pd.__version__)

data = np.array([100,102,103,104])

series = pd.Series(data,index=["a","b","c","d"])
print(series)

series.loc["a"] = 120

print(series.loc["a"]) #location by keyword

print(series.iloc[1])   #localtion by integer

for x in range (len(series)):   
    print(series.iloc[x])


less = series[series<105]
print(less)
max = np.max(series)
print(max)


calories = {"day1":1000,"day2":2000,"day3":3000}

series = pd.Series(calories)
print(series)

series.iloc[2] += 400
print(series)

series.loc["day1"] -= 200
print(series)

cheatday = series[series>2500]
print(cheatday)


mean = np.mean(series)
print(mean)
