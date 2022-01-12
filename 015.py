from array import array
import math
import feuler
"""

def s(r,c):
    if r < 5 and c < 5:
        #print(r,c)
        return s(r+1,c) + s(r,c+1)
    return 1


def si(r,c):
    cl = array("b",[0,1])
    print(cl.typecode)
    nl = array("b")
    track = 1
    ec = 0
    while True:
        print(track)
        track+=1
        #print(cl)
        for i in range(0,len(cl),2):
            
            if cl[i] < r:
                nl.append(cl[i]+1)
                nl.append(cl[i+1])
            if cl[i+1] < c:
                nl.append(cl[i])
                nl.append(cl[i+1]+1)
            
            if cl[i] < r and cl[i+1] < c:
                nl.append(cl[i])
                nl.append(cl[i+1]+1)
                nl.append(cl[i]+1)
                nl.append(cl[i+1])
            else:
                #cl.pop(i+1)
                #cl.pop(i)
                ec+=1
        if len(nl) == 0:
            return ec
        cl = nl
        nl = array("b")

print("ans", si(20,20)*2)
"""





