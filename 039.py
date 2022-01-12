import math
"""
ans = [0 for i in range(1001)]

for n in range(2,1001):
    for m in range(n+1,1001):
        a = m**2 - n**2
        b = 2*n*m
        c = n**2 + m**2
        
        print(a,b,c)

        if a + b + c > 1000:
            break

        ans[a+b+c] += 1

ans.sort()
print(ans)
"""

sol = [0 for i in range(1001)]

for a in range(1,1001):
    for b in range(1,1001):
        c = a**2 + b**2
        c = math.sqrt(c)
        if a + b + c < 1000 and c == int(c):
            print(a,b,c,a+b+c)
            sol[int(a+b+c)] += 1

m = 0
mi = 0
for i,x in enumerate(sol):
    if x > m:
        m = x
        mi = i
print(m,mi)
