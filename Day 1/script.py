import array

input = open("input.txt","r")


lines = input.readlines()

elfindex=0

elffood = []

tempsum = 0

for line in lines:
    if line.strip():
        linevalue= int(line)
        if elfindex == 0:
            elffood.append(linevalue)
        else:
            tempsum = tempsum + linevalue
    else:
        elffood.append(tempsum)
        tempsum=0
        elfindex+=1
        
elffood.sort(reverse=True)

print(elffood)

sum = elffood[0] + elffood[1] + elffood[2]

print(str(sum))
