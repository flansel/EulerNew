import math
import feuler

maxc = [0,1]
c = 0
for i in range(2, 1000000):
    j = i
    c = 0
    while j != 1:
        if j % 2 == 0:
            j = j/2
        else:
            j = 3*j +1
        c+=1
    if c > maxc[0]:
        maxc[0] = c
        maxc[1] = i
print(maxc)
