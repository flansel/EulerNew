# find t and b such that t > b and (b/t)*((b-1)/(t-1) = 1/2
# b(b-1) / t(t-1) = 1/2
# 1 / t(t-1) = (1/2)/(b(b-1)
# 1 / t(t-1) = b(b-1)/2
# t(t-1) = 2b(b-1)
# t^2 - t = 2b^2 - 2b

# find the smallest b such that t > 1 000 000 0000
# find b smallest b such that sb = b(b-1) > 5 000 000 0000 and 2(sb) = t(t-1) has an integer
# solution for t

d = 1000000000
n = 700000000

while True:
    
    p = (n/d) * ((n-1)/(d-1))

    if p > 1/2:
        d += 1
    elif p < 1/2:
        n += 1
    else:
        break
    print(n,d,p)
print(n,d,p)
