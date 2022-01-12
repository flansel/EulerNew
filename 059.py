from string import ascii_lowercase

def decode(pw,t):
    s = ""
    for i,c in enumerate(t):
        s+= chr(int(c)^pw[i%3])
    return s

f = open("059_text.txt", "r")
s = f.read().strip("\n").split(",")
#print(s)

for a in ascii_lowercase:
    for b in ascii_lowercase:
        for c in ascii_lowercase:
            pwd = (ord(a),ord(b),ord(c))
            r = decode(pwd,s)
            if r.find("An extract taken") != -1:
                print(r)
                rs = 0
                for c in r:
                    rs+=ord(c)
                print(rs)


