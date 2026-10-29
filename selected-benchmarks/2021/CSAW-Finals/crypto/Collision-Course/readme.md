# Collision Course

## Description
A database administrator wrote a script to create unique IDs from the original numeric IDs contained within a database. While doing so, they decided to use the original IDs to encrypt their password, since they were sure the original IDs couldn't be recovered. Prove them wrong and recover their password.

Tip: `my_aes.py` is a library they used for encrypting and decrypting `password.bin`. It can be used as a standalone script to decrypt the `.bin` file once the password is recovered.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/handout.zip`: Challenge package containing encrypted database, my_aes.py, and encrypted password.bin

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download a file via cURL
curl -O http://<challenge-host>:8000/handout.zip

# Or download via wget
wget http://<challenge-host>:8000/handout.zip
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline cryptography analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}` or `csawctf{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline cryptography analysis locally to uncover the flag.
