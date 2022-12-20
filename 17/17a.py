import os
import numpy as np

class shape:

    def __init__(self,shape):
        shapes = {'-':{'coords':[(2,0),(3,0),(4,0),(5,0)],'width':4,'height':1},
              '+':{'coords':[(3,2),(2,1),(3,1),(4,1),(3,0)],'width':3,'height':3},
              'J':{'coords':[(2,2),(3,2),(4,2),(4,1),(4,0)],'width':3,'height':3},
              'I':{'coords':[(2,3),(2,2),(2,1),(2,0)],'width':1,'height':4},
              'O':{'coords':[(2,1),(3,1),(2,0),(3,0)],'width':2,'height':2}  
                }
    
        self.shape = shape
        self.coords = shapes[self.shape]['coords']
        self.width = shapes[self.shape]['width']
        self.height = shapes[self.shape]['height']
    
    def print_shape(shape):
        strOut = ''
        for r in range(shape.height):
            for c in range(shape.width):
                nextChar = ' '
                for s in shape.coords:
                    if r + shape.height - 1 == s[1] and c + shape.width - 1 == s[0]:
                        nextChar = '#'
                        break
                strOut = strOut + nextChar
            strOur = strOut + '\n'
        
        return 
    
    def move_shape(self, dir):
        dirs = {'<':(-1,0),'>':(1,0),'d':(0,1)}
        coords = [tuple(np.add(i,dirs[dir])) for i in self.coords]
        return coords

class chamber:
    def __init__(self, shape=(3,7)):
        self.chamber = np.zeros(shape, dtype='str')
        self.width = shape[1]
        self.height = shape[0]
    

    def add_rows(self, numRows):
        newArr = np.zeros((numRows,self.chamber.shape[1]),dtype=str)
        self.chamber = np.vstack([newArr,self.chamber])
    
    def validate_move(self, coords):
        for i in coords:
            if i[0] < 0 or i[0] > 6: return False
            if i[1] > len(self.chamber)-1: return False

        curNum = np.count_nonzero(self.chamber) + len(coords)
        curArr = self.chamber.copy()

        for i in coords:
            curArr[i[1]][i[0]] = '#'

        if np.count_nonzero(curArr) == curNum:
            return True
        else:
            return False

    def add_shape(self,coords):
        for i in coords:
            self.chamber[i[1]][i[0]] = '#'
        self.trim()
        return

    def trim(self):
        x = 0
        while True:
            if np.count_nonzero(self.chamber[x]) > 0:
                self.chamber = self.chamber[x:]
                return
            x += 1
    
    def print_chamber(self):
        chamberStr = ''
        for i in range(0,len(self.chamber)):
            curRow = ''
            for j in self.chamber[i]:
                if j == '': 
                    curRow = curRow + '.'
                else:
                    curRow = curRow + j
            chamberStr = chamberStr + curRow
            if i<len(self.chamber)-1: chamberStr = chamberStr + '\n'
        
        return chamberStr



debug = False
debugPart = 'a'
if debug:
    numShapes = 2022
else:
    numShapes = 2022

#open file, get values as list of integers
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')
if debug and debugPart.lower()=='a': filename = os.path.join(dir, 'input_debug_partA.txt')
if debug and debugPart.lower()=='b': filename = os.path.join(dir, 'input_debug_partB.txt')

with open(filename, "r") as o:
    #these letters eventually get turned into numbers - the S and E replacement turn them into 0 and 27 in that calculation
    #inputList = [i.replace('\n','') for i in list(map(str, o.readlines()))]
    inputList = o.readlines()[0]

shapeList = ['-','+','J','I','O']
windIndex = 0

c = chamber()

for i in range(0,numShapes):
    curShape = shapeList[i%5]
    s = shape(curShape)
    if i>0: c.add_rows(3)
    c.add_rows(s.height)
    floating = True
    while floating:
        #move direction of wind if possible
        curWind = inputList[windIndex%len(inputList)]
        windIndex += 1

        newCoords = s.move_shape(curWind)
        if c.validate_move(newCoords):
            s.coords = newCoords

        #move down if possible
        newCoords = s.move_shape('d')
        if c.validate_move(newCoords):
            s.coords = newCoords
        else:
            c.add_shape(s.coords)
            floating = False
    if debug:
        print('Drop:',i)
        print(c.print_chamber())
        print('')

c.trim()
print(len(c.chamber))