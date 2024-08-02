import string

letters = list(string.ascii_letters)
length = len(letters)
inp_text = input("Your text: ")
inp_list = list(inp_text)

while 1:
    option = input("Enter option Encrypt or Decrypt: ").lower()
    if option in ['encrypt', 'decrypt']:
        break

for i, n in enumerate(inp_list):
    if n in letters:
        idex: int = letters.index(n)
        if option == 'encrypt':
            if (idex + 5) > length:
                idex = idex + 5 - length
            else:
                idex = idex + 5

        elif option == 'decrypt':
            idex: int = idex - 5
            inp_list[i] = letters[idex]

        inp_list[i] = letters[idex]
    else:
        inp_list[i] = n

print(''.join(inp_list))
