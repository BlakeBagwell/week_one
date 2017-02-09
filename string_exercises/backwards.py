y =
copy = ''
z = ''

for x in (len(y)):
    y.slice(len(y), len(y) +1) = copy
    z += copy
    y = y.slice(1, len(y))
print z



get string

loop based on length of string
    copy last character of string
    add it to newString
    redefine the string as itself minus its last space
        by copying and replacing with splice
print newString

givenString = raw_input("Word to reverse: ")
newString = ''
holder = ''

for x in range(len(givenString)):
    holder = givenString.slice(len(givenString), len(givenString) + 1)
    newString = newString + holder
    givenString = givenString.slice(0, len(givenString) - 1)
