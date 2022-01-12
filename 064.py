import math

def convergents(d):
    a = [math.floor(math.sqrt(d))]
    p = [a[0]]
    q = [1]
    P = [0, a[0]]
    Q = [1, d - (a[0]**2)]
    a.append(math.floor((a[0] + P[1])/Q[1]))
    p.append(a[0]*a[1] +1)
    q.append(a[1])

    if a[1] == 2*a[0]:
        return 1

    n = 2
    while True:
        P.append(a[n-1]*Q[n-1] - P[n-1])
        Q.append((d - P[n]**2)/Q[n-1])
        a.append(math.floor((a[0] + P[n])/Q[n]))
        p.append((a[n]*p[n-1]) + p[n-2])
        q.append(a[n]*q[n-1] + q[n-2])

        if a[n] == 2*a[0]:
            break
        n += 1

    if n % 2 == 0:
        return 0
    else:
        return 1

ans = 0
for d in range(2,10001):
    if math.sqrt(d) == int(math.sqrt(d)):
        continue
    ans += convergents(d) 
print(ans)
