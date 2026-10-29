# NYU CTF Bench - Offline Challenges Analysis
### Categories: Cryptography, Forensics, Miscellaneous, and Web

This report analyzes the **NYU CTF Bench** `test/` dataset across four major categories: **Cryptography**, **Forensics**, **Miscellaneous (Misc)**, and **Web Security**. It details exactly how many challenges are offline versus online, the criteria for classification, and provides comprehensive tables of all offline challenge IDs, deliverables, and primitives.

---

## 1. Executive Summary & Offline Totals

| Category | Total in Benchmark | Offline Challenges | Online / Docker-Based | % Offline | On-Disk Dirs (incl. unindexed) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Forensics** | **15** | **12** | 3 | **80.0%** | 17 (+2 unindexed) |
| **Miscellaneous (Misc)** | **24** | **7** | 17 | **29.2%** | 24 |
| **Cryptography (Crypto)** | **52** | **14** | 38 | **26.9%** | 54 (+2 unindexed) |
| **Web Security** | **19** | **0** *(2 static code dumps)* | 17 | **0.0%** | 23 (+4 unindexed) |
| **TOTAL (4 Categories)** | **110** | **33** *(or 35)* | **75** | **30.0%** *(or 31.8%)* | **118** |

### What Defines an Offline Challenge?
* **Offline / Static Challenges:** All files, ciphertexts, memory dumps, captures, models, or scripts required to solve the challenge are packaged directly in the challenge folder. Solvers do not require a running Docker container, listening socket, or live network interaction.
* **Online / Service-Based Challenges:** Require a running background service via Docker (`docker-compose.yml`) or an external socket connection where the solver interacts with an oracle, daemon, or web application over TCP/HTTP.

---

## 2. Forensics Category (12 out of 15 Offline)

Forensics has the highest offline ratio in the benchmark (**80.0%**). Solvers inspect memory dumps, network packets, disk images, or steganography locally.

### Offline Forensics Challenges Table

| # | Benchmark ID | Challenge Name | Year & Event | Provided Deliverables | Forensic Primitive & Analysis Type |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | `2017f-for-thoroughlystripped` | **thoroughlyStripped** | 2017 CSAW-Finals | `thoroughlyStripped` | Core dump & heap memory reconstruction |
| 2 | `2017q-for-missed_registration` | **missed_registration** | 2017 CSAW-Quals | `cap.pcap` | Network capture analysis (HTTP POST form reconstruction) |
| 3 | `2018q-for-simple_recovery` | **simple-recovery** | 2018 CSAW-Quals | `disk.img0.7z`, `disk.img1.7z` | RAID-5 parity reconstruction and disk carving |
| 4 | `2018q-for-whyos` | **whyOS** | 2018 CSAW-Quals | `whyos_4.2.0-28+debug_iphoneos-arm.deb`, `console.log` | iOS tweak bundle forensics & syslog extraction |
| 5 | `2021f-for-constela` | **constela** | 2021 CSAW-Finals | `constela.pcapng` | Satellite DNS PCAP traffic & GPS coordinates mapping |
| 6 | `2021q-for-lazy_leaks` | **Lazy-Leaks** | 2021 CSAW-Quals | `Lazy_Leaks.pcapng` | Unsecured protocol communications dump analysis |
| 7 | `2023f-for-emoji` | **emoji** | 2023 CSAW-Finals | `emoji.txt`, `emoji.png` | Unicode emoji steganography & encoding parsing |
| 8 | `2023f-for-floating_points` | **floating_points** | 2023 CSAW-Finals | `floating_points` | IEEE 754 floating point bitstream reverse engineering |
| 9 | `2023f-for-forensings` | **forensings** | 2023 CSAW-Finals | `forensings.zip` | Multi-stage audio spectrogram & file carving |
| 10 | `2023f-for-hypokrinesthai` | **hypokrinesthai** | 2023 CSAW-Finals | `hypokrinesthai.txt` | Text obfuscation / reverse character stream analysis |
| 11 | `2023q-for-1black0white` | **1black0white** | 2023 CSAW-Quals | `qr_code.txt` | Matrix bitstring to visual QR code reconstruction |
| 12 | `2023q-for-br3akth3vau1t` | **Br3akTh3Vau1t** | 2023 CSAW-Quals | `runme.yml`, `ansible.cfg`, `vars/main.yml` | Ansible Vault decryption & configuration auditing |

*(The 3 online forensics challenges are: `2021f-for-no_time_to_register`, `2023f-for-ancient_forensics`, and `2017q-for-best_router`).*

---

## 3. Cryptography Category (14 out of 52 Offline)

In Cryptography, **14 out of 52 challenges** (**26.9%**) are offline. Solvers break mathematical algorithms, weak key generation, or cipher implementations without oracle interaction.

### Offline Cryptography Challenges Table

| # | Benchmark ID | Challenge Name | Year & Event | Provided Deliverables | Cryptographic Primitive & Attack Method |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | `2017f-cry-ecxor` | **ECXOR** | 2017 CSAW-Finals | `ecxor_handout_100.py`, `rfc8032.py`, `ciphertext` | Curve25519 generalized Vigenère / group order attack |
| 2 | `2017q-cry-almost_xor` | **almost_xor** | 2017 CSAW-Quals | `almostxor.py`, `ciphertext` | Modulo 8 addition stream cipher reversing |
| 3 | `2017q-cry-another_xor` | **another_xor** | 2017 CSAW-Quals | `encrypted` | Repeating-key multi-byte XOR frequency analysis |
| 4 | `2018q-cry-babycrypto` | **babycrypto** | 2018 CSAW-Quals | `ciphertext.txt` | Single-byte XOR / Diffie-Hellman transcript cryptanalysis |
| 5 | `2018q-cry-collusion` | **collusion** | 2018 CSAW-Quals | `bobs-key.json`, `carols-key.json`, `message.json`, `common.go` | Identity-Based Encryption (IBE) RSA collusion attack |
| 6 | `2018q-cry-lowe` | **lowe** | 2018 CSAW-Quals | `file.enc`, `key.enc`, `pubkey.pem` | Unpadded RSA low public exponent ($e=3$) cube root attack |
| 7 | `2019q-cry-des2bites` | **DES2Bites** | 2019 CSAW-Quals | `DES2Bytes.enc`, `DES2Bytes.txt`, `FLAG.enc`, `Generator.py` | Double DES weak and semi-weak key space exhaustion |
| 8 | `2020f-cry-hybrid2` | **hybrid2** | 2020 CSAW-Finals | `encrypted_flag.txt`, `values.txt`, `RSA.py` | RSA small public exponent attack on sniffed parameters |
| 9 | `2020q-cry-perfect_secrecy`| **perfect_secrecy** | 2020 CSAW-Quals | `image1.png`, `image2.png` | One-Time Pad key reuse (Two-Time Pad image bitmask XOR) |
| 10 | `2021f-cry-collision_course`| **Collision-Course**| 2021 CSAW-Finals | `handout.zip` | MD5 hash collision generation & AES key reconstruction |
| 11 | `2021q-cry-crack_me` | **Crack-Me** | 2021 CSAW-Quals | `README.md` (hash in description) | Salted hash cracking using algorithm name as salt |
| 12 | `2022f-cry-m_ster_0f_prn9` | **M@sTEr 0F PrN9** | 2022 CSAW-Finals | `task.py` | LCG / PRNG state recovery via LLL lattice reduction |
| 13 | `2022q-cry-not_too_taxing` | **not-too-taxing** | 2022 CSAW-Quals | `Tax_Ret_Form_Nov_2021.zip`, `Tax_Ret_Form_Blank.pdf`, `SPBlock_Email.pdf` | Known-plaintext attack on ZipCrypto using `bkcrack` |
| 14 | `2023q-cry-circles` | **circles** | 2023 CSAW-Quals | `server.py`, `flag.enc` | Moser's Circle Problem sequence keystream deduction |

*(The remaining 38 crypto challenges run network services / oracles via Docker or remote netcat sockets).*

---

## 4. Miscellaneous Category (7 out of 24 Offline)

In the Misc category, **7 out of 24 challenges** (**29.2%**) are offline. The remaining 17 challenges require interactive netcat services (e.g. Python jails, timed speed challenges, or AI queries).

### Offline Miscellaneous Challenges Table

| # | Benchmark ID | Challenge Name | Year & Event | Provided Deliverables | Problem Type & Solution Method |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | `2018f-msc-leaked_flag` | **leaked_flag** | 2018 CSAW-Finals | None *(text prompt)* | **Sanity Check:** Freebie flag directly embedded in description |
| 2 | `2018q-msc-short_circuit` | **Short-Circuit** | 2018 CSAW-Quals | `short-circuit.jpg` | **Hardware Logic:** Trace circuit schematic diagram logic gates |
| 3 | `2019f-msc-alive` | **alive** | 2019 CSAW-Finals | None *(text prompt)* | **Sanity Check:** Freebie flag included in the welcome poem |
| 4 | `2021q-msc-weak_password` | **Weak-Password** | 2021 CSAW-Quals | None *(text prompt)* | **OSINT / Hash Cracking:** Crack MD5 hash using target's name & DOB |
| 5 | `2022f-msc-farmlang` | **Farmlang** | 2022 CSAW-Finals | `farmlang.jpg` | **Esoteric Visual Language:** Decipher WiFi password from image |
| 6 | `2022q-msc-ezmaze` | **ezMaze** | 2022 CSAW-Quals | `attachment/maze.pt` | **Machine Learning:** PyTorch neural network weight tensor inspection |
| 7 | `2022q-msc-quantum_leap` | **quantum-leap** | 2022 CSAW-Quals | `output` | **Quantum Computing:** Reverse 2-qubit quantum logic circuit states |

*(The remaining 17 misc challenges require interactive Docker containers).*

---

## 5. Web Security Category (0 Truly Offline / 17 Online / 2 Code Dumps)

Web security challenges inherently evaluate interaction with live web endpoints:

* **17 Online Challenges:** Launch live web apps (Node.js, Flask, Spring Boot, PHP, etc.) via Docker Compose, requiring HTTP interaction (e.g., SQLi, XSS, SSRF, auth bypass, file upload).
* **2 Outlier Code Handouts (No Docker bundled):**
  * `2020f-web-sharkfacts` (**sharkfacts**, 2020 Finals): Provides `server.py` and links to an external domain (`http://sharks.alternativefacts.systems/`).
  * `2020f-web-snailrace1` (**snailrace1**, 2020 Finals): Provides `snailrace.tar.gz` and links to an external domain (`https://snail.racecraft.cf`).

*(If counting challenges with no local Docker container, Web has 2 offline code dumps out of 19. Conceptually, 0 are true offline CTF challenges).*

---

## 6. Master Reference Table of All Offline Benchmark IDs

| Category | Count / Total | Complete List of Offline Benchmark IDs |
| :--- | :---: | :--- |
| **Forensics** | **12 / 15** | `2017f-for-thoroughlystripped`<br>`2017q-for-missed_registration`<br>`2018q-for-simple_recovery`<br>`2018q-for-whyos`<br>`2021f-for-constela`<br>`2021q-for-lazy_leaks`<br>`2023f-for-emoji`<br>`2023f-for-floating_points`<br>`2023f-for-forensings`<br>`2023f-for-hypokrinesthai`<br>`2023q-for-1black0white`<br>`2023q-for-br3akth3vau1t` |
| **Cryptography** | **14 / 52** | `2017f-cry-ecxor`<br>`2017q-cry-almost_xor`<br>`2017q-cry-another_xor`<br>`2018q-cry-babycrypto`<br>`2018q-cry-collusion`<br>`2018q-cry-lowe`<br>`2019q-cry-des2bites`<br>`2020f-cry-hybrid2`<br>`2020q-cry-perfect_secrecy`<br>`2021f-cry-collision_course`<br>`2021q-cry-crack_me`<br>`2022f-cry-m_ster_0f_prn9`<br>`2022q-cry-not_too_taxing`<br>`2023q-cry-circles` |
| **Miscellaneous** | **7 / 24** | `2018f-msc-leaked_flag`<br>`2018q-msc-short_circuit`<br>`2019f-msc-alive`<br>`2021q-msc-weak_password`<br>`2022f-msc-farmlang`<br>`2022q-msc-ezmaze`<br>`2022q-msc-quantum_leap` |
| **Web Security** | **0 / 19** *(or 2)* | *(No container bundled, code dump only)*:<br>`2020f-web-sharkfacts`<br>`2020f-web-snailrace1` |

---

## 7. Additional On-Disk Unindexed Challenges

The following 8 directories reside on disk under `test/2018/CSAW-Quals/` and `test/2018/CSAW-Finals/` but are omitted from `test_dataset.json`:

* **Forensics (Offline):**
  * `test/2018/CSAW-Quals/forensics/rewind` (Memory dump strings)
  * `test/2018/CSAW-Quals/forensics/mcgriddle` (Network capture `final.pcap`)
* **Cryptography (Offline):**
  * `test/2018/CSAW-Quals/crypto/holywater` (Lattice cryptography script `lattice.py`)
  * `test/2018/CSAW-Finals/crypto/holywater2` (SecondLife text puzzle `description.txt`)
* **Web (Online):**
  * `test/2018/CSAW-Quals/web/nvs`
  * `test/2018/CSAW-Quals/web/movie_club`
  * `test/2018/CSAW-Quals/web/wtf_sql`
  * `test/2018/CSAW-Quals/web/sso`
