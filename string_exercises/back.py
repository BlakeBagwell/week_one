givenString = raw_input("Word to reverse: ")
newString = ''
holder = ''

for x in range(len(givenString)):
    holder = givenString[len(givenString) - 1: len(givenString)]
    newString = newString + holder
    givenString = givenString[0: len(givenString) - 1]
print newString
