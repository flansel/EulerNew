import math

def f(x):
    N = str(x)
    B = bin(x)[2:]
    if N == N[::-1] and B == B[::-1]:
        return True
    return False

s = 0

for i in range(1000001):
    if f(i):
        s+=i
print(s)
