### Solution

1. **List files in the home directory:**

	List files:

	```bash
	ls -l
	```

	Output:

	```
	-rwsr-sr-x 1 flag13 level13 7303 Aug 30  2015 level13
	```

2. **Run the executable file:**

	```bash
	./level13
	```

	Output:

	```
	UID 2013 started us but we we expect 4242
	```

	Your UID is 2013. It expects 4242 (hex: `0x1092`).

3. **Open Binary in GDB.**

	```bash
	gdb level13
	```

	Disassemble `main`:

	```gdb
	disas main
	```

	Look for this code:

	```asm
	0x08048595 <+9>:   call   0x8048380 <getuid@plt>
	0x0804859a <+14>:  cmp    $0x1092,%eax
	0x0804859f <+19>:  je     0x80485cb <main+63>
	```

	This compares your UID to 4242 and only proceeds if equal.

4. **Bypass the UID Check.**

	Set a breakpoint *after* the `getuid()` call and *before* the comparison:

	```gdb
	break *0x0804859a
	```

	Start the program:

	```gdb
	run
	```

	When it breaks:

	```gdb
	set $eax = 0x1092
	continue
	```

	Output:

	```
	your token is 2A31L79asukciNyi8uppkEuSx
	```

	You’ll receive the `flag13` token.
