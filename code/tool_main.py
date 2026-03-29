# student_name: YOUR FULL NAME
# roll_number: 727823TUCY053
# project_name: RFIDNFCSecurityTester
# date: 2025-01-28

"""
RFID/NFC Security Tester - Main Tool
Simulates RFID/NFC tag scanning and vulnerability assessment.
"""

import random
import datetime
from colorama import Fore, Style, init
from tabulate import tabulate

init(autoreset=True)

ROLL_NUMBER = "727823TUCY053"
print(f"[*] Roll Number: {ROLL_NUMBER} | Started: {datetime.datetime.now()}")

DEFAULT_KEYS = [
    "FFFFFFFFFFFF",
    "A0A1A2A3A4A5",
    "D3F7D3F7D3F7",
    "000000000000",
    "B0B1B2B3B4B5",
]

def generate_uid():
    return ":".join([f"{random.randint(0,255):02X}" for _ in range(4)])

def simulate_tag_scan(tag_type="MIFARE_Classic"):
    uid = generate_uid()
    timestamp = datetime.datetime.now().isoformat()
    tag = {
        "uid": uid,
        "type": tag_type,
        "timestamp": timestamp,
        "sectors": random.randint(16, 64),
        "manufacturer": random.choice(["NXP", "HID Global", "EM Micro"]),
    }
    print(Fore.GREEN + f"[SCAN] Tag detected: UID={uid}, Type={tag_type}, Time={timestamp}")
    return tag

def test_default_keys(tag):
    print(Fore.YELLOW + f"\n[TEST] Checking default keys for UID: {tag['uid']}")
    vulnerable_sectors = []
    for sector in range(min(tag["sectors"], 8)):
        key = random.choice(DEFAULT_KEYS)
        if random.random() < 0.4:
            vulnerable_sectors.append({"sector": sector, "key": key})
            print(Fore.RED + f"  [!] Sector {sector}: VULNERABLE - default key {key}")
        else:
            print(Fore.GREEN + f"  [+] Sector {sector}: Protected")
    return vulnerable_sectors

def test_uid_clonability(tag):
    print(Fore.YELLOW + f"\n[TEST] Checking UID clone vulnerability: {tag['uid']}")
    clonable = tag["type"] in ["MIFARE_Classic", "EM4100"]
    if clonable:
        print(Fore.RED + f"  [!] UID {tag['uid']} is CLONABLE - card does not enforce UID locking")
    else:
        print(Fore.GREEN + f"  [+] UID locking enforced - clone attack mitigated")
    return clonable

def test_data_encryption(tag):
    print(Fore.YELLOW + f"\n[TEST] Checking data encryption on tag: {tag['uid']}")
    raw_data = bytes([random.randint(0, 255) for _ in range(16)])
    is_encrypted = not (raw_data == bytes(16) or raw_data[:4] == b'\x00\x00\x00\x00')
    print(f"  Raw sector data: {raw_data.hex()}")
    if is_encrypted:
        print(Fore.GREEN + "  [+] Data appears encrypted")
    else:
        print(Fore.RED + "  [!] Data appears UNENCRYPTED or uses null padding")
    return is_encrypted

def generate_report(results):
    print(Fore.CYAN + "\n" + "="*60)
    print(Fore.CYAN + "     RFID/NFC SECURITY ASSESSMENT REPORT")
    print(Fore.CYAN + f"     Roll Number: 727823TUCY053")
    print(Fore.CYAN + "="*60)
    table = []
    for r in results:
        table.append([
            r["uid"],
            r["type"],
            "YES" if r["uid_clonable"] else "NO",
            len(r["vulnerable_sectors"]),
            "NO" if r["data_encrypted"] else "YES",
        ])
    headers = ["UID", "Tag Type", "Clonable?", "Weak Key Sectors", "Unencrypted?"]
    print(tabulate(table, headers=headers, tablefmt="grid"))
    print(f"\n[*] Scan completed at: {datetime.datetime.now()}")
    print(f"[*] Roll Number: 727823TUCY053")

def run_test_case(tag_type, label):
    print(Fore.CYAN + f"\n{'='*60}")
    print(Fore.CYAN + f" TEST CASE: {label}")
    print(Fore.CYAN + f"{'='*60}")
    tag = simulate_tag_scan(tag_type)
    vuln_sectors = test_default_keys(tag)
    clonable = test_uid_clonability(tag)
    encrypted = test_data_encryption(tag)
    return {
        "uid": tag["uid"],
        "type": tag_type,
        "vulnerable_sectors": vuln_sectors,
        "uid_clonable": clonable,
        "data_encrypted": encrypted,
    }

if __name__ == "__main__":
    results = []
    results.append(run_test_case("MIFARE_Classic",
        "Case 1 - MIFARE Classic 1K (Access Card Simulation)"))
    results.append(run_test_case("NTAG215",
        "Case 2 - NTAG215 (NFC Sticker Simulation)"))
    results.append(run_test_case("EM4100",
        "Case 3 - EM4100 (125kHz Legacy Card Simulation)"))
    generate_report(results)
