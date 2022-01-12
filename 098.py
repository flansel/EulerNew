f = open("098words.txt", "r")
s = f.read().replace("\n","").replace("\"","").split(",")

agrams = []
anums = [[] for i in range(12)]
hm = {}
hm2 = {}

for wrd in s:
    x = list(wrd)
    x.sort()
    x = tuple(x)

    if x in hm and hm[x] != wrd[::-1]:
        agrams.append([hm[x], wrd])
    
    hm[x] = wrd

for i in range(2,10000):
    x = list(str(i**2))
    x.sort()
    x = tuple(x)

    if x in hm2:
        anums[len(x)].append([str(hm2[x]), str(i**2)])

    hm2[x] = i**2

msq = 0
FAILEDMAP = False

for pw in agrams:
    for pn in anums[len(pw[0])]:
        assoc = {}
        assoc2 = {}
        for i,c in enumerate(pw[0]):
            if c in assoc:
                if pn[0][i] != assoc[c]:
                    FAILEDMAP = True
                    break
            if pn[0][i] in assoc2:
                if assoc2[pn[0][i]] != c:
                    FAILEDMAP = True
                    break
            assoc[c] = pn[0][i]
            assoc2[pn[0][i]] = c
        
        if FAILEDMAP == True:
            FAILEDMAP = False
            continue
        
        for i,c in enumerate(pw[1]):
            if assoc[c] != pn[1][i]:
                FAILEDMAP = True
                break
            if assoc2[pn[1][i]] != c:
                FAILEDMAP = True
                break
        
        if FAILEDMAP == True:
            FAILEDMAP = False
            continue
        
        csq = max(int(pn[0]), int(pn[1]))
        
        if csq > msq:
            msq = csq
            print(msq, pw, pn)
