f = open("022_names.txt", "r")
s = f.read()
s = s[0:len(s)-1]
s = s.split(",")
s.sort()

a = 0

for i,w in enumerate(s):
    wscore = 0
    for c in w:
        wscore += ord(c)-64
    a += wscore * (i+1)

print(a)
    

