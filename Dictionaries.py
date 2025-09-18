bmw = {
    "company" : "Bayerische Motoren Werke AG",
    "country" : "German",
    "model" : "m3comp",


}

print(bmw["company"])
print(bmw["country"])
print(bmw["model"])

mini = bmw.keys()
print(mini)

bmw["topspeed"] = 450

print(mini)

bmw["country"] = "india"
print(bmw["country"])

bmw.update({"country" : 1})
print(bmw["country"])


bmw["F1"] = False
print(bmw)

bmw.popitem()

print(bmw)
bmw.clear()
print(bmw)
del bmw


nums = {
    5:"one",
    6:"two",
    7:"three"
}

for x in nums:
    print(x,nums[x])

for x in nums.values():
    print(x)

for x in nums.keys():
    print(x)

for x,y in nums.items():
    print(x,y)


b = nums.copy()
print(b)

cars = {
    "american":{
        "company":"ford",
        "revenue":"1billion"
    },
    "german":{
        "company":"bmw",
        "revenue":"2billion"
    }
}

print(cars["german"]["revenue"])

for x in cars["american"]:
    print(x,cars["american"][x])

for x ,y in cars.items():
    print(x,y)
