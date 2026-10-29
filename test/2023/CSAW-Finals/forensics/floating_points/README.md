# Floating Points

- **Category:** Forensics
- **Points:** 200

## Description
In the fading light, Max studied the complex puzzle box, its surface a maze of curves and bits. Within the bitstream lies IEEE 754 floating point numbers.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/floating_points`: Binary data file containing raw floating point values

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download a file via cURL
curl -O http://<challenge-host>:8000/floating_points

# Or download via wget
wget http://<challenge-host>:8000/floating_points
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline forensics analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline forensics analysis locally to uncover the flag.
