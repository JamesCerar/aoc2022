import os
from collections import Counter



#open file, get values as list of integers
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')

with open(filename, "r") as o:
    inputList = [i.replace('\n','').split(",") for i in list(map(str, o.readlines()))]

inputList = inputList[0][0]


#Part A:
for i in range(0,len(inputList)):
    curString = Counter(inputList[i:i+4])
    if len(curString) == 4:
        print(inputList[i:i+4])
        print(i+4)
        break

#Part B:
for i in range(0,len(inputList)):
    curString = Counter(inputList[i:i+14])
    if len(curString) == 14:
        print(inputList[i:i+14])
        print(i+14)
        break