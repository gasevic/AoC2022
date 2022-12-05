import sys
import copy

with open(sys.argv[-1]) as f:
    lines = f.readlines()

stacks = []
i=0

# Read in Stacks
for id, line in enumerate(lines):
    if line in ['\n', '\r\n']: # Check for empty line
        empty_line=id
        stack_size=(len(lines[empty_line-1].strip().split()))
        for x in range(0,stack_size):
            stacks.append([])
        for revline in list(reversed(lines[:empty_line-1])):
            for x in range(1,stack_size+1):
                if revline[4*x-3].strip():  
                    stacks[i].append(revline[4*x-3])
                i=i+1
            i=0
stacks2=copy.deepcopy(stacks)

for line in lines[empty_line+1:]:
    how_many=int(line.split()[1])
    fromx=int(line.split()[3])
    tox=int(line.split()[5])

    # Part I:
    for x in reversed(stacks[fromx-1][-how_many:]):
        stacks[tox-1].append(x)
        del stacks[fromx-1][-1]

    # Part II:
    stacks2[tox-1]=stacks2[tox-1]+stacks2[fromx-1][-how_many:]
    del stacks2[fromx-1][-how_many:]

# Output:
print("Part1:", end="")
for x in stacks:
    print(x[-1], end="")
print("")
print("Part2:", end="")
for x in stacks2:
    print(x[-1], end="")