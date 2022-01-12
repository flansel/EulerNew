import math


"""
a**2 + b**2 = c**2
a+b+c = L
a,b,c in N

"""
RANGE = 1500000

pt = [0 for i in range(RANGE+1)]

def Triplets(limits) :
    c, m = 0, 2

    # Limiting c would limit
    # all a, b and c
    while c < limits:
        # Now loop on n from 1 to m-1
        for n in range(1, m) :
            if math.gcd(m,n) != 1 or (m % 2 != 0 and n % 2 != 0):
                continue
            k = 1
            while True:
                a = k* (m * m - n * n)
                b = k* (2 * m * n)
                c = k* (m * m + n * n)

                if a + b + c < RANGE+1:
                    pt[a+b+c] += 1
                    #print(a,b,c, a+b+c)
                else:
                    break
                k += 1
            # if c is greater than
            # limit then break it
            if c > limits :
                break
        m = m + 1
Triplets(RANGE+1)
ans = 0
for n in pt:
    if n == 1:
        ans+=1
print(ans)
print(pt[24])
print(pt[120])
