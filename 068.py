import itertools
from collections import defaultdict

d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y = itertools.combinations(d, 3)

sfam = [[] for i in range(30)]
paths = defaultdict(set)
for x in y:
    sfam[sum(x)].append(x)

for fam in sfam:
    if len(fam) >= 5:
        for trip in fam:
            for trip2 in fam:
                if trip == trip2:
                    continue
                if len(set(trip+trip2)) == 5:
                    for i,x in enumerate(trip):
                        if x in trip2:
                            idx = trip2.index(x)
                            z = itertools.permutations(trip2)
                            for perm in z:
                                if perm[1] != x:
                                    continue
                                if i == 0 :
                                    t1 = (trip[1], trip[2], trip[0])
                                    t2 = (trip[2], trip[1], trip[0])
                                   
                                    paths[t1].add(perm)
                                    paths[t2].add(perm)
                                    
                                elif i == 1:
                                    t1 = (trip[0], trip[2], trip[1])
                                    t2 = (trip[2], trip[0], trip[1])
                                    paths[t1].add(perm)
                                    paths[t2].add(perm)
                                    
                                elif i == 2:
                                    t1 = trip
                                    t2 = (trip[1], trip[0], trip[2])
                                    paths[t1].add(perm)
                                    paths[t2].add(perm)
                                    
#for x in paths:
#    print(x, paths[x])

check = []

for x in list(paths):
    stack = [(x, [x])]
    visited = set()
    while len(stack) > 0:
        #print(len(stack))
        s = stack.pop()
        z = s[0]
        p = s[1]

        if len(p) == 5:
            if p[4][2] == p[0][1]:
                check.append(p)
            else:
                continue

        for y in paths[z]:
            for k in range(0 if len(p) < 4 else 1,len(p)-1):
                if len(set(list(p[k])+list(y))) < 6:
                    break
            else:
                #print(y,p)
                stack.append((y,p+[y]))
mx = 0

for pos in check:
    idx = 0
    mn = 100
    for i,x in enumerate(pos):
        if x[0] < mn:
            mn = x[0]
            idx = i
    lpcnt = 0
    st = ""
    while lpcnt < 5:
        st += "".join(map(lambda x: str(x), pos[idx]))
        lpcnt += 1
        idx = (idx + 1)%5
    if len(st) == 17:
        continue
    if mx < int(st):
        mx = int(st)
        print(mx)
