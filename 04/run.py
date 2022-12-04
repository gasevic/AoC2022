import sys

with open(sys.argv[-1]) as f:
    lines = f.readlines()

range1=[]
range2=[]
sum = 0
sum2 = 0
i = 0

for line in lines:
    sections=line.strip().split(",")
    range1=list(range(int(sections[0].split("-")[0]),int(sections[0].split("-")[1])+1))
    range2=list(range(int(sections[1].split("-")[0]),int(sections[1].split("-")[1])+1))

    if all(x in range1  for x in range2):
        sum = sum + 1
        if all(x in range2  for x in range1):
            sum = sum - 1
    if all(x in range2  for x in range1):
        sum = sum + 1
        
    for x in range1:
        if x in range2:
            sum2 = sum2 + 1
            break

print('Part1 {}.'.format(sum))
print('Part2 {}.'.format(sum2))

