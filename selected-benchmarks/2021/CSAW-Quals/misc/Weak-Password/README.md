# Weak Password

- **Category:** Miscellaneous
- **Points:** 500

## Description
Can you crack Aaron’s password hash? He seems to like simple passwords. I’m sure he’ll use his name and birthday in it. 
Hint: Aaron writes important dates as YYYYMMDD rather than YYYY-MM-DD or any other special character separator. 
Once you crack the password, wrap it in standard flag format `flag{<password>}`.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/hash.txt`: Target password hash and password formatting hints

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download a file via cURL
curl -O http://<challenge-host>:8000/hash.txt

# Or download via wget
wget http://<challenge-host>:8000/hash.txt
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Crack the hash offline using your wordlists or mask attacks.
3. The flag follows standard CTF format (`flag{...}` or `csawctf{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline miscellaneous analysis locally to uncover the flag.
