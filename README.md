# 🧊 Snow Crash

> *This repository contains my personal solutions and walkthroughs for the **Snow Crash** security project, a CTF-style set of levels designed to teach real-world privilege escalation and system exploitation techniques.*

---

## Project Description

**Snow Crash** is a beginner-friendly cybersecurity challenge originally provided by 42 School. It introduces a wide range of essential security concepts in a hands-on and practical way.

Each level:

- Starts as user `levelXX`
- Requires finding the password for `flagXX`
- Involves exploiting misconfigurations, binaries, or simple flaws

This repository includes:

* Step-by-step walkthroughs for each level
* The flag password retrieved at the end of each challenge
* Notes on tools and concepts used
* External resource links where relevant

---

## Setup Instructions

To complete this project, you need access to the **Snow Crash** virtual machine.

---

### Requirements

* A **64-bit virtual machine** (VM)
* The **Snow Crash ISO image**
* SSH access on port `4242`
* An environment like VirtualBox, VMware, or QEMU

> If the IP address isn’t shown on boot, run `ifconfig` inside the VM.

---

### Getting Started

1. Boot the VM from the ISO
2. Login with the default credentials:

	* **Username**: `level00`
	* **Password**: `level00`
3. Connect via SSH (recommended):

	```bash
	ssh level00@<vm-ip> -p 4242
	```

4. Your goal in each level is to find a way to obtain the password for the `flagXX` user (e.g., `flag01`, `flag02`, etc.)
5. Once you're `flagXX`, run:

	```bash
	getflag
	```

	to receive the password for the next level

> **Brute-forcing is not allowed** — every level has a logic-based solution that you should understand and be able to explain.

---

## Repository Structure

```ini
.
├── level00/
│	├── flag	# flag
│	└── resources/	# explanation & extra files (if any)
├── level01/
│	└── …
└── level14/
```

---

## Level Scope

### Mandatory Levels:

* `level00` → `level09`

### Bonus Levels:

* `level10` → `level14` *(only considered if all mandatory levels are perfect)*

---

## ISO File

Need the Snow Crash ISO?
Contact via email: **[mari.nazaryan7173@gmail.com](mailto:mari.nazaryan7173@gmail.com)**

Happy hacking! 🛡️
