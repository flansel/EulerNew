import math

def sq_dig(N):
    ret = 0
    while N > 0:
        ret += (N%10)**2
        N //= 10
    return ret

ans = 0 

pos = [-1 for i in range(10000000)]
pos[1] = 0
pos[0] = 0
pos[89] = 1

for i in range(1,10000000):
    #print(i)
    curr = []
    y = i
    while True:
        if pos[y] == 1:
            for x in curr:
                if x < 10000000:
                    pos[x] = 1
            break
        elif pos[y] == 0:
            for x in curr:
                if x < 10000000:
                    pos[x] = 0
            break
        curr.append(y)
        #y = sum(map(lambda z: int(z)**2, list(str(y))))
        y = sq_dig(y)


print(sum(pos))
