# RFID/NFC Security Tester

**Student:** VILASHINI V
**Roll Number:** 727823TUCY053
**Category:** RFID/NFC Security
**Project Folder:** SKCT_727823TUCY053_RFIDNFCSecurityTester

## Tools Used
- Python 3, colorama, tabulate, pycryptodome, pyyaml

## Lab Environment
- VirtualBox + Kali Linux VM
- Metasploitable2 (isolated network)

## Setup Steps
```bash
pip3 install -r requirements.txt
python3 code/setup_lab.py
```

## Usage
```bash
python3 code/tool_main.py        # Run all 3 test cases
python3 code/analyze_results.py  # View risk analysis
```

## Tool Capability
Simulates RFID/NFC tag scanning and tests for default key vulnerabilities,
UID clonability, and unencrypted data storage across MIFARE Classic,
NTAG215, and EM4100 tag types.
