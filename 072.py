import math
import f_utils

r = f_utils.seive(1000000)
p = [i for i,x in enumerate(r) if x == True]

ans = 0

for i in range(10000):
    phi = 1
    n = i
    for pi in p:
        if pi > i:
            break
        elif i % pi == 0:
            phi *= (1-(1/pi))
            n /= pi
    phi*=i
    ans+=phi
    print(i, phi)
print(ans)

"""
This is the basic idea, dont care to deal with slow af python

mathatica Sum[EulerPhi[i], {i, 2, 1000000}] is sufficient

"""
