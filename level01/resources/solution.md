### Solution

1. **Find the password hash of `flag01`:**

	The `/etc/passwd` file contains a hash that can be cracked.

	```bash
	cat /etc/passwd
	```

	Locate the line for `flag01`:
	```
	flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
	```

	The second field (`42hDRfypTqqnw`) is the hashed password.

2. **Save the hash to a file for cracking:**

	Create a new file to hold the hash in `username:hash` format:
	```bash
	echo 'flag01:42hDRfypTqqnw' > hash.txt
	```

3. **Crack the hash using John the Ripper:**

	Run John with a wordlist (e.g., `rockyou.txt`):
	```bash
	john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
	```

	Wait for John to find the password.

4. **Show the cracked password:**

	```bash
	john --show hash.txt
	```

	Output:
	```
	flag01:abcdefg
	```
	So the password is: `abcdef`

5. **Switch to user `flag01` and get the flag:**

	```bash
	su flag01
	```

	Enter the cracked password: `abcdef`

	Then run:
	```bash
	getflag
	```

	You’ll receive the `flag01` token.
