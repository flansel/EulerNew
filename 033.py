def checkF(a,b,x,z,g,h):
    if a != b:
        return False
    if z == 0:
        return False
    if x/z == g/h:
        return True



n = 1
d = 1
for i in range(10,100):
    for j in range(10,100):
        if i % 10 == 0 and j % 10 == 0:
            continue
        if i/j < 1:
            si = str(i)
            sj = str(j)
            if checkF(int(si[0]),int(sj[0]),int(si[1]),int(sj[1]),i,j):
                n*=i
                d*=j
            if checkF(int(si[0]),int(sj[1]),int(si[1]),int(sj[0]),i,j):
                n*=i
                d*=j
            if checkF(int(si[1]),int(sj[0]),int(si[0]),int(sj[1]),i,j):
                n*=i
                d*=j
            if checkF(int(si[1]) ,int(sj[1]),int(si[0]),int(sj[0]),i,j):
                n*=i
                d*=j

print(n,d)
