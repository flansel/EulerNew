def seive(N):
    r = [True for i in range(N+1)]
    r[0] = False
    r[1] = False

    for i in range(2, N+1):
        if r[i] == True:
            k = 2 
            while i*k <= N:
                r[i*k] = False
                k += 1
    return r
