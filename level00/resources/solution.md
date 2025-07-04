### Solution

1. **Find the file owned by `flag00`:**

	```bash
	find / -type f -user flag00 2>/dev/null
	```

2. **Read the content of the discovered file:**

	```bash
	cat /usr/sbin/john
	```

	This reveals:
	```
	cdiiddwpgswtgt
	```

3. **Decode it using ROT11:**

	```bash
	echo cdiiddwpgswtgt | tr 'a-z' 'l-za-k'
	```

	Output:
	```
	nottoohardhere
	```

4. **Switch to user `flag00` and get the flag:**

	```bash
	su flag00
	```

	Enter the decoded password: `nottoohardhere`

	Then run:
	```bash
	getflag
	```

	You’ll receive the `flag00` token.
