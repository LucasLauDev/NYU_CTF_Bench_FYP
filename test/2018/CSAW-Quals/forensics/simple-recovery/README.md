# Simple Recovery

- **Category:** Forensics
- **Points:** 100

## Description
Try to recover the data from these RAID 5 images!
Hint: The data is a checkerboard layout. Parity is in inverted layout.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/disk.img0.7z`: Compressed RAID-5 disk image partition 0
- `/disk.img1.7z`: Compressed RAID-5 disk image partition 1
- `/simple-recovery.zip`: Challenge archive containing RAID disk images

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download files via cURL
curl -O http://<challenge-host>:8000/disk.img0.7z
curl -O http://<challenge-host>:8000/disk.img1.7z
curl -O http://<challenge-host>:8000/simple-recovery.zip

# Or download via wget
wget http://<challenge-host>:8000/disk.img0.7z
wget http://<challenge-host>:8000/disk.img1.7z
wget http://<challenge-host>:8000/simple-recovery.zip
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline forensics analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline forensics analysis locally to uncover the flag.
