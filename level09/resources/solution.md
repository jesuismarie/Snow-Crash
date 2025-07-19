### Solution

1. **List files and check permissions:**

	```bash
	ls -l
	```

	You’ll see:

	```
	-rwsr-sr-x 1 flag09 level09 7640 Mar  5  2016 level09
	----r--r-- 1 flag09 level09   26 Mar  5  2016 token
	```

	* `level09` is a **SUID binary** owned by `flag09`.
	* The `token` file is **not readable** by `level09` user (only by `flag09`), but **executable binary can read it** due to SUID bit.

2. **Run the binary.**

	Run without arguments:

	```bash
	./level09
	```

	Output:

	```
	You need to provied only one arg.
	```

	Then pass the token file as argument:

	```bash
	./level09 token
	```

	Output:

	```
	tpmhr
	```

	The result appears to be an incomplete or incorrect output. Let’s investigate.

3. **Transfer the token file to host for analysis:**

	On your host:

	```bash
	scp -P 4242 level09@<vm-ip>:~/token .
	chmod 644 token
	```

	Use `hexdump` to see the raw content:

	```bash
	hexdump -C token
	```

	Output:

	```
	00000000  66 34 6b 6d 6d 36 70 7c  3d 82 7f 70 82 6e 83 82  |f4kmm6p|=..p.n..|
	00000010  44 42 83 44 75 7b 7f 8c  89 0a                    |DB.Du{....|
	```

	The last byte `0a` is a **newline character**, not part of the actual encrypted data. It can be safely ignored for decryption.

4. **Write a Python script to decrypt the token.**

	From Ghidra analysis of `level09`, we find that the binary performs **byte-wise decryption**, where:

	* Each byte is **decremented by its index**
	* If the result is negative, 127 is added to wrap it

	Create a script:

	```python
	token = [0x66, 0x34, 0x6b, 0x6d, 0x6d, 0x36, 0x70, 0x7c,
			0x3d, 0x82, 0x7f, 0x70, 0x82, 0x6e, 0x83, 0x82,
			0x44, 0x42, 0x83, 0x44, 0x75, 0x7b, 0x7f, 0x8c, 0x89]

	decrypted = ""

	for i in range(len(token)):
		token[i] -= i
		if token[i] < 0:
			token[i] += 127
		decrypted += chr(token[i])

	print(decrypted)
	```

	Output:

	```
	f3iji1ju5yuevaus41q1afiuq
	```

	That is the **decrypted token**.

5. **Use the token to switch user.**

	Back in the VM:

	```bash
	su flag09
	```

	Enter the token as password:

	```
	f3iji1ju5yuevaus41q1afiuq
	```

	Then get the flag:

	```bash
	getflag
	```

	Output:

	```
	Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z
	```

	You’ll receive the `flag09` token.
