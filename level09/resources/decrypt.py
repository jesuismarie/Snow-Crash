token = [0x66, 0x34, 0x6b, 0x6d, 0x6d, 0x36, 0x70, 0x7c, 0x3d, 0x82, 0x7f, 0x70, 0x82, 0x6e, 0x83, 0x82, 0x44, 0x42, 0x83, 0x44, 0x75, 0x7b, 0x7f, 0x8c, 0x89]

decrypted = ""

for i in range(0, len(token)):
	token[i] -= i
	if token[i] < 0:
		token[i] += 127
	decrypted = decrypted + chr(token[i])

print(decrypted)
