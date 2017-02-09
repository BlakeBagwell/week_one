userWord = raw_input("Word to convert: ").upper()
word = ''
letter = ''
for x in range(len(userWord)):
  letter = userWord[x: x + 1]
  if letter == 'A':
    word += '4'

  elif letter == 'E':
      word += '3'

  elif letter == 'G':
      word += '6'

  elif letter == 'I':
      word += '1'

  elif letter == 'O':
      word += '0'

  elif letter == 'S':
      word += '5'

  elif letter == 'T':
      word += '7'

  else:
    word += letter

print word
