import pandas as pd
import numpy as np


df= pd.read_csv("data.csv")

# print(df[["Name","Legendary"]].to_string())
print(df["Height"])

print(df["Type1"])

print(df.loc[0])


#used the name as an index 
df = pd.read_csv("data.csv",index_col="Name")

print(df.loc["Pikachu"])

#this will only show the height of pikachu
print(df.loc["Pikachu",["Height"]])


#you can even use the slice to print from this to this

print(df.loc["Pikachu":"Rapidash",["Height","Weight"]])







