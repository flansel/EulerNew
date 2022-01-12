import math
import f_utils

r = f_utils.seive(100001)
p = [i for i,x in enumerate(r) if x == True]

def coprime(N):
    ret = 0

    if r[N] == True:
        math.floor(N/2) - math.floor(N/3)
    
    x = set(prime_factor(N))
    seive = [True for i in range(N)]
    seive[0] = False
    for pi in p:
        if pi in x:
            k = 1
            while k*pi < N:
                seive[k*pi] = False
                k += 1
    for i in range(math.floor(N/3)+1, N):
        if i/N >= (1/2):
            break
        elif seive[i] == True:
            ret += 1
    return ret

def prime_factor(N):
    idx = 0
    factors = []
    while N > 1:
        if N % p[idx] == 0:
            #print(p[idx])
            N /= p[idx]
            factors.append(p[idx])
        else:
            idx+=1
    return factors
"""
print(prime_factor(8))
print(prime_factor(34))
print(coprime(8,5))
"""
ans = 0
RANGE = 12000

for i in range(3,RANGE+1):
    t = coprime(i)
    #print(i, t)
    ans += t
print(ans)
