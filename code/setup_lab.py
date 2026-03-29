# YOUR FULL NAME | 727823TUCY053
# student_name: YOUR FULL NAME
# roll_number: 727823TUCY053
# project_name: RFIDNFCSecurityTester
# date: 2025-01-28

import subprocess, datetime, sys

ROLL_NUMBER = "727823TUCY053"
print(f"Roll Number: {ROLL_NUMBER} | Timestamp: {datetime.datetime.now()}")

packages = ["colorama", "tabulate", "pycryptodome", "pyyaml", "requests"]

print("\n[*] Installing required Python packages...")
for pkg in packages:
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", pkg, "--break-system-packages"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        print(f"  [+] {pkg} installed successfully")
    else:
        print(f"  [!] Failed: {pkg} -> {result.stderr.strip()}")

print("\n[*] Verifying system tools...")
tools = ["nmap", "wireshark"]
for tool in tools:
    r = subprocess.run(["which", tool], capture_output=True, text=True)
    status = "Found" if r.returncode == 0 else "NOT FOUND"
    print(f"  {tool}: {status}")

print(f"\n[OK] Lab setup complete at {datetime.datetime.now()}")
print(f"[OK] Roll Number: 727823TUCY053")
