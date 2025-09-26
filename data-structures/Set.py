#unordered


a = {"one","two",3}

one,two,three = a

for c in a :
    print(one,two,three)


b = {1,2,2,3,3,4}
print(b)

emptyset = set()
print(type(emptyset))

nums ={1,2,3}

nums.add("hello")
print(nums)



nums.remove(3)
print(nums)


guns = {"ak","uzi","p90"}
print("ak" in guns)
guns.pop()
print(guns)
guns.pop()
print(guns)
guns.add("vandal")

f = ["vandal","phantom"]

guns.update(f,nums)
print(guns)


set1 = {"hbo","netflix","hotstar","cruncyroll","piratebay"}
set2 ={"piratebay","123movies","stremio"}

set3 = set2.union(set1) # or can use set3 = set1|set2
print(set3)


set3 = set1&set2
print(set3)
print(set2-set1)
print(set2^set1)

f = set2.difference(set1)
print(f)
