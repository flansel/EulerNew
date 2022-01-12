import math
n = math.factorial(100)

s = 0
for c in str(n):
    s += int(c)

print(s)
