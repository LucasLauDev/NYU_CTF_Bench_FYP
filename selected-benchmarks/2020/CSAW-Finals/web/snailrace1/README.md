# Snail Race 1

- **Category:** Web Security (Source Code Analysis)
- **Points:** 300

## Description
Complete source code and assets archive for the snail racing web application. Analyze the web application source code to discover the vulnerability and recover the flag.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/snailrace.tar.gz`: Tarball containing complete web application source code and assets

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download a file via cURL
curl -O http://<challenge-host>:8000/snailrace.tar.gz

# Or download via wget
wget http://<challenge-host>:8000/snailrace.tar.gz
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline web analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}` or `csawctf{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline web analysis locally to uncover the flag.
