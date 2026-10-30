# Emoji

- **Category:** Forensics
- **Points:** 200

## Description
🤬 A mysterious sequence of emoji characters and an image contain an encoded secret.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/emoji.png`: PNG image containing visual/steganographic emoji clues
- `/emoji.txt`: Unicode emoji character sequence stream

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download files via cURL
curl -O http://<challenge-host>:8000/emoji.png
curl -O http://<challenge-host>:8000/emoji.txt

# Or download via wget
wget http://<challenge-host>:8000/emoji.png
wget http://<challenge-host>:8000/emoji.txt
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline forensics analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline forensics analysis locally to uncover the flag.
