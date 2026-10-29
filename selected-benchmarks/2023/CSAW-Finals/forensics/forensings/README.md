# Forensings
> Category: forensics
> Suggested Points: -

# Description
> Detailed description for the participants.

Can you use your best forensics and singing skills to gather the four parts of the flag?

# Deployment
> Any special information about the deployment.

The .zip is the only file needed for deployment. This is an offline challenge.

# Design
> Detailed description for the lab members.

The challenge goal is to mix both forensics tasks with audio steganography. The flag is split into four different parts, where two of them will be gathered using forensics techniques, and the other two using different audio steganography mechanisms.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/link_to_the_zip_file.txt`: Download link for the complete audio challenge package

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download a file via cURL
curl -O http://<challenge-host>:8000/link_to_the_zip_file.txt

# Or download via wget
wget http://<challenge-host>:8000/link_to_the_zip_file.txt
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline forensics analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}` or `csawctf{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline forensics analysis locally to uncover the flag.
