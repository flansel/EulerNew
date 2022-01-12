import math

d_cur = []
fnd = []
sum = 0

for i in range(4000):
    for j in range(4000):
        f = list(str(i))
        g = list(str(j))
        h = list(str(i*j))
        d_cur = f + g + h
        if "0" in d_cur:
            continue
        if len(d_cur) == 9 and len(list(set(d_cur))) == 9:
            if(i*j not in fnd):
                print(i, j, i*j)
                sum+=(i*j)
                fnd.append(i*j)
print(sum)
