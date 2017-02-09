numbers = raw_input("Give me some numbers! I'll find the biggest!")
highest = 0
currentHighest = 0

for x in range(len(numbers)):
    if numbers[x: x + 1] > numbers[x + 1: x + 2]:
        currentHighest = numbers[x: x + 1]
        if currentHighest > highest:
            highest = currentHighest
print highest
