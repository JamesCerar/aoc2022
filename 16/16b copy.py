import os
import numpy as np
import itertools
import re

def canBeatMax(curMove,maxMoves,curVal,maxVal,maxCombo):
    #get maximum possible vals given current position
    #assume curMove gets maxVal for remainder of time - can they beat the actual maxVal?

    return True

debug = True
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

valves, valveVals, goodValves = {}, {}, []
for i in inputList:
    x = re.findall('Valve (.+) has flow rate=(\d+); (?:tunnels lead to valves|tunnel leads to valve) (.+)',i)
    valves[x[0][0]] = x[0][2].replace(' ','').split(',')
    if int(x[0][1])>0: 
        valveVals[x[0][0]] = int(x[0][1])
        goodValves.append(x[0][0])

doubleValves = {}
totalGoodValves = len(goodValves)
for i in valves:
    for j in valves:
        doubleValves[frozenset({i,j})] = []

for i in doubleValves:
    curVal = set()
    for v in valves[i]:
        for w in valves[i[1]]:
            curVal.add(frozenset({v,w}))
    doubleValves[i] = frozenset(y)

    
print(doubleValves)

valveComboVals = {}
maxComboVal = 0
for L in range(len(goodValves) + 1):
    for subset in itertools.combinations(goodValves, L):
        curVal = 0
        for s in subset:
            curVal += valveVals[s]
        x = frozenset(subset)
        valveComboVals[x] = curVal
        maxComboVal = max(maxComboVal, curVal)

print(valveComboVals)

paths = {}
paths[(('AA','AA'),frozenset({}))]=0
allValvesAchieved = False

for i in range(0,26):
    print(i)
    print(len(paths))
    newPaths = {}
    for p in paths:
        if len(p[1]) == totalGoodValves:
            newPaths[p] = max(newPaths.get(p,0),paths[p] + valveComboVals[p[1]])
            allValvesAchieved = True
            continue
        

        #for new paths
        for v in doubleValves[p[0]]:
            #newPaths[(valve,(valveList))] = max(newPaths[(valve,(valveList))], paths[p] + valveComboVals)
            newPaths[(v,p[1])] = max(newPaths.get((v,p[1]),0),paths[p] + valveComboVals[p[1]])

        #if current valve 1 is not open and >0:
        if p[0][0] in valveVals and p[0][0] not in p[1]: 

            #add valve to open valves list
            newValveSet = frozenset({p[1].union({p[0][0]})})

            #for all valves the second valve can visit:
            for j in valves[p[0][1]]:
                newValves = frozenset({p[0][0],j})
                newPaths[newValves,newValveSet] = max(newPaths.get((newValves,newValveSet),0),paths[p] + valveComboVals[p[1]])
        
        if p[0][1] in valveVals and p[0][1] not in p[1]: 
            newValveSet = frozenset({*p[1],p[0][1]})
            for j in valves[p[0][0]]:
                newValves = frozenset({p[0][1].union(j)})
                newPaths[newValves,newValveSet] = max(newPaths.get((newValves,newValveSet),0),paths[p] + valveComboVals[p[1]])
    paths = {}
    paths = newPaths.copy()

    if allValvesAchieved:
        continue
        
maxTotal = 0
for p in paths:
    maxTotal = max(maxTotal,paths[p])

print(maxTotal)