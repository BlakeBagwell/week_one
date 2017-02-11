#add matrices

given1 = [[1, 2], [2, 3]]
given2 = [[3, 4], [4, 5]]
newList = []
finalList = []

for i in range(len(given1)):
    for j in range(len(given1[i])):
        if len(newList) == len(given1):
            break
        else:
            newList += [given1[i][j] + given2 [i][j]]
    finalList.append(newList)
    newList = []
print finalList
