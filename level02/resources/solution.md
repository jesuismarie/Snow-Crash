### Solution

1. **List files in the home directory:**

	```bash
	ls -l
	```

	You will see:
	```
	----r--r-- 1 flag02 level02 8302 Aug 30	2015 level02.pcap
	```

	The `level02.pcap` file is a packet capture and is readable.

2. **Transfer the `.pcap` file to your host machine:**

	From your host, use `scp` to copy the file:

	```bash
	scp -P 4242 level02@<vm-ip>:~/level02.pcap .
	```

	Enter the password for `level02` when prompted.
	Then run:

	```bash
	chmod +r level02.pcap
	```

3. **Extract the password from the capture file:**

	#### Option 1: Use Wireshark (GUI)

	* Open the file:

		```bash
		wireshark level02.pcap
		```

	* Right-click any packet and choose:

		```
		Follow → TCP Stream
		```

	* In the popup window you’ll find:

		```
		Password:
		ft_wandr...NDRel.L0L
		```

	#### Option 2: Use `tshark` (Terminal)

	* If Wireshark isn’t available, use this command:

		```bash
		tshark -Tfields -e data -r level02.pcap > data
		```

	This extracts raw hexadecimal payload data from the capture file.

4. **Convert text to C Array:**

	```ini
	char peer0_13[] = { /* Packet 45 */ 0x66 }; /* f */
	char peer0_14[] = { /* Packet 47 */ 0x74 }; /* t */
	char peer0_15[] = { /* Packet 49 */ 0x5f }; /* _ */
	char peer0_16[] = { /* Packet 51 */ 0x77 }; /* w */
	char peer0_17[] = { /* Packet 53 */ 0x61 }; /* a */
	char peer0_18[] = { /* Packet 55 */ 0x6e }; /* n */
	char peer0_19[] = { /* Packet 57 */ 0x64 }; /* d */
	char peer0_20[] = { /* Packet 59 */ 0x72 }; /* r */
	char peer0_21[] = { /* Packet 61 */ 0x7f }; /* Delete */
	char peer0_22[] = { /* Packet 63 */ 0x7f }; /* Delete */
	char peer0_23[] = { /* Packet 65 */ 0x7f }; /* Delete */
	char peer0_24[] = { /* Packet 67 */ 0x4e }; /* N */
	char peer0_25[] = { /* Packet 69 */ 0x44 }; /* D */
	char peer0_26[] = { /* Packet 71 */ 0x52 }; /* R */
	char peer0_27[] = { /* Packet 73 */ 0x65 }; /* e */
	char peer0_28[] = { /* Packet 75 */ 0x6c }; /* l */
	char peer0_29[] = { /* Packet 77 */ 0x7f }; /* Delete */
	char peer0_30[] = { /* Packet 79 */ 0x4c }; /* L */
	char peer0_31[] = { /* Packet 81 */ 0x30 }; /* 0 */
	char peer0_32[] = { /* Packet 83 */ 0x4c }; /* L */
	char peer0_33[] = { /* Packet 85 */ 0x0d }; /* Carriage Return */
	```

5. **Switch to user `flag02` and get the flag:**

	Back in your VM terminal:

	```bash
	su flag02
	```

	Enter the password: `ft_waNDReL0L`

	Then run:

	```bash
	getflag
	```

	You’ll receive the `flag02` token.
