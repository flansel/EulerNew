n = 1
x = 0
mi = 2000001
ans = 0

for j in range(1,1000):
    z = (j*(j+1))/2
    n = 1
    it = 0
    x = 0
    while x <= 2000000:
        x = z*((n*(n+1))/2)
        curr = 2000000-x
        #print(z,n,x)
        if curr < mi and curr > 0:
            mi = curr
            ans = [n*j, n, j, z, x]
        n+=1

print(((3*(4))/2)*((3*(4))/2))
print(mi, ans)
