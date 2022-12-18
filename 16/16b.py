import os
import numpy as np
import itertools
import re

def cantBeatMax(curMove,maxMoves,curVal,curValveScore,maxVal,maxValveScore):
    #get maximum possible vals given current position
    #assume curMove gets maxVal for remainder of time - can they beat the actual maxVal?

    #return False

    numMoves = maxMoves - curMove + 1
    theorMax = maxVal + (maxValveScore*numMoves)
    thisMax = curVal + (curValveScore*numMoves)

    if theorMax > thisMax + 24:
        return True
    else:
        return False



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

valves, valveVals, goodValves = {}, {}, []
for i in inputList:
    x = re.findall('Valve (.+) has flow rate=(\d+); (?:tunnels lead to valves|tunnel leads to valve) (.+)',i)
    valves[x[0][0]] = x[0][2].replace(' ','').split(',')
    if int(x[0][1])>0: 
        valveVals[x[0][0]] = int(x[0][1])
        goodValves.append(x[0][0])

totalGoodValves = len(goodValves)
nextValves = {}
for a in valves:
    for b in valves:
        nextValves[(a,b)] = set()

for v in nextValves:
    for a in valves[v[0]]:
        for b in valves[v[1]]:
            p = [a,b]
            p.sort()
            nextValves[v].add(tuple(p))

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


paths = {(('AA','AA'),frozenset({})):0}
maxAchieved = False
for i in range(1,27):
    print(i)
    #print(len(paths))

    newPaths = {}

    #check if any paths have opened all paths
    if not maxAchieved:
        for p in paths:
            if len(p[1])==totalGoodValves:
                print('MAX ACHIEVED')
                maxAchieved = True
                break

    maxVal = max(paths.values())
    maxValveSet = max([valveComboVals[i[1]] for i in paths])
    maxValves = max([len(i[1]) for i in paths])
    print('Max valves:',maxValves, "out of total",totalGoodValves)
    print('Max valave set:',maxValveSet)
    print('NumPaths:',len(paths))

    for p in paths:
        #if i == 10 and p == (('CC','EE'),frozenset({'DD','JJ','BB','HH','CC'})):
        #    print('stop')
        #once a path has opened all valves, it's final value is known.
        #check if current path can theoretically beat that path's value - eliminate path if not
        #if maxAchieved and cantBeatMax(i,26,paths[p],maxVal,maxComboVal): 
        if cantBeatMax(i,26,paths[p],maxComboVal,maxVal,maxValveSet): 
            continue

        #if current path has opened all valves, no need for combination of new paths
        #add to new paths with same combo, updating value
        if len(p[1])==totalGoodValves:
            newPaths[p] = max(newPaths.get(p,0),paths[p]+maxComboVal)
            continue

        valveA = p[0][0]
        valveB = p[0][1]

        #if current valve A is good and not currently open, open it
        if valveA not in p[1] and valveA in goodValves:
            newOpenValves = frozenset(p[1].union({valveA}))
            for v in valves[valveB]:
                newPath = [valveA, v]
                newPath.sort()
                newPaths[(tuple(newPath),newOpenValves)] = max(newPaths.get((tuple(newPath),newOpenValves),0),paths[p]+valveComboVals[p[1]])
        

        #if current valve B is good and not currently open, open it
        if valveB not in p[1] and valveB in goodValves:
            newOpenValves = frozenset(p[1].union({valveB}))
            for v in valves[valveA]:
                newPath = [valveB, v]
                newPath.sort()
                newPaths[(tuple(newPath),newOpenValves)] = max(newPaths.get((tuple(newPath),newOpenValves),0),paths[p]+valveComboVals[p[1]])


        #if both current valves are good and not currently open, open them
        if (valveA not in p[1] and valveA in goodValves) and (valveB not in p[1] and valveB in goodValves) and valveA != valveB:
            newOpenValves = frozenset(p[1].union({valveA}).union({valveB}))
            newPaths[(p[0],newOpenValves)] = max(newPaths.get((p[0],newOpenValves),0),paths[p]+valveComboVals[p[1]])

        #add any potential new paths:
        for nv in nextValves[p[0]]:
            newPaths[(nv,p[1])] = max(newPaths.get((nv,p[1]),0),paths[p]+valveComboVals[p[1]])

    paths = {}
    paths = newPaths.copy()


        
maxTotal = 0
for p in paths:
    maxTotal = max(maxTotal,paths[p])

print(maxTotal)