import string

input = open("C:\Advent of code\Day 3\input.txt","r")

alllines = input.readlines()

lines_grouped = []

all_chars = []

start = 0
end = len(alllines)
step = 3
for i in range(start, end, step):
    x = i
    lines_grouped.append(alllines[x:x+step])

for lines in lines_grouped:
    repeatedchar=list(set(lines[0])&set(lines[1])&set(lines[2]))
    if '\n' in repeatedchar:
        repeatedchar.remove('\n')
    print(repeatedchar)
    all_chars.append(repeatedchar)

print(len(all_chars))

values = dict()

for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index + 1


for index, letter in enumerate(string.ascii_uppercase):
    values[letter] = index + 27

totalvalue=0

for letter in all_chars:
    totalvalue = totalvalue + values[letter[0]]
    
print(totalvalue)