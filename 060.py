import math
import f_utils


def is_prime(N):
    if N < 2:
        return False
    for i in range(2,int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

RANGE = 10000

s = f_utils.seive(RANGE)
p = [i for i,x in enumerate(s) if x == True]

arr = [set() for i in range(RANGE)]

for prm in p:
    for prm2 in p:
        if prm == prm2 or prm2 in arr[prm]:
            continue

        sz1 = int(math.log10(prm))+1
        sz2 = int(math.log10(prm2))+1

        t1 = prm2 * (10**sz1) + prm
        t2 = prm * (10**sz2) + prm2
        
        f1 = False
        f2 = False
        
        if t1 < RANGE:
            if s[t1] == True:
                f1 = True
        elif is_prime(t1):
            f1 = True
        else:
            continue

        if t2 < RANGE:
            if s[t2] == True:
                f2 = True
        elif is_prime(t2):
            f2 = True
        else:
            continue
        
        if f1 == True and f2 == True:
            arr[prm].add(prm2)
            arr[prm2].add(prm)
"""
for prme in p:
    prm = prme
    N = 0
    zcnt = 0
    cnt  = 0
    while True:
        while prm % 10 == 0:
            zcnt += 1
            prm //= 10
            continue
        N = ((prm % 10) * (10**(cnt+zcnt))) + N
        prm //= 10

        if prm == 0:
            break

        sz = int(math.log10(prm))+1
        
        if s[N] == True and s[prm] == True:
            rev = (N * (10**sz))+prm
            if rev < 20000000:
                if s[rev] == True:
                #if (prm == 9679 and N  == 3) or (prm == 3 and N == 9679):
                    #print(prme, prm, N, rev, cnt)
                    arr[prm].add(N)
                    arr[N].add(prm)
            elif is_prime(rev):
                arr[prm].add(N)
                arr[N].add(prm)
                #print("fnd over", prm, N)
        cnt += 1
"""
arr2 = [[] for i in range(RANGE)]

for i,fam in enumerate(arr):
    #print(key,value)
    arr2[i] = list(fam)

print(673 in arr[3])
print(673 in arr[7])
print(673 in arr[109])

def DFS(s):
    
    stack = []

    stack.append((s,[]))

    while(len(stack)):
        s = stack[0]
        stack.pop(0)

        if len(s[1]) >= 4:
            print(s, len(s[1]), sum(s[1])+s[0])

        for node in arr2[s[0]]:
            if node not in s[1]:
                for x in s[1]:
                    if node not in arr[x]:
                        break
                else:
                    stack.append((node, s[1]+[s[0]]))


for i in range(len(p)):
    DFS(p[i])
