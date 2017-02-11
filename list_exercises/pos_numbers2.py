#create new list of positive numbers from a diff list
givenList = [1, 2, 3, 4, -5, -6]
newList = []
for i in range(len(givenList)):
    if givenList[i] > 0:
        newList.append(givenList[i])
print newList
