import os
import numpy as np
import re

def addRange(rangeList,curRange):
    for i in range(0,len(rangeList)):
        if rangeList[i][0] > curRange[0]:
            rangeList.insert(i,curRange)
            break
    
    if curRange not in rangeList: rangeList.append(curRange)
    
    rangeListOut = []
    thisRange = rangeList.pop(0)
    while len(rangeList) > 0:
        upperRange = rangeList.pop(0)
        if thisRange[1] + 1 >= upperRange[0]:
            thisRange[0] = min(thisRange[0],upperRange[0])
            thisRange[1] = max(thisRange[1],upperRange[1])
        else:
            rangeListOut.append(thisRange)
            thisRange = upperRange
    rangeListOut.append(thisRange)
    return rangeListOut

debug = False
debugPart = 'a'
if debug:
    maxLen = 20
else:
    maxLen = 4000000


#open file, get values as list of integers
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')
if debug and debugPart.lower()=='a': filename = os.path.join(dir, 'input_debug_partA.txt')
if debug and debugPart.lower()=='b': filename = os.path.join(dir, 'input_debug_partB.txt')

with open(filename, "r") as o:
    #these letters eventually get turned into numbers - the S and E replacement turn them into 0 and 27 in that calculation
    inputList = [i.replace('\n','') for i in list(map(str, o.readlines()))]

sensorList = []
for i in inputList:
    x = re.findall('Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)',i)
    sensorList.append([(int(x[0][0]),int(x[0][1])),(int(x[0][2]),int(x[0][3])),abs(int(x[0][0])-int(x[0][2]))+abs(int(x[0][1])-int(x[0][3]))])

for checkRow in range(0,maxLen):
    print(checkRow)
    checkSet = []
    for s in sensorList:
        if (s[0][1]<=checkRow and s[0][1]+s[2]>=checkRow) or (s[0][1]>=checkRow and s[0][1]-s[2]<=checkRow):
            y = abs(s[0][1]-checkRow)
            minX = s[0][0]-(s[2]-y)
            maxX = s[0][0]+(s[2]-y)
            if minX < 0: minX = 0
            if maxX > maxLen: maxX = maxLen
            if minX > maxLen or maxX < 0: continue
            #print(minX,maxX)
            checkSet = addRange(checkSet,[minX,maxX])
            #print(checkSet)
    if len(checkSet) > 1:
        print('solution found')
        print(checkRow)
        print(checkSet)
        break


print((checkSet[0][1]+1)*4000000 + checkRow)