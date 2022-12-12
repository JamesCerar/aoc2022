import os
import re
import math


debug = False
debugPart = 'a'

#open file, get values as list of integers
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')
if debug and debugPart.lower()=='a': filename = os.path.join(dir, 'input_debug_partA.txt')
if debug and debugPart.lower()=='b': filename = os.path.join(dir, 'input_debug_partB.txt')

with open(filename, "r") as o:
    inputList = [i.replace('\n','') for i in list(map(str, o.readlines()))]


#part B

#build list of monkeys
monkeys = []
curMonkey = {'num':0, 'count':0}
for i in inputList[1:]:
    if re.search('Monkey (\d*):',i):
        monkeys.append(curMonkey)
        curMonkey = {'num':curMonkey['num']+1, 'count':0}
    
    if re.search('Starting items:',i):
        objs = [int(i) for i in re.findall('(\d+)+',i)]
        curMonkey['objs'] = objs
    
    if re.search('Operation:',i):
        calc = re.findall('(new = )(old|new|\d+) (\+|\*) (old|new|\d+)',i)[0]
        curMonkey['op'] = {'val1':calc[1],'opr':calc[2],'val2':calc[3]}

    if re.search('Test:',i):
        test = re.findall('(\d+)',i)[0]
        curMonkey['test'] = int(test)

    if re.search('If false:',i):
        ifFalse = re.findall('(\d+)',i)[0]
        curMonkey['ifFalse'] = int(ifFalse[0])

    if re.search('If true:',i):
        ifTrue = re.findall('(\d+)',i)[0]
        curMonkey['ifTrue'] = int(ifTrue[0])

monkeys.append(curMonkey)

#do the game
numRounds = 10000
lcm = math.prod([i['test'] for i in monkeys])

for r in range(0,numRounds):
    print('')
    print('Round: '+str(r))
    #print(monkeys)
    for m in range(0,len(monkeys)):
        #inspect each item
        for i in range(0,len(monkeys[m]['objs'])):
            monkeys[m]['count'] += 1
            curObj = monkeys[m]['objs'].pop(0)

            #do the calc to get new worry level, and then int divide by 3
            if monkeys[m]['op']['val2'] == 'old':
                val2 = curObj
            else:
                val2 = int(monkeys[m]['op']['val2'])
            
            if monkeys[m]['op']['opr'] == '+':
                curObj = (curObj + val2)
            elif monkeys[m]['op']['opr'] == '*':
                curObj = (curObj * val2)
            else:
                raise Exception('Operator Error!')
            
            curObj = curObj%lcm

            #do test to see who to throw to, and throw
            if int(curObj / monkeys[m]['test']) == curObj / monkeys[m]['test']:
                monkeys[monkeys[m]['ifTrue']]['objs'].append(curObj)
            else:
                monkeys[monkeys[m]['ifFalse']]['objs'].append(curObj)

monkeyBusiness = [m['count'] for m in monkeys]
monkeyBusiness.sort(reverse=True)

print(monkeyBusiness)

print(monkeyBusiness[0]*monkeyBusiness[1])