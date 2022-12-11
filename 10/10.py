import os


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
targetCycles = [20,60,100,140,180,220]
registers = {0:1}
reg = 0
x = 1
for i in range(0,len(inputList)):
    reg += 1
    registers[reg] = x
    if inputList[i][0:4] == 'addx':
        reg += 1
        x += int(inputList[i][5:])
        registers[reg] = x

sigStrength = 0
for j in targetCycles:
    sigStrength += (registers[j-1]*j)
    print('j='+str(j)+'...sigStrength='+str(registers[j]))

print(sigStrength)

#part B
pixels = ['','','','','','']
for i in range(0,len(registers)-1):
    curVal = ' '
    spriteLoc = {registers[i]-1,registers[i],registers[i]+1}
    if {i%40}.intersection(spriteLoc) == {i%40}: curVal = '#'
    pixels[i//40] = pixels[i//40] + curVal

print('')
for p in pixels:
    print(p)
print('')

