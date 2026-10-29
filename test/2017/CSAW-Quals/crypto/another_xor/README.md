# Another_XOR

## Description
Hey, hey can you find my secret?
Break the XOR encryption to recover the flag.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/encrypted`: Hex-encoded ciphertext message
- `/cipher.py`: Python cipher generation script

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download files via cURL
curl -O http://<challenge-host>:8000/encrypted
curl -O http://<challenge-host>:8000/cipher.py

# Or download via wget
wget http://<challenge-host>:8000/encrypted
wget http://<challenge-host>:8000/cipher.py
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline cryptography analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}` or `csawctf{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline cryptography analysis locally to uncover the flag.
