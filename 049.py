RANGE = 10000

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

def check(N):
    pcount = 1
    l0 = set(list(str(N)))
    l1 = set(list(str(N+3330)))
    l2 = set(list(str(N+6660)))
    
    if N + 3330 < 10000 and s[N + 3330] != True:
        return False
    if N + 6660 < 10000 and s[N + 6660] != True:
        return False

    if l0 != l1 or l0 != l2:
        return False
    print(N, N+3330, N+6660)
    return True


for i in range(1000, 10001):
    if s[i] == True:
        check(i)
