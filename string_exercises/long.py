userWord = raw_input("Word: ")
longWord = ''

for x in range(len(userWord)):
    if userWord[x: x + 1] != userWord[x + 1: x + 2]:
        longWord += userWord[x: x + 1]
    if userWord[x: x + 1] == userWord[x + 1: x + 2]:
        longWord += (userWord[x: x + 1]) * 4

print longWord
