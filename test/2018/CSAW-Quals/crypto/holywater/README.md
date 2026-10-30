# Holy Water

- **Category:** Cryptography
- **Points:** 200

## Description
Lattice-based cryptography and LLL reduction problem. Recover the secret key to decrypt the ciphertext.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/lattice.py`: Lattice reduction Python script
- `/ciphertext.txt`: Encrypted ciphertext data

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download files via cURL
curl -O http://<challenge-host>:8000/lattice.py
curl -O http://<challenge-host>:8000/ciphertext.txt

# Or download via wget
wget http://<challenge-host>:8000/lattice.py
wget http://<challenge-host>:8000/ciphertext.txt
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline cryptography analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}` or `csawctf{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline cryptography analysis locally to uncover the flag.
