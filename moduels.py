import moduels_util

print(moduels_util.Adding(5,5))
print(moduels_util.Subtracting(10,5))

f = moduels_util.person["id"]
print(f)


from moduels_util import onlyimportingthis #this will only import this function

onlyimportingthis("frankOcean")



import os 

print(os.getcwd())

####
import string_utils
import maths_util

print(string_utils.revstring("hi"))
print("this many vowels",string_utils.countvowel("how many vowels here"))
print(string_utils.capfirstword("first letter of words will be cap"))
print(maths_util.factorial(5))
print(maths_util.primenmber(6))