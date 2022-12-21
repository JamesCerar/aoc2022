import os
import numpy as np
import itertools

def ranges(k):
    for a, b in itertools.groupby(enumerate(k), lambda pair: pair[1] - pair[0]):
        b = list(b)
        yield b[0][1], b[-1][1]

debug = False
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

maxX = max([int(i[0]) for i in inputList])+3 #not one, not two, but three!
maxY = max([int(i[1]) for i in inputList])+3 #three because there's 0 indexing (so max = max number + 1)
maxZ = max([int(i[2]) for i in inputList])+3 #and because we need buffers on both sides of each axis
minX = min([int(i[0]) for i in inputList])
minY = min([int(i[1]) for i in inputList])
minZ = min([int(i[2]) for i in inputList])


cubeArr = np.zeros((maxX,maxY,maxZ),dtype=int)

cubeCoords = []
for i in inputList:
    cubeArr[int(i[0])+1][int(i[1])+1][int(i[2])+1] = 1
    curRow = []
    for j in i:
        curRow.append(int(j))
    cubeCoords.append(curRow)


voidNum = 2
uncheckedSet = set()
for i in range(len(cubeArr)):
    for j in range(len(cubeArr[i])):
        for k in range(len(cubeArr[i][j])):
            if cubeArr[i][j][k] == 0: uncheckedSet.add((i,j,k))


neighbourIndex = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
checkSet = {(0,0,0)}
outerSet = {(0,0,0)}
doneSet = {(0,0,0)}
while checkSet:
    c = checkSet.pop()
    outerSet.add(c)
    for n in neighbourIndex:
        x,y,z = c[0]+n[0],c[1]+n[1],c[2]+n[2]
        #if (x,y,z) == (1,1,0):
        #    print('stop')
        if x < len(cubeArr) and y < len(cubeArr[0]) and z < len(cubeArr[0][0]) and x >= 0 and y >= 0 and z >= 0 and cubeArr[x][y][z] == 0 and (x,y,z) not in doneSet:
            doneSet.add((x,y,z))
            checkSet.add((c[0]+n[0],c[1]+n[1],c[2]+n[2]))

cubeDict = {1:{},2:{},3:{}}

# for x in range(maxX):
#     for y in range(maxY):
#         outerSet.add((x,y,-1))
#         outerSet.add((x,y,maxZ))

# for x in range(maxX):
#     for z in range(maxZ):
#         outerSet.add((x,-1,z))
#         outerSet.add((x,maxY,z))

# for y in range(maxY):
#     for z in range(maxZ):
#         outerSet.add((-1,y,z))
#         outerSet.add((maxX,y,z))

for d in [1,2,3]:
    otherDims = {1:(0,1),2:(-2,0),3:(-3,-2)}
    for i in outerSet:
        #print(cubeDict[d].get((i[d+otherDims[d][0]],i[d+otherDims[d][1]]),[]))
        #print((i[d+otherDims[d][0]],i[d+otherDims[d][1]]))
        curList = cubeDict[d].get((i[d+otherDims[d][0]],i[d+otherDims[d][1]]),[])
        curList.append(i[d-1])
        cubeDict[d][(i[d+otherDims[d][0]],i[d+otherDims[d][1]])] = curList

print(outerSet)

totalFaces = 0
for i in cubeDict:
    for j in cubeDict[i]:
        cubeDict[i][j].sort()
        t = list(ranges(cubeDict[i][j]))
        print(t,'numFaces:',(len(t)-1)*2,"i=",i,"j=",j)
        totalFaces += (len(t)-1)*2

print(totalFaces)
print(cubeArr)