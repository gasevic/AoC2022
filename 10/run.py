import sys

with open(sys.argv[-1]) as f:
    lines = f.readlines()

x=1
cycle=1
positions=(20,60,100,140,180,220)
screen=[[]]
row=0
signal=0

def check (cycle,x,signal,row,screen):
    if cycle in positions:
        signal+=cycle*x
    sprite=[x,x+1,x+2]
    if cycle-row*40 in sprite:
        screen[row].append("#")
    else:
        screen[row].append(".")
    if cycle % 40 == 0:
        row+=1
        screen.append([])
    
    return signal,row,screen

for line in lines:
    signal,row,screen=(check(cycle,x,signal,row,screen))
    if line.split()[0] == "noop":
        cycle+=1
    if line.split()[0] == "addx":
        addx = int(line.split()[1])
        cycle+=1
        signal,row,screen=(check(cycle,x,signal,row,screen))
        cycle+=1
        x+=addx

print("Part1:", signal)
print("Part2:")
for i in screen:
    print(''.join(i))
