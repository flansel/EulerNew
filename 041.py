import math
from itertools import permutations

d =  ["7", "6", "5", "4", "3", "2", "1"]

l = list(permutations(d))

def isp(N):
    for i in range(2,int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

for x in l:
    s = int("".join(x))
    #print(s)
    if isp(s):
        print(s)
        break
