import math

def convergents(d, r):
    a = [math.floor(math.sqrt(d))]
    p = [a[0]]
    q = [1]
    P = [0, a[0]]
    Q = [1, d - (a[0]**2)]
    a.append(math.floor((a[0] + P[1])/Q[1]))
    p.append(a[0]*a[1] +1)
    q.append(a[1])
    for n in range(2,r+1):
        P.append(a[n-1]*Q[n-1] - P[n-1])
        Q.append((d - P[n]**2)/Q[n-1])
        a.append(math.floor((a[0] + P[n])/Q[n]))
        p.append((a[n]*p[n-1]) + p[n-2])
        q.append(a[n]*q[n-1] + q[n-2])
    
    idx = 0
    for ri,an in enumerate(a):
        if an == 2*a[0]:
           idx = ri-1
           break
    
    if idx % 2 == 0:
        return (p[2*idx +1], q[2*idx +1])
    else:
        return (p[idx], q[idx])

mx = 0
mi = 0
for d in range(2,1001):
    if math.sqrt(d) == int(math.sqrt(d)):
        continue
    z = convergents(d, 1000)[1] 
    if z > mx:
        mx = z
        mi = d
print(mx,mi)
