n = 1
m = 1
ii = 2

while len(str(n)) < 1000:
    t = n
    n = m+n
    m = t
    ii+=1
    print(n)
print(ii)

