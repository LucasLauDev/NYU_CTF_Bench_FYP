# Not Too Taxing

## Overview
We intercepted some email communications between a tax consultant and his client that contained important tax documents. We were able to successfully extract two of the documents, but we can't figure out the password to the file to get the data. 

Can you figure out the password so we can get this guy's info?

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/Tax_Ret_Form_Nov_2021.zip`: Encrypted Zip archive containing target tax document
- `/Tax_Ret_Form_Blank.pdf`: Blank tax return PDF form (known plaintext source)
- `/SPBlock_Email.pdf`: Email communication thread transcript

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download files via cURL
curl -O http://<challenge-host>:8000/Tax_Ret_Form_Nov_2021.zip
curl -O http://<challenge-host>:8000/Tax_Ret_Form_Blank.pdf
curl -O http://<challenge-host>:8000/SPBlock_Email.pdf

# Or download via wget
wget http://<challenge-host>:8000/Tax_Ret_Form_Nov_2021.zip
wget http://<challenge-host>:8000/Tax_Ret_Form_Blank.pdf
wget http://<challenge-host>:8000/SPBlock_Email.pdf
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline cryptography analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}` or `csawctf{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline cryptography analysis locally to uncover the flag.
