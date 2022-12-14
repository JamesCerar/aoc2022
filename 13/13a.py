import os
import json

def compareSides(upper,lower):
    #both ints:
    if type(upper) is int and type(lower) is int:
        if upper == lower:
            return 'next'
        elif upper < lower:
            return 'correct'
        else:
            return 'incorrect'

    #one int one list:
    if type(upper) is int:
        upper = [upper]
    
    if type(lower) is int:
        lower = [lower]
    
    #both lists:
    maxLen = max(len(upper),len(lower))
    for i in range(0,maxLen):
        if len(upper) == i: return 'correct'
        if len(lower) == i: return 'incorrect'
        test = compareSides(upper[i],lower[i])
        if test == 'next':
            continue
        else:
            return test
    return 'next'

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

pairsList = []
curPair = []
for i in inputList:
    if i == '':
        pairsList.append(curPair)
        curPair = []
    else:
        curPair.append(json.loads(i))

totalCorrect = 0
for i in range(0,len(pairsList)):
    print('')
    print('next pair:')
    print(pairsList[i])
    test = compareSides(pairsList[i][0],pairsList[i][1])
    if test == 'correct':
        totalCorrect += i+1
    print(test)

print(totalCorrect)