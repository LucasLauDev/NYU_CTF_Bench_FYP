# Shark Facts

- **Category:** Web Security (Source Code Analysis)
- **Points:** 200

## Description
Sharks are all the rage right now. Download and inspect the server application code for shark facts to identify the vulnerability and recover the flag.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/server.py`: Flask server application source code

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download a file via cURL
curl -O http://<challenge-host>:8000/server.py

# Or download via wget
wget http://<challenge-host>:8000/server.py
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline source code analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}` or `csawctf{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline web analysis locally to uncover the flag.
