import array

input = open("C:\Advent of code\Day 2\input.txt","r")


lines = input.readlines()

elfpoints=0
mypoints=0

for line in lines:
    match line[0]:
        case "A":
            match line[2]:
                case "X":
                    mypoints = mypoints + 4
                case "Y":
                    mypoints = mypoints + 8
                case "Z":
                    mypoints = mypoints + 3
        case "B":
            match line[2]:
                case "X":
                    mypoints = mypoints + 1
                case "Y": 
                    mypoints = mypoints + 5
                case "Z":
                    mypoints = mypoints + 9
        case "C":
            match line[2]:
                case "X":
                    mypoints = mypoints + 7
                case "Y":
                    mypoints = mypoints + 2
                case "Z":
                    mypoints = mypoints + 6

print(str(mypoints))
