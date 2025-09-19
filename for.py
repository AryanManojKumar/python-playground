a = [5,6,7,8]

for x in a :
    print(x)

 
f = "lol"
j=len(f)-1
palindrome = 0

for x in (range(len(f)//2)):
  if f[x] != f[j]:
     palindrome = False
     break
else:
   palindrome = True


print(palindrome)




nums1 =[1,2,3,4]
nums2 =[4,3,2,1]

for x in nums1:
   for j in nums2 :
      if x>j:
         print(x,"is greater then",j)
      elif x==j:
        print(x,"is Equal to",j)
      else :
         print(j,"is greater then",x)
    





      
     
       
        
    