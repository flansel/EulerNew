import math

d_sums = [0]

def gfs(n):
    s = 0
    for i in range(1,n):
        if n % i == 0:
            s+=i
    return s

def solve():
    s = 0
    
    for i in range(1,10001):
        d_sums.append(gfs(i))

    for i in range(10001):
        if d_sums[i] > 10000:
            continue
        if d_sums[d_sums[i]] == i and d_sums[i] != i:
            print(i, d_sums[i])
            s += i
    return s

print(gfs(284))
print(gfs(220))

print(solve())
