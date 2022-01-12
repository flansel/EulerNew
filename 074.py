import math

def d_fac(N):
    y = str(N)
    ret = 0
    for c in y:
        ret += math.factorial(int(c))
    return ret

cl = 0
fnd = []
ans = 0
for i in range(1000000):
    fnd = []
    fnd.append(i)
    x = d_fac(i)
    cl = 1
    while x not in fnd:
        fnd.append(x)
        x = d_fac(x)
        cl +=1
        if cl == 60:
            ans += 1
            print(i)
print(ans)
