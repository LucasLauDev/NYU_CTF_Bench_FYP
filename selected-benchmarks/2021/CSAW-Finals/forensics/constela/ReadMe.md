# Constela

- **Category:** Forensics
- **Points:** 300

## Description
The year is 7331, and BadCorp rules the galaxy with its omnipresent satellites. But recently a resistance movement led by a band of hackers calling themselves the OSIRIS has hacked into BadCorp systems; they have taken over the satellites and it is believed they are trying to send a message across the galaxy...
Can humanity *see* their message?

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/constela.pcapng`: Satellite communication network packet capture (PCAPNG)
- `/gps_data.txt`: Orbital GPS coordinates and timing logs

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download files via cURL
curl -O http://<challenge-host>:8000/constela.pcapng
curl -O http://<challenge-host>:8000/gps_data.txt

# Or download via wget
wget http://<challenge-host>:8000/constela.pcapng
wget http://<challenge-host>:8000/gps_data.txt
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline forensics analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline forensics analysis locally to uncover the flag.
