import math
import f_utils

s = f_utils.seive(10000) 

for i in range(1,10000,2):
    if s[i] == True:
        continue
    for j in range(1,i):
        dif = i - 2*(j**2)
        if dif < 2:
            print(i)
            quit()
        if s[dif] == True:
            #print("GB: ", i, j, dif) 
            break
