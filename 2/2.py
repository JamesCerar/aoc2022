import os

##Part A##

#open file, get values as list of integers
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')


with open(filename, "r") as o:
    #inputList = [i.split() for i in list(map(str, o.readlines()))]
    inputList = [i.strip() for i in list(map(str, o.readlines()))]

#inputList = ['A Z','B Y','C X']
# A Z = 3, B Y = 5, C X = 7

print(inputList)

#part A
#X = Rock, 1pt. Y = Paper, 2pt. Z = Scissors, 3pt.
#A = Rock, B = Paper, C = Scissors
pointsDict = {'A X':4,'B X':1,'C X':7,'A Y':8,'B Y':5,'C Y':2,'A Z':3,'B Z':9,'C Z':6}
pointsList = [pointsDict[i] for i in inputList]
totalPoints = sum(pointsList)
print(totalPoints)


#part B
#x=lose, y=draw, z=win
replaceDict = {'A X':'A Z','B X':'B X','C X':'C Y','A Y':'A X','B Y':'B Y','C Y':'C Z','A Z':'A Y','B Z':'B Z','C Z':'C X'}
inputList = [replaceDict[i] for i in inputList]
pointsList = [pointsDict[i] for i in inputList]
totalPoints = sum(pointsList)
print(totalPoints)