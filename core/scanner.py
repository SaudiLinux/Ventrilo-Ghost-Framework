import asyncio, aiohttp, random
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

class GhostScanner:
    def __init__(self, target):
        self.target = target
        self.domain = urlparse(target).netloc
        self.visited = set()

    async def start(self):
        async with aiohttp.ClientSession() as session:
            await self.scan(session, self.target)

    async def scan(self, session, url):
        if url in self.visited: return
        self.visited.add(url)
        print(f"[*] Scanning: {url}")
        try:
            async with session.get(url, timeout=5) as r:
                soup = BeautifulSoup(await r.text(), "html.parser")
                for a in soup.find_all("a", href=True):
                    link = urljoin(url, a['href'])
                    if self.domain in link: await self.scan(session, link)
        except: pass