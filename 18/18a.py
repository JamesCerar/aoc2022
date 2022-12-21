import os
import numpy as np
import itertools

def ranges(k):
    for a, b in itertools.groupby(enumerate(k), lambda pair: pair[1] - pair[0]):
        b = list(b)
        yield b[0][1], b[-1][1]

debug = True
debugPart = 'a'
if debug:
    numShapes = 2022
else:
    numShapes = 2022

#open file, get values as list of integers
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')
if debug and debugPart.lower()=='a': filename = os.path.join(dir, 'input_debug_partA.txt')
if debug and debugPart.lower()=='b': filename = os.path.join(dir, 'input_debug_partB.txt')

with open(filename, "r") as o:
    #these letters eventually get turned into numbers - the S and E replacement turn them into 0 and 27 in that calculation
    inputList = [i.replace('\n','').split(',') for i in list(map(str, o.readlines()))]
    #inputList = o.readlines()[0]

cubeCoords = []
for i in inputList:
    curRow = []
    for j in i:
        curRow.append(int(j))
    cubeCoords.append(curRow)
    
cubeDict = {1:{},2:{},3:{}}

for d in [1,2,3]:
    otherDims = {1:(0,1),2:(-2,0),3:(-3,-2)}
    for i in cubeCoords:
        #print(cubeDict[d].get((i[d+otherDims[d][0]],i[d+otherDims[d][1]]),[]))
        #print((i[d+otherDims[d][0]],i[d+otherDims[d][1]]))
        curList = cubeDict[d].get((i[d+otherDims[d][0]],i[d+otherDims[d][1]]),[])
        curList.append(i[d-1])
        cubeDict[d][(i[d+otherDims[d][0]],i[d+otherDims[d][1]])] = curList

totalFaces = 0
for i in cubeDict:
    for j in cubeDict[i]:
        cubeDict[i][j].sort()
        t = list(ranges(cubeDict[i][j]))
        print(i,j)
        print(t)
        totalFaces += len(t)*2
print(totalFaces)