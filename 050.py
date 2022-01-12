RANGE = 1000000

s = [True for i in range(RANGE+1)]
p = []
s[0] = False
s[1] = False

for i in range(2, RANGE+1):
    if s[i] == True:
        k = 2
        while i*k <= RANGE:
            s[i*k] = False
            k += 1

for i,z in enumerate(s):
    if z == True:
        p.append(i)

maxl = [0,0]

for i in range(len(p)):
    curr = [0,0]
    for j in range(i, len(p)):
        curr[0] += p[j]
        curr[1] += 1

        if curr[0] >= len(s):
            break

        if s[curr[0]] == True and curr[1] > maxl[1]:
            maxl[0] = curr[0]
            maxl[1] = curr[1]
            print(maxl)

print(maxl)
