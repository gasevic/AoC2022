import sys
import fnmatch

summary={}
rec_summary={}
read=False
tempsum=0
part1=0

with open(sys.argv[-1]) as f:
    lines = f.readlines()

# Read in all paths and the size of (only) the files in the folder 
for line in lines:
    if fnmatch.fnmatch(line, "$ cd*"):
        if read:
            for j in summary:
                if j == path:
                    continue
            summary[path]=tempsum
            read=False
            tempsum=0
        if(line.split()[2]) == "/":
            path="/"
            continue
        if(line.split()[2]) == "..":
            path='/'.join(path.split('/')[:-2])+"/"
            continue
        else:
            path=path+line.split()[2]+"/"
            continue
    if line.strip() == "$ ls":
        read=True
        continue
    if line == lines[-1]:
        summary[path]=tempsum+int(line.split()[0])
    if read:
        if line.split()[0] != "dir":
            tempsum=tempsum+int(line.split()[0])
            continue

# Include size of subfolders:
for i in summary:
    for j in summary:
        if i == j:
            continue
        if fnmatch.fnmatch(j, i+"*"):
            summary[i]=summary[i]+summary[j]
        
needed_space=30000000-(70000000-summary["/"])
del_folders=[]

# Check if file size is below 100.000 & make sum (part1)
# Check if folder can be deleted (part2)
for i in summary:
    if summary[i] >= needed_space:
        del_folders.append(summary[i])
    if summary[i] <= 100000:
        part1=part1+summary[i]
del_folders.sort()
    
print("Part1:", part1)
print("Part2:", del_folders[0])