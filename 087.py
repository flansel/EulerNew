import math
import f_utils

s = f_utils.seive(int(math.sqrt(50000000)))
p = [i for i,p in enumerate(s) if p == True]

fnd = set()

ans = 0

for sq in p:
    for cu in p:
        for fo in p:
            z = sq**2 + cu**3 + fo**4
            if z < 50000000:
                if z not in fnd:
                #print(sq,cu,fo)
                    ans += 1
                    fnd.add(z)
            else:
                break
print(ans)
