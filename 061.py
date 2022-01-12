import math
from collections import defaultdict

nums = [set() for i in range(6)]
fams = defaultdict(set)
n = 1
donext = True

while donext:
    donext = False
    trin = int((n*(n+1))/2)
    sqn = n**2
    pentn = int((n*((3*n) -1))/2)
    hexan = n * ((2*n) -1)
    heptn = int((n * ((5*n) -3))/2)
    octan = n*((3*n)-2)
    
    if trin > 999 and trin < 10000:
        nums[0].add(trin)
        fams[str(trin)[0:2]].add(trin)
        donext = True
    if sqn > 999 and sqn < 10000:
        nums[1].add(sqn)
        fams[str(sqn)[0:2]].add(sqn)
        donext = True
    if pentn > 999 and pentn < 10000:
        nums[2].add(pentn)
        fams[str(pentn)[0:2]].add(pentn)
        donext = True
    if hexan > 999 and hexan < 10000:
        nums[3].add(hexan)
        fams[str(hexan)[0:2]].add(hexan)
        donext = True
    if heptn > 999 and heptn < 10000:
        nums[4].add(heptn)
        fams[str(heptn)[0:2]].add(heptn)
        donext = True
    if octan > 999 and octan < 10000:
        nums[5].add(octan)
        fams[str(octan)[0:2]].add(octan)
        donext = True
    if trin < 999:
        donext = True
    n += 1
"""
#print(fams)
for i in nums:
    for k in i:
        print(k)
"""
for i,x in enumerate(nums):
    for k in x:
        stack = [(k, [k], [0 if j != i else 1 for j in range(6)])]
        #print(stack)
        while len(stack) > 0:
            s = stack.pop()
            if len(s[1]) == 6 and s[1][0] in fams[str(s[1][5])[2:]]:
                print(s, sum(s[1]))
            #quit()

            for y in fams[str(s[0])[2:]]:
                for g,spot in enumerate(s[2]):
                    if spot == 0 and y in nums[g]:
                        narr = s[2][:]
                        narr[g] = 1
                        stack.append((y,s[1]+[y], narr))
"""
uu = [6670, 7056, 5688, 8855, 5565, 6533]
for h in uu:
    for i in range(6):
        if h in nums[i]:
            print(i,h)
"""
