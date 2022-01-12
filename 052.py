for i in range(1,1000000):
    s = list(str(i))
    s.sort()
    for m in range(2,7):
        t = list(str(i*m))
        t.sort()
        print(s,t,s==t)
        if s != t:
            break
    else:
        print(i)
        quit()

