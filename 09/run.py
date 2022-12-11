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
h2=[0,0]
k1=[0,0]
k2=[0,0]
k3=[0,0]
k4=[0,0]
k5=[0,0]
k6=[0,0]
k7=[0,0]
k8=[0,0]
k9=[0,0]
position=[]
position2=[]

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


# Part I
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

# Part II
for line in lines:
    if line.strip().split()[0] == "R":
        for i in range(int(line.strip().split()[1])):
            h2=[h2[0]+1,h2[1]]
            temp=h2
            check(h2,k1)
            check(k1,k2)
            check(k2,k3)
            check(k3,k4)
            check(k4,k5)
            check(k5,k6)
            check(k6,k7)
            check(k7,k8)
            check(k8,k9)
            position2.append(k9.copy())

    if line.strip().split()[0] == "L":
        for i in range(int(line.strip().split()[1])):
            h2=[h2[0]-1,h2[1]]
            check(h2,k1)
            check(k1,k2)
            check(k2,k3)
            check(k3,k4)
            check(k4,k5)
            check(k5,k6)
            check(k6,k7)
            check(k7,k8)
            check(k8,k9)
            position2.append(k9.copy())

    if line.strip().split()[0] == "U":
        for i in range(0,int(line.strip().split()[1])):
            h2=[h2[0],h2[1]+1]
            check(h2,k1)
            check(k1,k2)
            check(k2,k3)
            check(k3,k4)
            check(k4,k5)
            check(k5,k6)
            check(k6,k7)
            check(k7,k8)
            check(k8,k9)
            position2.append(k9.copy())

    if line.strip().split()[0] == "D":
        for i in range(int(line.strip().split()[1])):
            h2=[h2[0],h2[1]-1]
            check(h2,k1)
            check(k1,k2)
            check(k2,k3)
            check(k3,k4)
            check(k4,k5)
            check(k5,k6)
            check(k6,k7)
            check(k7,k8)
            check(k8,k9)
            position2.append(k9.copy())


print("Part1:", len(Counter(str(elem) for elem in position)))
print("Part2:", len(Counter(str(elem) for elem in position2)))
#print("Park9:", max(score))
