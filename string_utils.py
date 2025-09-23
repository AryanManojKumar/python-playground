

def revstring(a):
    x=len(a)-1
    
    f=""
    while x>=0:
        f=f+a[x]
        x-=1

    return f



def countvowel(a):
    vowels = "aeiouAEIOU"

    count = 0
    for x in a:
        if x in vowels:
            count+=1

    return count
        

def capfirstword(a):
    
    b = a.split()
    g=""
    for x in (range(len(b))):
        f = b[x]
        f = f[0].capitalize()+f[1:]
        g=g+" "+f
        
    
    return g
    


        
