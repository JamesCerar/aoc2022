import os
import numpy as np

def drawArray(curLocs):
    maxX,minX,maxY,minY = 0,0,0,0
    for l in curLocs:
        maxX = max(maxX,l[0])
        minX = min(minX,l[0])
        maxY = max(maxY,l[1])
        minY = min(minY,l[1])
    lenX = maxX-minX+1
    lenY = maxY-minY+1
    curArr = np.zeros((lenY,lenX),dtype=int)
    for x in range(0,len(curLocs)):
        curArr[curLocs[x][1]+minY,curLocs[x][0]+minX] = x+1
    np.flip(curArr,0)
    print(curArr)

debug = False
debugPart = 'b'

#open file, get values as list of integers
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')
if debug and debugPart.lower()=='a': filename = os.path.join(dir, 'input_debug_partA.txt')
if debug and debugPart.lower()=='b': filename = os.path.join(dir, 'input_debug_partB.txt')

with open(filename, "r") as o:
    inputList = [i.replace('\n','') for i in list(map(str, o.readlines()))]


#part A
curLocH = (0,0)
curLocT = (0,0)
tailLocs = set()
tailLocs.add(curLocT)
dirDict = {'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}
for i in inputList:
    direction = dirDict[i[0:1]]
    distance = int(i[2:])
    for j in range(0,distance):
        curLocH = (curLocH[0]+direction[0],curLocH[1]+direction[1])
        if abs(curLocH[0]-curLocT[0]) > 1 or abs(curLocH[1]-curLocT[1]) > 1:
            curLocT = (curLocH[0]-direction[0],curLocH[1]-direction[1])
            tailLocs.add(curLocT)
        #if debug:print("Head: "+str(curLocH)+"... Tail: "+str(curLocT))
#print(len(tailLocs))


#part B
curLocs = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
tailLocs = set()
tailLocs.add(curLocs[9])
for i in inputList:
    if debug: print(i)
    direction = dirDict[i[0:1]]
    distance = int(i[2:])
    for j in range(0,distance):
        curLocs[0] = (curLocs[0][0]+direction[0],curLocs[0][1]+direction[1])
        for n in range(1,10):
            deltaX,deltaY = curLocs[n-1][0]-curLocs[n][0], curLocs[n-1][1]-curLocs[n][1]
            dirX,dirY = np.sign(deltaX),np.sign(deltaY)

            if abs(deltaX) > 1 or abs(deltaY) > 1:
                curLocs[n] = (curLocs[n][0]+(dirX),curLocs[n][1]+(dirY))
            
        
            
        tailLocs.add(curLocs[9])
        if debug:
            print("Head: "+str(curLocs[0])+"... Tail: "+str(curLocs[9]))
            drawArray(curLocs)
            
print(len(tailLocs))