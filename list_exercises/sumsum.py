numbers = raw_input("Give me some numbers!")
sum = 0

for x in range(len(numbers)):
    sum += int(numbers[x: x + 1])

print sum
