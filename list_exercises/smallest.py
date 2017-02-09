numbers = raw_input("Give me some numbers! I'll find the lowest!")
currentLowest = 9
lowest = (currentLowest * 0) + currentLowest

for x in range(len(numbers)):
    if numbers[x: + 1] == 0:
        print 0
    else:
        for y in range(len(numbers)):
            if numbers[x: x + 1] < numbers[x + 1: x + 2]:
                currentLowest = numbers[x: x + 1]
                lowest = currentLowest
                if currentLowest < lowest:
                    lowest = currentLowest
print lowest
