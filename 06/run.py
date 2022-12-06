import sys

with open(sys.argv[-1]) as f:
    lines = f.readlines()

def algorithm(size):
    group = []
    for id in range(len((lines[0]))):
        for i in range(0,size):
            group.append(lines[0][id+i])
        if (len(set(group)) == len(group)):
            return id+size
        else:
            group = []

position1 = algorithm(4)
position2 = algorithm(14)

print("Part1:", position1)
print("Part2:", position2)