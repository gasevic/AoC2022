import sys

with open(sys.argv[-1]) as f:
    lines = f.readlines()

grid=[]
score=[]
sum=0
biggest=False

def xcheck(x,y,end,beginning=0):
    temparray=[]
    count=0
    biggest=False
    for x_check in range(beginning,end):
        temparray.append(grid[y][x_check])
    if beginning == 0:
        temparray.reverse()
    for item in temparray:
        if item < grid[y][x]:
            count=count+1
        else:
            count=count+1
            break
    if all(grid[y][x] > item for item in temparray):
        biggest=True
    if x == 0:
        count=0
    elif y == 0:
        count=0
    return biggest, count    

def ycheck(x,y,end,beginning=0):
    temparray=[]
    count=0
    biggest=False
    for y_check in range(beginning,end):
        temparray.append(grid[y_check][x])
    if beginning == 0:
        temparray.reverse()
    for item in temparray:
        if item < grid[y][x]:
            count=count+1
        else:
            count=count+1
            break
    if all(grid[y][x] > item for item in temparray):
        biggest=True
    if x == 0:
        count=0
    elif y == 0:
        count=0
    return biggest, count 


for line in lines:
    grid.append(list(line.strip()))

for x in range(len(grid[0])):
    for y in range(len(grid)):
        score.append(xcheck(x,y,x)[1]*xcheck(x,y,len(grid[y]),x+1)[1]*ycheck(x,y,y)[1]*ycheck(x,y,len(grid),y+1)[1])
        # Left Check
        if xcheck(x,y,x)[0]:
            sum=sum+1
            continue
        #Right Check
        if xcheck(x,y,len(grid[y]),x+1)[0]:
            sum=sum+1
            continue
        #Top Check
        if ycheck(x,y,y)[0]:
            sum=sum+1
            continue
        #Bottom Check
        if ycheck(x,y,len(grid),y+1)[0]:
            sum=sum+1
            continue

print("Part1:", sum)
print("Part2:", max(score))
