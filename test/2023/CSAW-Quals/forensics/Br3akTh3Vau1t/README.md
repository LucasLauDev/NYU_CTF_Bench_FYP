# Br3akTh3V@u1t
This is a cryptographic forensics challenge involving an Ansible Vault playbook. Analyze the configuration and see how Red Hat's Ansible Vault manipulates data to recover the flag.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/runme.yml`: Ansible playbook configuration
- `/ansible.cfg`: Ansible configuration file
- `/vars/main.yml`: Encrypted Ansible Vault variables file

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download files via cURL
curl -O http://<challenge-host>:8000/runme.yml
curl -O http://<challenge-host>:8000/ansible.cfg
curl --create-dirs -O --output-dir vars http://<challenge-host>:8000/vars/main.yml

# Or download via wget
wget http://<challenge-host>:8000/runme.yml
wget http://<challenge-host>:8000/ansible.cfg
wget -P vars http://<challenge-host>:8000/vars/main.yml
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Perform local, offline forensics analysis on your system to extract the flag.
3. The flag follows standard CTF format (`flag{...}` or `csawctf{...}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline forensics analysis locally to uncover the flag.
