offset = 13
secretWord = raw_input("Secret word: ")

alphabet = 'abcdefghijklmnopqrstuvwxyz'
cipher = ''
letter = ''
translation = ''

for x in range(len(alphabet)):
    letter = alphabet[x + offset: x + 1 + offset]
    cipher += letter
    if x == len(alphabet) - offset:
        break
for y in range(offset):
    letter = alphabet[y: y + 1]
    cipher += letter

for z in range(len(secretWord)):
    for v in range(len(cipher)):
        if secretWord[z: z + 1] == cipher[v: v + 1]:
            letter = alphabet[v: v + 1]
            translation += letter
            break
    if secretWord[z: z + 1] != cipher[v: v + 1]:
        letter = secretWord[z: z + 1]
        translation += letter

print translation
