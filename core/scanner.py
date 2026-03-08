import asyncio, aiohttp, random
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

class GhostScanner:
    def __init__(self, target):
        self.target = target
        self.domain = urlparse(target).netloc
        self.visited = set()

    async def start(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept-Encoding": "gzip, deflate"
        }
        async with aiohttp.ClientSession(headers=headers) as session:
            await self.scan(session, self.target)

    async def scan(self, session, url):
        if url in self.visited: return
        self.visited.add(url)
        print(f"[*] Scanning: {url}")
        try:
            async with session.get(url, timeout=10) as r:
                if r.status != 200:
                    print(f"[!] Failed to access {url}: Status {r.status}")
                    return
                text = await r.text()
                soup = BeautifulSoup(text, "html.parser")
                for a in soup.find_all("a", href=True):
                    link = urljoin(url, a['href'])
                    if self.domain in link: 
                        await self.scan(session, link)
        except Exception as e:
            print(f"[!] Error scanning {url}: {str(e)}")