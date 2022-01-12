import math

s = 0

def fac_dig(L):
    N = [int(x) for x in list(str(L))]
    #print(N)
    g = 0
    for n in N:
        g+= math.factorial(n)
    return g

for i in range(3, 1000000):
    if fac_dig(i) == i:
        s+=i
        print(s,i)
