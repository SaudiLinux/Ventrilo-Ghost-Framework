import asyncio
import aiohttp
import random
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class GhostScanner:
    def __init__(self, target):
        self.target = target
        self.domain = target.split('//')[-1].split('/')[0]
        self.visited = set()
        self.user_agents = ["Mozilla/5.0 Chrome/120.0", "Mozilla/5.0 Firefox/119.0"]

    async def get_headers(self):
        return {"User-Agent": random.choice(self.user_agents), "X-Forwarded-For": "1.2.3.4"}

    async def scan_page(self, session, url):
        if url in self.visited: return
        self.visited.add(url)
        print(f"[*] فحص عميق: {url}")
        try:
            async with session.get(url, headers=await self.get_headers(), timeout=10) as r:
                html = await r.text()
                soup = BeautifulSoup(html, "html.parser")
                # استخراج الروابط (Spidering)
                for a in soup.find_all("a", href=True):
                    link = urljoin(url, a['href']).split("#")[0]
                    if self.domain in link:
                        await self.scan_page(session, link)
        except: pass

    async def run(self):
        async with aiohttp.ClientSession() as session:
            await self.scan_page(session, self.target)
