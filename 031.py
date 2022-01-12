c = [1,2,5,10,20,50,100,200]

"""

"""

def f(S, m, n):
    if(n == 0):
        return 1
    if(n < 0 ):
        return 0

    if(m <= 0 and n >= 1):
        return 0

    return f(S, m - 1, n) + f(S, m, n-S[m-1])

m = len(c)
print(f(c, m, 200))
