numbers = [1, 2, 3, 3, 2, 5, 2, 3, 1, 3, 2]
lowest = 0


#for i in range(len(numbers)):
#    for j in range(len(numbers)):
#        if numbers[i] < numbers[j]:
#            lowest = numbers[i]
#print lowest


a = [1, 2, 3, 2]
minimum = a[0]

for number in a:
    if minimum > number:
       minimum = number
print minimum
