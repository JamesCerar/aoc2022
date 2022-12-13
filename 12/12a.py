import os
import numpy as np


debug = False
debugPart = 'a'

#open file, get values as list of integers
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')
if debug and debugPart.lower()=='a': filename = os.path.join(dir, 'input_debug_partA.txt')
if debug and debugPart.lower()=='b': filename = os.path.join(dir, 'input_debug_partB.txt')

with open(filename, "r") as o:
    #these letters eventually get turned into numbers - the S and E replacement turn them into 0 and 27 in that calculation
    inputList = [[*i.replace('\n','').replace('S','`').replace('E','{')] for i in list(map(str, o.readlines()))]

#turn letters into numbers
inputList = [[ord(i)-96 for i in j] for j in inputList]



#part A

#trying to make an Djikstra's algo here
heightMap = np.array(inputList)
tenativeMap = np.ones(heightMap.shape,dtype=int)*9999999
distanceMap = np.zeros(heightMap.shape, dtype=int)
startLoc = np.unravel_index(heightMap.argmin(), heightMap.shape)
endLoc = np.unravel_index(heightMap.argmax(), heightMap.shape)
tenativeMap[startLoc] = 0
shortestPath = {}
unvisited = set()
neighbours = [(0,1),(1,0),(0,-1),(-1,0)]

for r in range(0,len(heightMap)):
    for c in range(0,len(heightMap[r])):
        unvisited.add((r,c))


while len(unvisited) > 0:
    if startLoc in unvisited:
        #if first node, use start
        curNode = startLoc
    else:
        #if not first node, find the lowest tenative value unvisited node
        minTenative = np.inf
        for u in unvisited:
            if minTenative > tenativeMap[u[0],u[1]]:
                curNode = u
                minTenative = tenativeMap[u[0],u[1]]
    
    unvisited.remove(curNode)

    for n in neighbours:
        nLoc = (curNode[0]+n[0],curNode[1]+n[1])
        if not (nLoc[0] < 0 or nLoc[0] > len(tenativeMap)-1 or nLoc[1] < 0 or nLoc[1] > len(tenativeMap[0])-1):
            if heightMap[nLoc[0]][nLoc[1]] == heightMap[curNode[0]][curNode[1]] or heightMap[nLoc[0]][nLoc[1]] == heightMap[curNode[0]][curNode[1]] + 1 or heightMap[nLoc[0]][nLoc[1]] < heightMap[curNode[0]][curNode[1]]:
                tenativeMap[nLoc] = min(tenativeMap[curNode] + 1, tenativeMap[nLoc])

for i in tenativeMap:
    print(i)

print('')

for i in heightMap:
    print(i)

print(tenativeMap[endLoc])

