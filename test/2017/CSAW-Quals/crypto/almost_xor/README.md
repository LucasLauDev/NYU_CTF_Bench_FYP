# almost_xor

## Description
Break the custom XOR-like stream cipher to decrypt the ciphertext and recover the flag.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/almostxor.py`: Stream cipher script implementing modulo 8 addition
- `/ciphertext`: Hex-encoded ciphertext

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download files via cURL
curl -O http://<challenge-host>:8000/almostxor.py
curl -O http://<challenge-host>:8000/ciphertext

# Or download via wget
wget http://<challenge-host>:8000/almostxor.py
wget http://<challenge-host>:8000/ciphertext
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline cryptography analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}` or `csawctf{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline cryptography analysis locally to uncover the flag.
