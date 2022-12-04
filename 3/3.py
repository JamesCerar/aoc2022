import os

##Part A##

#open file, get values as list of integers
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')


with open(filename, "r") as o:
    #inputList = [i.split() for i in list(map(str, o.readlines()))]
    inputList = [i.strip() for i in list(map(str, o.readlines()))]


#part A

#a=97, z=122
#A=65, Z=90

totalNum = 0
for i in inputList:
    curNum = ord(list(set(i[:int(len(i)/2)]).intersection(set(i[int(len(i)/2):])))[0])
    if curNum >= 97:
        totalNum += curNum - 96
    else:
        totalNum += curNum - 38


print(totalNum)
#part B
totalNum = 0
inputList = [set(i) for i in inputList]
groupList = [inputList[k:k+3] for k in range(0,len(inputList),3)]
for i in groupList:
    curNum = ord(list(set.intersection(*i))[0])
    if curNum >= 97:
        totalNum += curNum - 96
    else:
        totalNum += curNum - 38

print(totalNum)