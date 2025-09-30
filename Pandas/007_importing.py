import numpy as np
import pandas as pd


data = pd.read_csv("data.csv")

print(data.to_string())

json = pd.read_json("data.json")

print(json.to_string)



print(data[["Name","Legendary"]].to_string())

