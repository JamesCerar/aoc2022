import os
import numpy as np
import itertools
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

valves, valveVals, goodValves = {}, {}, []
for i in inputList:
    x = re.findall('Valve (.+) has flow rate=(\d+); (?:tunnels lead to valves|tunnel leads to valve) (.+)',i)
    valves[x[0][0]] = x[0][2].replace(' ','').split(',')
    if int(x[0][1])>0: 
        valveVals[x[0][0]] = int(x[0][1])
        goodValves.append(x[0][0])

valveComboVals = {}
for L in range(len(goodValves) + 1):
    for subset in itertools.combinations(goodValves, L):
        curVal = 0
        for s in subset:
            curVal += valveVals[s]
        x = list(subset)
        x.sort()
        valveComboVals[tuple(x)] = curVal

print(valveComboVals)

paths = {}
paths[('AA',tuple())]=0

for i in range(0,30):
    print(i)
    print(len(paths))
    newPaths = {}
    for p in paths:
        #for new paths
        for v in valves[p[0]]:
            #newPaths[(valve,(valveList))] = max(newPaths[(valve,(valveList))], paths[p] + valveComboVals)
            newPaths[(v,p[1])] = max(newPaths.get((v,p[1]),0),paths[p] + valveComboVals[p[1]])

        if p[0] in valveVals and p[0] not in p[1]: 
            newValveSet = list((*p[1],p[0]))
            newValveSet.sort()
            newPaths[(p[0],tuple(newValveSet))] = max(newPaths.get((p[0],tuple(newValveSet)),0),paths[p] + valveComboVals[p[1]])
        

    paths = {}
    paths = newPaths.copy()
        
maxTotal = 0
for p in paths:
    maxTotal = max(maxTotal,paths[p])

print(maxTotal)