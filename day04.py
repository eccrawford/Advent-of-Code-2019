#Advent of Code 2019 - Day 4


start = 382345
end = 843167

def checker(s, e):
    validPasswords = 0
    for num in range(s, e+1):
        string = str(num)

        doubleAndIncreasing = checkDouble(string)

        if doubleAndIncreasing:
            validPasswords = validPasswords + 1

    return validPasswords


def checkIncreasing(string):
    increasing = True
    i = 0
    while i != len(string)-1 and increasing == True:
        if string[i] <= string[i+1]:
            i = i + 1
        else:
            increasing = False
    return increasing

def checkDouble(string):
    double = False
    i = 0
    
    increasing = checkIncreasing(string)

    if increasing:
        for char in string:
            if string.count(char) == 2: #Part 2, for Part 1 change == to >=
                double = True
    return double


print(checker(start,end))           
        
    
