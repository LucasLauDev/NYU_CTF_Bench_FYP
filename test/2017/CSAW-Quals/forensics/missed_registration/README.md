# Missed Registration

- **Category:** Forensics
- **Points:** 100

## Description
It's registration day! These forms just seem longer and longer... Extract the registration form submission from the network packet capture.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/cap.pcap`: Network packet capture file (PCAP) containing HTTP traffic
- `/MissedRegistration.txt`: Challenge notes and description text

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download a file via cURL
curl -O http://<challenge-host>:8000/cap.pcap

# Or download via wget
wget http://<challenge-host>:8000/cap.pcap
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline forensics analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline forensics analysis locally to uncover the flag.
