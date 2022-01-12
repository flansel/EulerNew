import math

"""
cm = 0
ans = (1,1)

for d in range(1,100):
    print(d)
    for n in range(ans[0],d):
        if n/d > cm and n/d < 3/7:
            cm = n/d
            ans = (n,d)
            print(cm, (n,d))
            break
"""
n = 2
d = 5

while d < 1000000:
    n+=3
    d+=7
print((n-3)/(d-7),n-3,d-7)
