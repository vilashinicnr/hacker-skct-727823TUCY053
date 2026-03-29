# YOUR FULL NAME | 727823TUCY053
# student_name: YOUR FULL NAME
# roll_number: 727823TUCY053
# project_name: RFIDNFCSecurityTester
# date: 2025-01-28

import datetime
from tabulate import tabulate

ROLL_NUMBER = "727823TUCY053"
print(f"Roll Number: {ROLL_NUMBER} | Timestamp: {datetime.datetime.now()}")

simulated_results = [
    {"uid": "A1:B2:C3:D4", "type": "MIFARE_Classic", "weak_sectors": 3,
     "clonable": True,  "encrypted": False},
    {"uid": "E5:F6:07:18", "type": "NTAG215",        "weak_sectors": 0,
     "clonable": False, "encrypted": True},
    {"uid": "22:33:44:55", "type": "EM4100",          "weak_sectors": 5,
     "clonable": True,  "encrypted": False},
]

print("\n[*] RFID/NFC Risk Analysis Summary:")
print(f"[*] Roll Number: 727823TUCY053\n")

table = [
    [r["uid"], r["type"], r["weak_sectors"],
     "YES" if r["clonable"] else "NO",
     "YES" if not r["encrypted"] else "NO"]
    for r in simulated_results
]
headers = ["UID", "Tag Type", "Weak Key Sectors", "Clonable?", "Unencrypted?"]
print(tabulate(table, headers=headers, tablefmt="grid"))

total = len(simulated_results)
vulnerable = sum(1 for r in simulated_results if r["clonable"] or r["weak_sectors"] > 0)

print(f"\n[*] Vulnerable Tags : {vulnerable}/{total}")
print(f"[*] Risk Level      : {'HIGH' if vulnerable >= 2 else 'MEDIUM'}")
print(f"[*] Recommendation  : Replace EM4100 and MIFARE Classic with MIFARE DESFire EV2")
print(f"\n[OK] Analysis complete at {datetime.datetime.now()}")
print(f"[OK] Roll Number: 727823TUCY053")
