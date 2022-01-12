from collections import Counter

def hand_eval(h):
    flush = False
    straight = False

    n = [ord(c) for i,c in enumerate(h) if i % 2 == 0]
    s = [c for i,c in enumerate(h) if i % 2 != 0]
    
    for i in range(len(n)):
        if n[i] == ord('A'):
            n[i] = 14
        elif n[i] == ord('K'):
            n[i] = 13
        elif n[i] == ord('Q'):
            n[i] = 12
        elif n[i] == ord('J'):
            n[i] = 11
        elif n[i] == ord('T'):
            n[i] = 10
        else:
            n[i] = int(chr(n[i]))

    n.sort()

    if len(set(s)) == 1:
        flush = True
    
    for i in range(len(n)-1):
        if n[i+1]-1 != n[i]:
            straight = False
            break
    else:
        straight = True

    if straight and flush:
        if n[len(n)-1] == 14:
            return (10, n[4])
        else:
            return (9, n[4])
    if n[0] == n[3] or n[1] == n[4]:
        return (8, n[4])
    
    if len(set(n)) == 2:
        if n[0] == n[2]:
            return (7,n[0])
        else:
            return (7,n[4])

    if flush:
        return (6, n[4])
    
    if straight:
        return (5, n[4])
    
    y = Counter(n)
    z = list(y.values())
    
    if max(z) == 3:
        if n[0] == n[1]:
            return (4,n[0])
        elif n[1] == n[2]:
            return (4,n[1])
        else:
            return (4,n[2])
    
    if len(set(n)) == 3:
        if n[4] == n[3]:
            if n[2] == n[1]:
                return (3,n[4],n[2],n[0])
            else:
                return (3,n[4],n[1],n[2])
        else:
            return (3,n[3],n[1],n[4])

    if max(z) == 2:
        p = 0
        for i in range(len(n)-1):
            if n[i] == n[i+1]:
                p = n[i]
                n.pop(i+1)
                n.pop(i)
                break
        return (2,p,max(n))
   
    return (1,n[4])
    
p1w = 0
f = open("054_poker.txt", "r")
for l in f:
    h1 = l[0:14].replace(" ","")
    h2 = l[15:len(l)-1].replace(" ","")
    
    print(h1,h2)

    h1s = hand_eval(h1)
    h2s = hand_eval(h2)

    print(h1s,h2s)

    for i in range(len(h1s)):
        if h1s[i] > h2s[i]:
            p1w+=1
            print("p1")
            break
        elif h2s[i] > h1s[i]:
            print("p2")
            break
print(p1w)


