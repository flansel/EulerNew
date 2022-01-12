import math
import itertools
from collections import defaultdict
sq = [(0,1),(0,4),(0,9),(1,6),(2,5),(3,6),(4,9),(6,4),(8,1)]
d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
1st {0, 1, 2, 3, 4, (6,9), 8}
2nd {1, 4, (6,9), 5}
"""
ans = 0
comb = itertools.combinations(d,6)
mycomb = []

for c in comb:
    mycomb.append(list(c))

for c in mycomb:
    if 6 in c and 9 not in c:
        #z = [x if x != 6 else 9 for x in c]
        #if z in mycomb:
        #    mycomb.remove(z)
        c.append(9)
    elif 9 in c and 6 not in c:
        #z = [x if x != 9 else 6 for x in c]
        #if z in mycomb:
        #    mycomb.remove(z)
        c.append(6)

dup = []
for x in mycomb:
    for y in mycomb:
        if (x,y) in dup:
            continue
        for square in sq:
            if (not (square[0] in x and square[1] in y)) and not(square[0] in y and square[1] in x):
                break
        else:
            print(x,y)
            dup.append((y,x))
            """
            c1 = 1
            c2 = 1
            if len(x) > 6:
                c1 = 2
            if len(y) > 6:
                c2 = 2
            
            ans += c1 * c2
            """
            ans += 1
print(ans)
