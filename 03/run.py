import sys
from string import ascii_lowercase as alc

with open(sys.argv[-1]) as f:
    lines = f.readlines()

match_found = False
match_cases=[]
priority_list=['']
priority_sum=0
priority_sum2=0
i=0
group=[]
group_match=[]
group_priorities=[]

for line in lines:
    # Part I:
    word1 = line[0:len(line.strip())//2]
    word2 = line[len(line.strip())//2:len(line.strip())]
    for x in word1:
        for y in word2:
            if x == y:
                match_found = True
                match_cases.append(x)
                break
        if match_found:
            match_found = False
            break

    # Part II:
    i=i+1
    if i < 4:
        group.append(line.strip())
    if i == 3:
        for x in group[0]:
            for y in group[1]:
                if x == y:
                    group_match.append(x)
        for x in group[2]:
            if x in group_match:
                group_priorities.append(x)
                i = 0
                group=[]
                group_match=[]

                
# Priority list:

for i in alc:
    priority_list.append(i)
for i in alc:
    priority_list.append(i.upper())

for i in match_cases:
    priority_sum = priority_sum + priority_list.index(i)
for i in group_priorities:
    priority_sum2 = priority_sum2 + priority_list.index(i)

print('Part1 {}.'.format(priority_sum))
print('Part2 {}.'.format(priority_sum2))

