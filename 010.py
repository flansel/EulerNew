import math
import feuler

a = feuler.prime_sieve(2000000)
sumx = 0

for idx, x in enumerate(a):
    if x:
        sumx+=idx
print(sumx)
