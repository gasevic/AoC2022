import sys

with open(sys.argv[-1]) as f:
    lines = f.readlines()

sum_array=[]
temp_sum=0

for line in lines:
    if len(line.strip()) == 0 :
        sum_array.append(temp_sum)
        temp_sum = 0
    else:
        temp_sum = temp_sum + int(line)
sum_array.sort()
   
print('Part1 {}.'.format(sum_array[-1]))
print('Part2 {}.'.format(sum_array[-1]+sum_array[-2]+sum_array[-3]))
