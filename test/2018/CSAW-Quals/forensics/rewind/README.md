# Rewind

## Description
Sometimes you have to look back and replay what has been done right and wrong.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/memstrings.cpp`: Memory string extraction C++ source code
- `/memstrings.h`: Memory string extraction C++ header file

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download files via cURL
curl -O http://<challenge-host>:8000/memstrings.cpp
curl -O http://<challenge-host>:8000/memstrings.h

# Or download via wget
wget http://<challenge-host>:8000/memstrings.cpp
wget http://<challenge-host>:8000/memstrings.h
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline forensics analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}` or `csawctf{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline forensics analysis locally to uncover the flag.
