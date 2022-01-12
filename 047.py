import math
import f_utils

def pf(r, N):
    fac = []
    for i,d in enumerate(r):
        if i > N:
            break
        while d == True and N % i == 0:
            fac.append(i)
            N /= i
    return fac


s = f_utils.seive(1000001)

c = 0

for i in range(2,1000000):
    x = pf(s,i)
    if len(set(x)) == 4:
        #print(i, x, c)
        c += 1
    else:
        c = 0

    if c == 4:
        print("FND: ", i-3)
        quit()


