import numpy as np

randomgen = np.random.default_rng(seed=1)



a = randomgen.integers(low=0,high=2,size=1000)

heads = a[a==1]
print("head count",len(heads))
tails = a[a==0]
print("tail count",len(tails))

headsprob = ((len(heads))/(len(a)) )*100
print("head prob",headsprob)
tailsprob = ((len(tails))/(len(a)) )*100
print("tail prob",tailsprob)
