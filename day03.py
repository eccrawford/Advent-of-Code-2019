#Advent of Code 2019 - Day 3

#Part One
f = open('day03input.txt')

center = (0,0)

wiresPath = []
wire1coords = []
wire2coords = []
for line in f:
    wire = line.split(",")
    wiresPath.append(wire)


def listCoords(directions, coordList):
    xcounter = 0
    ycounter = 0
    for direction in directions:
        distance = int(direction[1:len(direction)])
        currentPos = (xcounter, ycounter)
        counter = 0
        if direction[0] == "U":
            while counter != distance:
                ycounter = ycounter + 1
                counter = counter + 1
                currentPos = (xcounter, ycounter)
                coordList.append(currentPos)
        elif direction[0] == "D":
            while abs(counter) != distance:
                ycounter = ycounter - 1
                counter = counter - 1
                currentPos = (xcounter, ycounter)
                coordList.append(currentPos)
        elif direction[0] == "R":
            while counter != distance:
                xcounter = xcounter + 1
                counter = counter + 1
                currentPos = (xcounter, ycounter)
                coordList.append(currentPos)
        elif direction[0] == "L":
            while abs(counter) != distance:
                xcounter = xcounter - 1
                counter = counter - 1
                currentPos = (xcounter, ycounter)
                coordList.append(currentPos)
    return coordList

coordList1 = listCoords(wiresPath[0],wire1coords)
coordList2 = listCoords(wiresPath[1], wire2coords)

wire1Path = set(coordList1)
wire2Path = set(coordList2)

if wire1Path & wire2Path:
    common = list(wire1Path & wire2Path)

def calculateManhattanDistance(commonList):
    mDistances = []
    for coord in commonList:
        mDistance = abs((center[0] - coord[0])) + abs((center[1] - coord[1]))
        mDistances.append(mDistance)
    return min(mDistances)

minmDist = calculateManhattanDistance(common)
print("min manhattan distance", minmDist)

#Part Two

def stepCounter(coords):
    stepsTracker = []
    for coord in coords:
        steps1 = coordList1.index(coord) + 1
        steps2 = coordList2.index((coord)) + 1
        totalSteps = steps1 + steps2
        stepsTracker.append(totalSteps)
    return min(stepsTracker)

print("min steps",stepCounter(common))