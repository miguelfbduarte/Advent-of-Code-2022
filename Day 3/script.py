import string

input = open("C:\Advent of code\Day 3\input.txt","r")


lines = input.readlines()

repeatedletters = []

for line in lines:
    index=0
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    a=list(set(firstpart)&set(secondpart))
    repeatedletters.append(a[0])
    print(a[0])

values = dict()

for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index + 1


for index, letter in enumerate(string.ascii_uppercase):
    values[letter] = index + 27



totalvalue=0

for letter in repeatedletters:
    totalvalue = totalvalue + values[letter]
    
print(totalvalue)