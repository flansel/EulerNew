import math

ans = 0

for base in range(1,1000):
    for exp in range(50):
        x = base**exp
        if len(str(x)) == exp:
            print(base, exp, x)
            ans += 1
print(ans)
