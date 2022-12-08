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

    if (firstAreaBeginning < secondAreaBeginning) and (firstAreaEnd >= secondAreaBeginning):
            count = count + 1
            continue
    if (firstAreaBeginning > secondAreaBeginning) and (secondAreaEnd >= firstAreaBeginning):
            count = count + 1
            continue
    if(firstAreaBeginning == secondAreaBeginning) or (firstAreaBeginning == secondAreaBeginning):
            count = count + 1
            continue        

print(str(count))
    
