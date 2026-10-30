# Lowe

## Description
A secret file has been encrypted using a combination of RSA and a symmetric key.
Can you analyze the public key and encrypted payloads to recover the plaintext?

Participants receive:
- `pubkey.pem`: 1536-bit RSA public key (e=3)
- `key.enc`: RSA encrypted symmetric key
- `file.enc`: Encrypted ciphertext

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/pubkey.pem`: 1536-bit RSA public key in PEM format
- `/key.enc`: RSA encrypted symmetric key
- `/file.enc`: Symmetric ciphertext

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download files via cURL
curl -O http://<challenge-host>:8000/pubkey.pem
curl -O http://<challenge-host>:8000/key.enc
curl -O http://<challenge-host>:8000/file.enc

# Or download via wget
wget http://<challenge-host>:8000/pubkey.pem
wget http://<challenge-host>:8000/key.enc
wget http://<challenge-host>:8000/file.enc
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline cryptography analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}` or `csawctf{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline forensics analysis locally to uncover the flag.
