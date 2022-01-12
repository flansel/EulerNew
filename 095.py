import math

RANGE = 1000000
curr = set()

s = [1 for i in range(RANGE+1)]

for i in range(2,RANGE+1):
    k = 2
    while i*k < RANGE+1:
        s[i*k] += i
        k += 1

print(s[12496])

ml = 0
mi = 1000001

for i in range(2, RANGE):
    curr = set()
    nxt = i
    curr.add(i)
    cl = 1
    ci = nxt
    #print("next", nxt)
    while nxt < 1000000:
        nxt = s[nxt]
        #print("next", nxt)
        if nxt < ci:
            ci = nxt
        if nxt in curr:
            if nxt == i and cl > ml:
                ml = cl
                mi = ci
                print(ml,mi,i)
                #for x in curr:
                    #print(x)
            break
        curr.add(nxt)
        cl+=1
print(ml,mi)
