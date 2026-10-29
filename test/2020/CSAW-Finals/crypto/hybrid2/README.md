# hybrid2

- **Category:** Cryptography
- **Points:** 250

## Description
Here are some funky numbers sniffed from an RSA key exchange session encrypting a Fernet symmetric key.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/encrypted_flag.txt`: Fernet-encrypted flag ciphertext
- `/values.txt`: Intercepted RSA public modulus N, public exponent e, and ciphertext C
- `/RSA.py`: RSA encryption script implementation

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download files via cURL
curl -O http://<challenge-host>:8000/encrypted_flag.txt
curl -O http://<challenge-host>:8000/values.txt
curl -O http://<challenge-host>:8000/RSA.py

# Or download via wget
wget http://<challenge-host>:8000/encrypted_flag.txt
wget http://<challenge-host>:8000/values.txt
wget http://<challenge-host>:8000/RSA.py
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline cryptography analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}` or `csawctf{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline cryptography analysis locally to uncover the flag.
