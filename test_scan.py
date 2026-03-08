import asyncio
from core.scanner import GhostScanner

async def test():
    target = "https://tayseerme.com"
    scanner = GhostScanner(target)
    print(f"[*] Starting test scan for {target}")
    await scanner.start()
    print("[*] Scan finished")

if __name__ == "__main__":
    asyncio.run(test())
