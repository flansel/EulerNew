import math

ans = 0

for i in range(1,101):
    for j in range(1,i+1):
        x = math.factorial(i)/(math.factorial(j) * math.factorial(i-j))
        if x > 1000000:
            ans += 1
print(ans)
