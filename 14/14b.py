import os
import numpy as np
import re

def PrintSpace(space):
    print('~~~~~~~~~~~~~~~~~~')
    with open('output.txt','w') as o:
        for i in space:
            curLine = ''
            for j in i:
                if j == '':
                    curLine = curLine + ' '
                else:
                    curLine = curLine + str(j)
            print(curLine)
            o.write(curLine+'\n')
    print('~~~~~~~~~~~~~~~~~~')

def DrawLine(start,end):
    line = []
    vertical = start[0] == end[0]

    if vertical:
        for i in range(0,max(start[1],end[1])-min(start[1],end[1])+1):
            line.append((start[0],min(start[1],end[1])+i))
    else:
        for i in range(0,max(start[0],end[0])-min(start[0],end[0])+1):
            line.append((min(start[0],end[0])+i,start[1]))

    return line

def GetRestingSpot(space,loc):
    curCol = space[loc[1]:,loc[0]]
    nextObj = np.nonzero(curCol)[0]
    if len(nextObj) == 0:
        return (-999,-999)
    else:
        restingSpot = (loc[0],loc[1]+nextObj[0]-1)
        if space[restingSpot[1]+1][restingSpot[0]-1]=='':
            return GetRestingSpot(space,(restingSpot[0]-1,restingSpot[1]+1))
        elif space[restingSpot[1]+1][restingSpot[0]+1]=='':
            return GetRestingSpot(space,(restingSpot[0]+1,restingSpot[1]+1))
        else:
            return restingSpot

    


debug = False
debugPart = 'a'

#open file, get values as list of integers
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')
if debug and debugPart.lower()=='a': filename = os.path.join(dir, 'input_debug_partA.txt')
if debug and debugPart.lower()=='b': filename = os.path.join(dir, 'input_debug_partB.txt')

with open(filename, "r") as o:
    #these letters eventually get turned into numbers - the S and E replacement turn them into 0 and 27 in that calculation
    inputList = [i.replace('\n','') for i in list(map(str, o.readlines()))]

lines = []
maxX, maxY, minX, minY = 0,0,9999,9999
for i in inputList:
    curLine = []
    for j in re.findall('(\d+,\d+)',i):
        curLine.append((int(j[:3]),int(j[4:])))
        maxX = max(maxX,int(j[:3])+5)
        maxY = max(maxY,int(j[4:])+5)
        minX = min(minX,int(j[:3])-5)
        minY = min(minY,int(j[4:])-5)
    lines.append(curLine)
lines.append([(1,maxY-3),(999,maxY-3)])
minX = 0
maxX = 1000

space = np.zeros((maxY+1,maxX-minX),dtype='str')


for l in lines:
    for v in range(1,len(l)):
        for n in DrawLine(l[v-1],l[v]):
            space[n[1]][n[0]-minX] = '#'

PrintSpace(space)
iters = 0

while True:
    iters += 1
    if iters >= 100000000: break
    curSand = (500,0)
    newLoc = GetRestingSpot(space,curSand)
    if newLoc == (-999,-999): break
    if space[0][500-minX] == 'O': break
    space[newLoc[1],newLoc[0]] = 'O'

PrintSpace(space)
print(iters-1)