import sys
from collections import Counter

with open(sys.argv[-1]) as f:
    lines = f.readlines()

x=0
y=0
gox=0
goy=0
h=[0,0]
t=[0,0]
position=[]

def check(h, t):

    if h[0]-t[0] == 1:
        if  h[1]-t[1] == 2:
            t[0]+=1
            t[1]+=1
        if  h[1]-t[1] == -2:
            t[0]+=1
            t[1]-=1

    if h[0]-t[0] == -1:
        if h[1]-t[1] == 2:
            t[0]-=1
            t[1]+=1
        if h[1]-t[1] == -2:
            t[0]-=1
            t[1]-=1

    if h[0]-t[0] == 2:
        t[0]+=1
        if h[1]-t[1] == 1:
            t[1] += 1
        if h[1]-t[1] == -1:
            t[1] -= 1

    if h[0]-t[0] == -2:
        t[0]-=1
        if h[1]-t[1] == 1:
            t[1] += 1
        if h[1]-t[1] == -1:
            t[1] -= 1

    if h[1]-t[1] == 2:
        t[1]+=1
    if h[1]-t[1] == -2:
        t[1]-=1
    return t



for line in lines:
    if line.strip().split()[0] == "R":
        for i in range(int(line.strip().split()[1])):
            h=[h[0]+1,h[1]]
            check(h,t)
            position.append(t.copy())

    if line.strip().split()[0] == "L":
        for i in range(int(line.strip().split()[1])):
            h=[h[0]-1,h[1]]
            check(h,t)
            position.append(t.copy())

    if line.strip().split()[0] == "U":
        for i in range(0,int(line.strip().split()[1])):
            h=[h[0],h[1]+1]
            check(h,t)
            position.append(t.copy())

    if line.strip().split()[0] == "D":
        for i in range(int(line.strip().split()[1])):
            h=[h[0],h[1]-1]
            check(h,t)
            position.append(t.copy())


print("Part1:", len(Counter(str(elem) for elem in position)))
#print("Part2:", max(score))
