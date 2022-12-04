import os

##Part A##

#open file, get values as list of integers
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')


with open(filename, "r") as o:
    inputList = [i.strip().split(",") for i in list(map(str, o.readlines()))]


#part A
inputList = [[j.split("-") for j in i] for i in inputList]
#inputList = [[[int(k) for k in j] for j in i] for i in inputList]
inputList = [[set(range(int(l[0]),int(l[1])+1)) for l in k] for k in inputList]

contained = 0
for i in inputList:
    if i[0].intersection(i[1]) in (i[0],i[1]):
        contained += 1

print(contained)


#part B
intersected = 0
for i in inputList:
    if len(list(i[0].intersection(i[1])))>0:
        intersected += 1

print(intersected)