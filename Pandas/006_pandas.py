import pandas as pd 
import numpy as np

data = {
    "name":["apdillion","sikandar_kalon","diljitdoshaj"],
    "Networth":[1000,2000,3000]
}

dataframe = pd.DataFrame(data,index=["singer1","singer2","singer3"])

print(dataframe)

print(dataframe.loc["singer3"])

#adding column 

dataframe["residency"] = ["Canada","india","usa"]
print(dataframe)

#adding row , for adding a new row will make a new dataframe and concat that row to the existing dataframe

newrow = {
    "name" :["sindhumoosewala"],
    "Networth" : [6000],
    "residency" : ["India punjab"],
}

df = pd.DataFrame(newrow,index=["singer4"])
print(df)


df = pd.concat([dataframe,df])
print(df)


#can add column with same world in every row
dataframe["tour"] = "worldtour"
print(dataframe)


