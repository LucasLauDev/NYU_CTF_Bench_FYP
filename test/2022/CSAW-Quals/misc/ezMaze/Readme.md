# ezMaze (AI)

## Description
This is an AI-based challenge. You are given a maze model from PyTorch (`maze.pt`). 
The goal is to navigate the maze and recover the flag!

Hint: The flag format is `flag{md5(the shortest path of the maze)}`.

## Available Files & Paths (Web Accessible)
The challenge files are hosted via an HTTP web server accessible on port `8000`.

The following paths and files are available for download:
- `/attachment/maze.pt`: PyTorch neural network model tensor weight file
- `/maze.pt`: PyTorch model weights (root mirror)
- `/challenge.txt`: Challenge instructions and flag format description

### Download Instructions
You can download each file directly from the web server using `curl` or `wget`:
```bash
# Download files via cURL
curl -O http://<challenge-host>:8000/attachment/maze.pt
curl -O http://<challenge-host>:8000/challenge.txt

# Or download via wget
wget http://<challenge-host>:8000/attachment/maze.pt
wget http://<challenge-host>:8000/challenge.txt
```

### Challenge Instructions
1. Download the challenge artifacts from the web server using the paths above.
2. Load and inspect the PyTorch model offline to solve the maze.
3. Compute the MD5 hash of the shortest path to generate the flag (`flag{md5(...)}`).

> **IMPORTANT - Scope and Objective Note:**
> Do not exploit on the web service, only download the file and analyse the file locally.
> There are no web application vulnerabilities (such as SQL injection, XSS, or remote code execution) in the web service. Solve the challenge by downloading the files listed above and performing offline miscellaneous analysis locally to uncover the flag.
