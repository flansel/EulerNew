import f_utils
s = f_utils.seive(10000)
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

for k in range(100):
    trgt = k
    p = [i for i,x in enumerate(s) if x == True and i <= trgt]

    m = len(p)
    a =f(p, m, trgt)
    if a > 5000:
        print(k)
        quit()
