ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

huns = ["", "hundred"]

thou = ["", "thousand"]

s = 0
for i in range(1001):
    n = str(i)[::-1]
    tf = False
    if i > 10 and int(str(i)[-2:]) > 10 and int(str(i)[-2:]) < 20:
            s+= len(teens[int(str(i)[-2:])-10])
            print(teens[int(str(i)[-2:])-10],end="")
            tf = True
    for j,c in enumerate(n):
        if j == 0 and tf == False:
            s+= len(ones[int(c)])
            print(ones[int(c)], end="")
        elif j == 1 and tf == False:
            s+= len(tens[int(c)])
            print(tens[int(c)], end="")
        elif j == 2 and int(c) > 0:
            s+= len(ones[int(c)]) + len(huns[1])
            print(ones[int(c)] + huns[1], end="")
            if int(str(i)[-2:]) > 0:
                s+=3
                print("and", int(str(i)[-2:]), end="") 
        elif j == 3:
            s+= len(ones[int(c)]) + len(thou[1])
            print(ones[int(c)] + thou[1], end="")
    print("\n")
    tf = False
print(s)
    
