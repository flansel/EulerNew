import math
import f_utils
import collections

s = f_utils.seive(1000000)
p = [i for i,x in enumerate(s) if x == True]

m = 87109/79180
mi = 87109
phii = 79180

for i in reversed(range(2, 25000)):
    for j in range(2, 25000):
        #print(i,j)
        x = p[i]*p[j]
        if x < 10000000:
            phi = (p[i]-1)*(p[j]-1)
            if x/phi < m:
                #print(x, phi, x/phi)
                if collections.Counter(list(str(phi))) == collections.Counter((list(str(x)))):
                        print(x, phi, x/phi)
                        m = x/phi
                        mi = x
                        phii = phi
        else:
            break
print(m,mi,phii)
