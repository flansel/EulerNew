import math
import feuler

def prime_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False
    ptrack = 0
    for idx in range(2, len(a)):
        if a[idx] == False:
            continue
        x = idx*2
        while x < len(a):
            a[x] = False
            x+=idx
    for p in range(len(a)):
        if a[p] == True:
            ptrack+=1
            #print(p)
            if ptrack == 10001:
                print(p)

prime_sieve(10000000)

