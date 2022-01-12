import math

def is_prime(N):
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

def f(N):
    for x in list(str(N)):
        if int(x) % 2 == 0:
            return False
    return True

def g(N):
    d = list(str(N))
    for i in range(len(d)+1):
        j = d.pop()
        d.insert(0,j)
        if not is_prime(int("".join(d))):
            return False
    return True

s = 1

for i in range(3,1000000,2):
    if f(i) == True and g(i) == True:
        s += 1
        print(s,i)

