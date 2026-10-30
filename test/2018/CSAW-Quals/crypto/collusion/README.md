# Collusion

## Description
A collusion-secure identity-based encryption scheme built from RSA. Can you break the scheme and decrypt the secret message?

We provide the master public key, a ciphertext encrypted to Alice, and decrypter keys for Bob and Carol. Your objective is to decrypt the message to Alice.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/encrypter.json`: Master public key parameters (N and H)
- `/bobs-key.json`: Bob's IBE private key parameters
- `/carols-key.json`: Carol's IBE private key parameters
- `/message.json`: Encrypted message payload in JSON format
- `/common.go`: Shared Go types and cryptographic definitions

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download files via cURL
curl -O http://<challenge-host>:8000/encrypter.json
curl -O http://<challenge-host>:8000/bobs-key.json
curl -O http://<challenge-host>:8000/carols-key.json
curl -O http://<challenge-host>:8000/message.json
curl -O http://<challenge-host>:8000/common.go

# Or download via wget
wget http://<challenge-host>:8000/encrypter.json
wget http://<challenge-host>:8000/bobs-key.json
wget http://<challenge-host>:8000/carols-key.json
wget http://<challenge-host>:8000/message.json
wget http://<challenge-host>:8000/common.go
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline cryptography analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}` or `csawctf{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline cryptography analysis locally to uncover the flag.
