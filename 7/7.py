import os


debug = False

#open file, get values as list of integers
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')
if debug: filename = os.path.join(dir, 'input_debug.txt')

with open(filename, "r") as o:
    inputList = [i.replace('\n','') for i in list(map(str, o.readlines()))]

#part A

inputList = inputList[1:] #remove base location

valDict = {'/':{'level':0,'size':0,'parent':''}}
curLevel = 1
curParent = '/'
for i in inputList:
    if i in ['$ ls']:
        continue
    elif i == '$ cd ..':
        curParent = valDict[curParent]['parent']
        curLevel -= 1
    elif i[0:4] == '$ cd':
        curParent = curParent + '/' + i[5:]
        curLevel = valDict[curParent]['level'] + 1
    elif i[0:3] == 'dir':
        curDir = curParent + '/' + i[4:]
        valDict[curDir] = {'level':curLevel,'size':0,'parent':curParent}
    else:
        size = int(i.split(' ')[0])
        valDict[curParent]['size'] += size

maxDepth = max(int(d['level']) for d in valDict.values())


for i in reversed(range(1,maxDepth+1)):
    for key in valDict:
        if valDict[key]['level'] == i:
            valDict[valDict[key]['parent']]['size']+=valDict[key]['size']

totalSum = 0
for key in valDict:
    if valDict[key]['size'] <= 100000: totalSum+=valDict[key]['size']

if debug: print(valDict)
print('total small dirs:')
print(totalSum)

#part B
reqSpace = 30000000 - (70000000 - valDict['/']['size'])

print("space req'd to be deleted:")
print(reqSpace)

bestDel = ['',-99999999999]

vals = [valDict[i]['size'] for i in valDict]
vals.sort()

for i in valDict:
    if reqSpace - valDict[i]['size'] <= 0 and reqSpace - valDict[i]['size'] > bestDel[1]:
        bestDel = [i,reqSpace - valDict[i]['size'],valDict[i]['size']]

print('dir to delete')
print(bestDel)