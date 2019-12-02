#Advent of Code 2019 - Day 1


def calculateFuel(mass):
    fuel = (mass//3)-2
    return fuel

def fuelReq(): #part One
    file = open('day01input.txt')
    totalFuel = 0
    for f in file:
        totalFuel += calculateFuel(int(f))
    return totalFuel


def doubleChecker(): #part Two
    file = open('day01input.txt')
    totalFuel = 0
    startFuel = 0

    for f in file:
        startFuel = calculateFuel(int(f))
        while startFuel > 0:
            totalFuel += startFuel
            startFuel = calculateFuel(startFuel)
            if startFuel <= 0:
                break
        startFuel = 0
    return totalFuel


print(fuelReq())
print(doubleChecker())
