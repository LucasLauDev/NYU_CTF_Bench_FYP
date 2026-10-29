# M@sTEr 0F PrN9

- **Category:** Cryptography
- **Points:** 350

## Description
One day, I asked my mom when I would be able to become a master of PRNG. PRNG state recovery via truncated LCG and lattice reduction.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/task.py`: PRNG challenge Python script containing algorithm and intercepted outputs

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download a file via cURL
curl -O http://<challenge-host>:8000/task.py

# Or download via wget
wget http://<challenge-host>:8000/task.py
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline cryptography analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}` or `csawctf{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline cryptography analysis locally to uncover the flag.
