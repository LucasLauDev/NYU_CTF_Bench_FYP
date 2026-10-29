# Short-Circuit

## Description
Start from the monkey's paw and work your way down the high voltage line, for every wire that branches off has an element that is either on or off. Ignore the first bit. Standard flag format.

Hint: There are 112 Things You Need to Worry About.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/short-circuit.jpg`: Digital logic circuit schematic diagram image

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download a file via cURL
curl -O http://<challenge-host>:8000/short-circuit.jpg

# Or download via wget
wget http://<challenge-host>:8000/short-circuit.jpg
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}` or `csawctf{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline miscellaneous analysis locally to uncover the flag.
