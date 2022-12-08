import os
import numpy as np


debug = False

#open file, get values as list of integers
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')
if debug: filename = os.path.join(dir, 'input_debug.txt')

with open(filename, "r") as o:
    heightArray = np.array([[*i.replace('\n','')] for i in list(map(str, o.readlines()))], dtype=int)


#part A

#create tree array
arraySize = heightArray.shape
visArray = np.zeros((arraySize),dtype=bool)
visArray[0] = 1
visArray[-1] = 1
visArray[:,0] = 1
visArray[:,-1] = 1
transposed = False

#directions is a list of directions to follow, representing a move along a column or row, and from which direction
#(x=[bool],y=[bool]) where x = transposed (ie, travel in x or y direction),
# and y = reversed (ie, travel from top vs bottom / left vs right)
directions = [(False,False,1),(True,False,1),(False,True,-1),(True,True,-1)]

for d in directions:
    #transpose so that we always look at rows in array
    if d[0] != transposed: 
        heightArray = np.transpose(heightArray)
        visArray = np.transpose(visArray)
        transposed = d[0]
    
    arrShape = heightArray.shape

    #set range based on direction
    if d[1]:
        cols = range(arrShape[1]-2,0,-1)
    else:
        cols = range(1,arrShape[1]-1)

    for r in range(0,arrShape[0]):
        localMax = heightArray[r][cols[0] - d[2]]
        for c in cols:
            if heightArray[r][c] > localMax:
                visArray[r][c] = True
                localMax = heightArray[r][c]


if transposed:
    visArray = np.transpose(visArray)
    heightArray = np.transpose(heightArray)

totalVis = sum(sum(visArray))

print(totalVis)

#part B

#directions is tuple of values
#(y,x,z) where y = index of movement in y direction (ie, up/down)
# x = index of movement in x direction (ie, left/right)
# z = curCellVal index
directions = [(1,0,0),(0,1,1),(-1,0,2),(0,-1,3)]
maxX, maxY = arraySize[1]-1, arraySize[0]-1

scoreArray = np.zeros(arraySize, dtype=int)


for r in range(0,maxY):
    for c in range(0,maxX):
        curCellVal = [0,0,0,0]
        for d in directions:
            curIndex = (r,c)
            curVal = 0
            curHeight = heightArray[r][c]
            while True:
                curIndex = (curIndex[0] + d[0], curIndex[1] + d[1])
                #is there anything beside me? If no, then 0 and next direction
                if curIndex[0] < 0 or curIndex[0] > maxY or curIndex[1] < 0 or curIndex[1] > maxX: break

                curVal += 1

                if heightArray[curIndex[0]][curIndex[1]] >= curHeight: break
            
            curCellVal[d[2]] = curVal

        scoreArray[r,c] = np.prod(curCellVal)


maxVis = np.amax(scoreArray)

print(maxVis)