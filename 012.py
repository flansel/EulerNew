import math
import feuler

i = 1
j = 2

divisors = []
while len(divisors) <= 500:
    divisors = []
    i += j
    j += 1
    for d in range(1,int(math.sqrt(i))+1): 
        if i % d == 0:
            divisors.append(d)
            divisors.append(i/d)
    #print(i, divisors)
print(i)
