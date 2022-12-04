import sys

# Opponent: 
# A - Rock
# B - Paper
# C - Scissors
#
# Part I:
# Me (points in brakets):
# X - Rock (1)
# Y - Paper (2) 
# Z - Scissors (3)
#
# Part II:
# X - forced Lose
# Y - forced Draw
# Z - forced Win
#
# Points:
# Lose: 0
# Draw: 3
# Win: 6

sum1=0
sum2=0

with open(sys.argv[-1]) as f:
    lines = f.readlines()

for line in lines:
    if (line.split()[0]) == "A":
        if (line.split()[1]) == "X":
            sum1=sum1+4
            sum2=sum2+3
        if (line.split()[1]) == "Y":
            sum1=sum1+8
            sum2=sum2+4
        if (line.split()[1]) == "Z":
            sum1=sum1+3
            sum2=sum2+8
    if (line.split()[0]) == "B":
        if (line.split()[1]) == "X":
            sum1=sum1+1
            sum2=sum2+1
        if (line.split()[1]) == "Y":
            sum1=sum1+5
            sum2=sum2+5
        if (line.split()[1]) == "Z":
            sum1=sum1+9
            sum2=sum2+9
    if (line.split()[0]) == "C":
        if (line.split()[1]) == "X":
            sum1=sum1+7
            sum2=sum2+2
        if (line.split()[1]) == "Y":
            sum1=sum1+2
            sum2=sum2+6
        if (line.split()[1]) == "Z":
            sum1=sum1+6
            sum2=sum2+7
   
print('Part1 {}.'.format(sum1))
print('Part2 {}.'.format(sum2))
