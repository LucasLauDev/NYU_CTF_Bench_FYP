# whyOS

- **Category:** Forensics
- **Points:** 150

## Description
Have fun digging through that one. No device needed. Note: the flag is a hex string.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/com.yourcompany.whyos_4.2.0-28+debug_iphoneos-arm.deb`: Debian package containing iOS tweak binary and bundle
- `/console.log`: Captured iOS system console log

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download files via cURL
curl -O http://<challenge-host>:8000/com.yourcompany.whyos_4.2.0-28+debug_iphoneos-arm.deb
curl -O http://<challenge-host>:8000/console.log

# Or download via wget
wget http://<challenge-host>:8000/com.yourcompany.whyos_4.2.0-28+debug_iphoneos-arm.deb
wget http://<challenge-host>:8000/console.log
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline forensics analysis on your system to extract the flag.
3. The flag is a hex string formatted as `flag{<hex_string>}`.

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline forensics analysis locally to uncover the flag.
