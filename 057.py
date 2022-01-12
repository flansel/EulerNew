import math


"""
1/2 2/5 
"""

ans = 0

num = 1
den = 2

for i in range(1000):
    num += 2*den
    tmp = den
    den = num
    num = tmp
    print(num+den,den)
    if len(str(num + den)) > len(str(den)):
        ans += 1
print(ans)
