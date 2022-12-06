import os
import re

def getInput():

    #open file, get values as list of integers
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'input.txt')


    debug = False

    with open(filename, "r") as o:
        inputList = [i.replace('\n','').split(",") for i in list(map(str, o.readlines()))]

    if debug:
        inputList = [
    ['    [D]    '],
    ['[N] [C]    '],
    ['[Z] [M] [P]'],
    [' 1   2   3 '],
    [''],
    ['move 1 from 2 to 1'],
    ['move 3 from 1 to 3'],
    ['move 2 from 2 to 1'],
    ['move 1 from 1 to 2]']
    ]

    print(inputList)


    #make input useful
    stacks, instructions = [], []
    isInstructions = False

    for i in inputList:
        if i[0] == '':
            isInstructions = True
        elif isInstructions:
            instructions.append(i)
        else:
            stacks.append(i)
    stacks = stacks[:-1]
    #do stacks - goal is to get a dict with keys = stacks, and values = list of letters
    stackDict = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}

    if debug:
        stackDict = {1:[],2:[],3:[]}

    for i in reversed(range(0,len(stacks))):
        curLine = stacks[i][0] + ' '
        print(str(len(curLine)))
        leng=10
        if debug: leng=4
        for s in range(1,leng):
            curLet = curLine[(s-1)*4+1:(s-1)*4+2]
            if curLet != ' ':
                stackDict[s].append(curLet)

    return stackDict, instructions

#part A

stackDict, instructions = getInput()
for i in instructions:
    iMatch = re.search('move (\d*) from (\d*) to (\d*)',i[0])
    moveNum = int(iMatch.group(1))
    moveFrom = int(iMatch.group(2))
    moveTo = int(iMatch.group(3))
    
    for j in range(0,moveNum):
        moveString = stackDict[moveFrom][-1:]
        stackDict[moveFrom] = stackDict[moveFrom][:-1]
        #output = stackDict[moveTo]
        stackDict[moveTo].append(moveString[0])

    for j in stackDict:
        if '' in stackDict[j]:
            print(j)

outputStr = ''
for i in stackDict:
    outputStr = outputStr + stackDict[i][-1:][0]

print('part A:')
print(outputStr)



#part B
stackDict, instructions = getInput()
print(stackDict)

for i in instructions:
    iMatch = re.search('move (\d*) from (\d*) to (\d*)',i[0])
    moveNum = int(iMatch.group(1))*-1
    moveFrom = int(iMatch.group(2))
    moveTo = int(iMatch.group(3))
    
    moveString = stackDict[moveFrom][moveNum:]
    stackDict[moveFrom] = stackDict[moveFrom][:moveNum]
    #output = stackDict[moveTo]
    stackDict[moveTo].extend(moveString)
    print(stackDict)
    print('next')

outputStr = ''
for i in stackDict:
    outputStr = outputStr + stackDict[i][-1:][0]

print(outputStr)
print(stackDict)