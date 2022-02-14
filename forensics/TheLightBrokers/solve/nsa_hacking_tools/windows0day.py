from time import sleep
import sys
import os

print('''
 __          ___           _                    ___      _             
 \ \        / (_)         | |                  / _ \    | |            
  \ \  /\  / / _ _ __   __| | _____      _____| | | | __| | __ _ _   _ 
   \ \/  \/ / | | '_ \ / _` |/ _ \ \ /\ / / __| | | |/ _` |/ _` | | | |
    \  /\  /  | | | | | (_| | (_) \ V  V /\__ \ |_| | (_| | (_| | |_| |
     \/  \/   |_|_| |_|\__,_|\___/ \_/\_/ |___/\___/ \__,_|\__,_|\__, |
                                                                  __/ |
                                                                 |___/ 
''')
sleep(0.2)
if len(sys.argv) < 2:
    print(f"[*] Usage: {sys.argv[0]} -t <target-ip>")
    sys.exit()
print("[+] Scanning Target's ports:",flush=True,end="")
for i in range(20):
    sleep(0.4)
    print("#",flush=True,end="")
print("#")

print("[+] Getting RCE:",flush=True,end="")
for i in range(10):
    sleep(0.4)
    print("#",flush=True,end="")
print("#")
print("[+] Congrats your in the system hack away!!!")
print("Microsoft Windows 6.1.7601\r\n\r\n")
while(1):
    cmd = input("C:\\Windows\\System32>")
    print(os.popen(cmd).readline())
