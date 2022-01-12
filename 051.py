import math
import f_utils
import itertools

s = f_utils.seive(1000000)
p = [i for i,x in enumerate(s) if x == True]
c = 0

iters = []
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def is_prime(N):
    if N < 1000000:
        return s[N]

    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

for i in range(7):
    yy = itertools.combinations(list(range(7)),i)
    iters.append(list(yy))

iters.pop(0)

for prm in p:
    sp = str(prm)
    for i, lnfam in enumerate(iters):
        for comb in lnfam:
            cnt = 0
            ms = 0
            tmp = list(sp)
            if max(comb) >= len(sp):
                continue
            for d in digits:
                lmin = 1000000
                for idx in comb:
                    #print(idx, comb, tmp)
                    tmp[idx] = d
                #if prm == 56003 and comb == (2,3):
                    #print(prm, sp,tmp, cnt, comb)
                tst = int("".join(tmp))
                if tst == prm:
                    continue
                if d == "0" and 0 in comb:
                    continue
                if is_prime(tst):
                    cnt += 1
                    print(tst)
                    if cnt >= 8:
                        print(prm, comb, cnt, lmin)
                        quit()
                else:
                    ms += 1
