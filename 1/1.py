import os

##Part A##

#open file, get values as list of integers
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')


with open(filename, "r") as o:
    inputList = [i.strip() for i in list(map(str, o.readlines()))]


#part A
maxCals = 0
curCals = 0
for i in inputList:
    if i == '':
        maxCals = max(maxCals,curCals)
        curCals = 0
    else:
        curCals += int(i)

print (maxCals)


#part B
allCals = []
curCals = 0
for i in inputList:
    if i == '':
        allCals.append(curCals)
        curCals = 0
    else:
        curCals += int(i)

top3Sum = sum(sorted(allCals, reverse=True)[:3])
print(top3Sum)