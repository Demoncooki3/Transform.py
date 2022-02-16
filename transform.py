'''edited by: Demoncooki3'''
'''this will find the flag for transformation flag'''
ltrs  = input("Enter code to decipher: ")
nums = [ord(l) for l in ltrs]
# picoCTF 2021
# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])


chars = []

for l in ltrs:
	int_char = ord(l)
	offset = (int_char >> 8)
	char1 = chr(offset)
	chars.append(char1)
	char2 = chr(int_char - (offset << 8))
	chars.append(char2)
	# print(chr(ord(l) >> 8),chr(ord(l)))
# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

print(''.join(chars))