import math
#from itertools import permutations

ref = ["1","2","3","4","5","6","7","8","9"]
#l = list(permutations(d))
#m = 0

for i in range(100000):
    fnd = []
    fnd += list(str(i))
    n = 2
    
    while len(fnd) <= 9:
        x = i*n
        fnd += list(str(x))
        #print(i,x,fnd)
        if len(fnd) != len(set(fnd)) or ("0" in fnd):
            break
        if len(fnd) == 9:
            print(i,fnd)
        n += 1
    


"""
    fn = "".join(x)
    #print(fn) 
    t = [int(fn[6:]), int(fn[3:6]), int(fn[:3])]

    if t[0] % t[2] == 0 and t[1] % t[2] == 0:
        print(t)

    t2 = [int(fn[6:]), int(fn[4:6]), int(fn[2:4]), int(fn[:2])]

    if t2[0] % t2[3] == 0 and t2[1] % t2[3] == 0 and t2[2] % t2[3] == 0:
        print(t2)

    t3 = [int(fn[5:]), int(fn[2:5]), int(fn[:2])]

    if t[0] % t[2] == 0 and t[1] % t[2] == 0:
        print(t3)

for i in range(1, 4):
    for j in range(i, min(4+i, 10)):
        for k in range(j, min(4+j, 10)):
            if k == 9:
                print(i,j,k)
            for z in range(k, min(4+k, 10)):
                if z == 9:
                    print(i,j,k,z)
            else:
                break
                for y in range(z, min(4 + z, 10)):
                    if y == 9:
                        print(i,j,k,z,y)
                else:
                    break
        else:
            break
"""
