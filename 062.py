from itertools import permutations
import math

for i in range(1,10000):
    print(i)
    #n = set([''.join(p) for p in permutations(str(i**3))])
    #print(n)
    gperms = 0
    #print(i, len(n))
    #print(n)
    s = list(str(i**3))
    s.sort()
    for j in range(15000):
        x = list(str(j**3))
        x.sort()
        if x == s:
            print(i, i**3, j, j**3)
            gperms += 1
    if gperms > 3:
        print(i)
        quit()
