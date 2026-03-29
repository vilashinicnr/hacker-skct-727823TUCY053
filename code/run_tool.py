# YOUR FULL NAME | 727823TUCY053
# student_name: YOUR FULL NAME
# roll_number: 727823TUCY053
# project_name: RFIDNFCSecurityTester
# date: 2025-01-28

import datetime, subprocess, sys, os

ROLL_NUMBER = "727823TUCY053"
print(f"Roll Number: {ROLL_NUMBER} | Timestamp: {datetime.datetime.now()}")

print("\n[*] Launching RFID/NFC Security Tester...\n")

tool_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tool_main.py")

result = subprocess.run([sys.executable, tool_path])

if result.returncode == 0:
    print(f"\n[OK] Tool executed successfully at {datetime.datetime.now()}")
    print(f"[OK] Roll Number: 727823TUCY053")
else:
    print(f"\n[ERROR] Tool exited with code: {result.returncode}")
