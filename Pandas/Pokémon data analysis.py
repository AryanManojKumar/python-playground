import numpy as np
import pandas as pd


csv = pd.read_csv("data.csv")


print(csv.loc[:,"Name"].to_string())

print("Total no. of pokemon",len(csv))


leng = csv[csv["Legendary"]>0]

print(leng)



avgh = np.mean(csv["Height"])
print("AVg heigh of the pokemons is ",avgh)

avgW = np.mean(csv["Weight"])
print("avg weight of the pokemons is ",avgW)

tallest = np.argmax(csv["Height"])
print("the Tallest one is ",csv.loc[tallest,"Name"])

fattest = np.argmax(csv["Weight"])
print("fattest one is ",csv.loc[fattest,"Name"])

bmi =  csv["Weight"]/(csv["Height"]**2)

csv["Bmi"] = bmi

print(csv)

grasstype =  csv[csv["Type1"]=="Grass"]

avggrassheight = np.mean(grasstype["Height"])
print("avg height of the grass type is ",avggrassheight)


summary = pd.DataFrame({
    "stats":["avg height","avg weight","tallest","fattest"],
    "values":[avgh,avgW,csv.loc[tallest,"Name"],csv.loc[fattest,"Name"]],
})


print(csv.to_string())

print("summary of the csv")
print(summary)