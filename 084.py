import math
import random

board = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3", "JAIL", "C1", "U1",
        "C2", "C3", "R2", "D1", "CC2", "D2", "D3", "FP", "E1", "CH2", "E2", "E3", "R3", "F1",
        "F2", "U2", "F3", "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]

bTrack = [[0,i] for i in range(len(board))]
bTrack[0][0] = 1

CC = ["" for i in range(16)]
CC[0] = "GO"
CC[1] = "JAIL"

random.shuffle(CC)

CH = ["" for i in range(16)]
CH[0] = "GO"
CH[1] = "JAIL"
CH[2] = "C1"
CH[3] = "E3"
CH[4] = "H2"
CH[5] = "R1"
CH[6] = "R"
CH[7] = "R"
CH[8] = "U"
CH[9] = "BACK"

random.shuffle(CH)

POS = 0
ITERATION = 1000000
TRACKER = 0
DOUBLES = 0
while TRACKER < ITERATION:
    r1 = random.randrange(1,5)
    r2 = random.randrange(1,5)
    if r1 == r2:
        DOUBLES += 1
    else:
        DOUBLES = 0

    if DOUBLES < 3:
        POS = (POS+r1 + r2) % len(board)
    else:
        POS = 10
        bTrack[POS][0] += 1
        DOUBLES = 0
        continue

    if board[POS][0:2] == "CC":
        Cd = CC[0]
        CC.pop(0)
        CC.append(Cd)
        if Cd == "GO":
            POS = 0
        elif Cd == "JAIL":
            POS = 10
        
        bTrack[POS][0] += 1

    elif board[POS][0:2] == "CH":
        Cd = CH[0]
        CH.pop(0)
        CH.append(Cd)
        if Cd == "GO":
            POS = 0
        elif Cd == "JAIL":
            POS = 10 
        elif Cd == "C1":
            POS = 11
        elif Cd == "E3":
            POS = 24
        elif Cd == "H2":
            POS = 39
        elif Cd == "R1":
            POS = 5
        elif Cd == "R":
            for i in range(POS, len(board)):
                if board[i][0] == "R":
                    POS = i
                    break
        elif Cd == "U":
            for i in range(POS, len(board)):
                if board[i][0] == "U":
                    POS = i
                    break
        elif Cd == "BACK":
            POS -= 3
            if POS < 0:
                POS += 40
            if board[POS][0:2] == "CC":
                Cd = CC[0]
                CC.pop(0)
                CC.append(Cd)
                if Cd == "GO":
                    POS = 0
                elif Cd == "JAIL":
                    POS = 10
        bTrack[POS][0] += 1
    elif board[POS] == "G2J":
        POS = 10
        bTrack[POS][0] += 1
    else:
        bTrack[POS][0] += 1
    TRACKER += 1

def myFunc(x):
    return x[0]

bTrack.sort(key=myFunc)

for x in bTrack:
    print(x)








