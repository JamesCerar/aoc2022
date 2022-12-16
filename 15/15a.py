import os
import numpy as np
import re

debug = False
debugPart = 'a'
if debug:
    checkRow = 10
else:
    checkRow = 2000000

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

checkSet = set()
for s in sensorList:
    if (s[0][1]<=checkRow and s[0][1]+s[2]>=checkRow) or (s[0][1]>=checkRow and s[0][1]-s[2]<=checkRow):
        y = abs(s[0][1]-checkRow)
        checkSet.update(list(range((s[0][0]-(s[2]-y)),s[0][0]+(s[2]-y)+1)))
#        print(y)
#        print(s)

for s in sensorList:
    if s[0][1] == checkRow: checkSet.discard(s[0][0])
    if s[1][1] == checkRow: checkSet.discard(s[1][0])

print(len(checkSet))


#print(sensorList)

