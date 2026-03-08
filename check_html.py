import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch():
    url = "https://tayseerme.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Encoding": "gzip, deflate"
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as r:
            text = await r.text()
            print(f"[*] Length: {len(text)}")
            print(f"[*] First 1000 chars: {text[:1000]}")
            soup = BeautifulSoup(text, "html.parser")
            links = soup.find_all("a", href=True)
            print(f"[*] Links found: {len(links)}")
            for a in links[:10]:
                print(f"[*] Link: {a['href']}")

if __name__ == "__main__":
    asyncio.run(fetch())
