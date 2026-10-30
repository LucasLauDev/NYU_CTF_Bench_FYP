# DES2Bites

- **Category:** Cryptography
- **Points:** 200

## Description
You are taking too big of a bite. Try to take a nibble. Weak key Double DES cryptanalysis.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/DES2Bytes.enc`: Ciphertext of known plaintext encrypted under Double DES
- `/DES2Bytes.txt`: Known plaintext text file
- `/FLAG.enc`: Flag ciphertext encrypted under the same Double DES keys
- `/Generator.py`: Double DES generation script illustrating key constraints

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download files via cURL
curl -O http://<challenge-host>:8000/DES2Bytes.enc
curl -O http://<challenge-host>:8000/DES2Bytes.txt
curl -O http://<challenge-host>:8000/FLAG.enc
curl -O http://<challenge-host>:8000/Generator.py

# Or download via wget
wget http://<challenge-host>:8000/DES2Bytes.enc
wget http://<challenge-host>:8000/DES2Bytes.txt
wget http://<challenge-host>:8000/FLAG.enc
wget http://<challenge-host>:8000/Generator.py
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline cryptography analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}` or `csawctf{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline cryptography analysis locally to uncover the flag.
