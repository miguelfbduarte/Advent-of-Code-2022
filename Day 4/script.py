with open("C:\Advent of code\Day 4\input.txt","r") as f:
    allLines = f.read().splitlines()

count = 0

for singleLine in allLines:
    separatedLine = singleLine.split(',')
    
    firstArea = separatedLine[0].split('-')
    
    firstAreaBeginning = int(firstArea[0])
    firstAreaEnd = int(firstArea[1])

    secondArea = separatedLine[1].split('-')
    
    secondAreaBeginning = int(secondArea[0])
    secondAreaEnd = int(secondArea[1])

    #print(firstAreaBeginning)
    #print(firstAreaEnd)
    #print(secondAreaBeginning)
    #print(secondAreaEnd)

    if firstAreaBeginning <= secondAreaBeginning:
        if firstAreaEnd >= secondAreaEnd:
            count = count + 1
            continue
    if secondAreaBeginning <= firstAreaBeginning:
        if secondAreaEnd >= firstAreaEnd:
            count = count + 1
            continue
            

print(str(count))
    



    