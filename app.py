import requests
import pandas as pd
from datetime import datetime
import sys

print("#"*90)
print("     Author: Tal Sperling")
print("     Version: 1.0.0")
print("     This code is to be used for educational purposes or legal penetration testing only")
print("     I do not take responsibility for any misuse or illegal action/use of this code")
print("#"*90+"\n")

requests.adapters.DEFAULT_RETRIES = 2

try:
    file = open(sys.argv[1], 'r')
    Lines = file.readlines()

except Exception as e:
    print("[-] Error")
    print(e)


sites = []

start_time = datetime.now()

print("[+] Starting Scan")

for line in Lines:

    status = {"URL":[], "Status":[], "Comments":[], "Port":[]}

    print(f'[+] Scanning {line.strip()} on port 443')
    try:
        resp = requests.head(f'https://{line.strip()}')
      
        status = {"URL": line.strip(), "Port": "443", "Status": "UP", "Comments": resp.status_code}

    except Exception as e:
        status = {"URL": line.strip(), "Port": "443", "Status": "DOWN", "Comments": e}

    sites.append(status)

print("[+] End Of Scan")

dataDf = pd.DataFrame(sites)
print(dataDf)

file_name = 'scan_results.xlsx'

try:
    dataDf.to_excel(file_name)
    print('[+] Saved To Excel')
except Exception as e:
    print("[-] Error saving to excel")
    print(e)
        

end_time = datetime.now()

counter = ((start_time - end_time).total_seconds()) / 60
print(f'[+] Run time: {counter}')
    



