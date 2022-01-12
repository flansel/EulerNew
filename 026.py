def cycle_l(i):
    p = 1
    if i % 2 == 0 or i % 5 == 0:
        return 0
    while 10**p % i != 1:
        p+=1
    return p

def solve():
    max_cl = 0
    max_i = 0
    for i in range(2,1000):
        tcl = cycle_l(i)
        if tcl > max_cl:
            max_i = i
            max_cl = tcl

    return (max_i, max_cl)

print(solve())
