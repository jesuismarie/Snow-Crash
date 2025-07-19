### Solution

1. **Understand the goal.**

	You're `level14`, but the binary `/bin/getflag` only gives the token if your UID is `3014` (user: `flag14`).

	Check the UID of `flag14`:

	```bash
	cat /etc/passwd | grep flag14
	```

	Output:

	```
	flag14:x:3014:3014::/home/flag/flag14:/bin/bash
	```

2. **Open `/bin/getflag` in GDB.**

	```bash
	gdb /bin/getflag
	```

3. **Disassemble `main()` function:**

	```gdb
	disas main
	```

	Look for this part early in `main()`:

	```asm
	0x08048989 <+67>:	call   0x8048540 <ptrace@plt>
	0x0804898e <+72>:	test   %eax, %eax
	0x08048990 <+74>:	jns    0x80489a8 <main+98>
	0x08048992 <+76>:	movl   $0x8048fa8,(%esp)
	0x08048999 <+83>:	call   0x80484e0 <puts@plt>
	```

4. **Bypass the anti-debugging check (`ptrace`).**

	The `ptrace` call is used to detect if a debugger is attached. If it is, the return value (`%eax`) is `-1`.

	To bypass:

	* Set a breakpoint at the test instruction:

		```gdb
		break *0x0804898e
		```

	* Run the program:

		```gdb
		run
		```

	* After the breakpoint hits, verify and patch:

		```gdb
		print $eax
		set $eax = 0
		continue
		```

	This tricks the binary into thinking no debugger is attached.

5. **Find and bypass the UID check.**

	Look for the section that checks your UID:

	```asm
	0x08048afd <+439>:	call   0x80484b0 <getuid@plt>
	0x08048b02 <+444>:	mov    %eax,0x18(%esp)
	0x08048b06 <+448>:	mov    0x18(%esp),%eax
	0x08048b0a <+452>:	cmp    $0xbbe,%eax      # Compare with UID 3006
	...
	0x08048bbb <+629>:	je     0x8048de5        # Jump if eax == 0xbc6 (3014)
	```

4. **Set breakpoints.**

	First, break before the `ptrace()` anti-debugging check:

	```gdb
	break *0x0804898e
	```

	Also break right before the UID comparison:

	```gdb
	break *0x08048b0a
	```

5. **Run the program.**

	```gdb
	run
	```

6. **Bypass anti-debugging logic.**

	When it breaks at `0x0804898e`:

	```gdb
	set $eax = 0    # Make ptrace think it's not being debugged
	continue
	```

7. **Change UID to 3014.**

	When it breaks at `0x08048b0a`:

	```gdb
	print $eax       # Should be 2014 (your real UID)
	set $eax = 3014  # Fools the binary into thinking you're flag14
	continue
	```

	Output:

	```
	Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
	```

	You’ve successfully tricked the binary and retrieved `flag14`!
