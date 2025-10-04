import pandas as pd
import numpy as np


df = pd.read_csv("data.csv")

print(df.loc[:10])

print(df.loc[0:20:2])


df = pd.read_csv("data.csv",index_col="Name")


Pokemon = input("Enter Pokemon name")

try: 
    print(df.loc[Pokemon])
except KeyError  :
    print(KeyError)

