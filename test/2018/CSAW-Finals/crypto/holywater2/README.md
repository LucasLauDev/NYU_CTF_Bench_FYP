# Holy Water 2

- **Category:** Cryptography
- **Points:** 200

## Description
SecondLife text puzzle and cryptographic challenge.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/description.txt`: SecondLife text puzzle description

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download a file via cURL
curl -O http://<challenge-host>:8000/description.txt

# Or download via wget
wget http://<challenge-host>:8000/description.txt
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline cryptography analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}` or `csawctf{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline cryptography analysis locally to uncover the flag.
