import aiohttp
from bs4 import BeautifulSoup as bs

from .constant import BASE_URL


class GoogleTranslate:
    """Translate text from https://translate.google.com/m"""

    def __init__(self, tl, text) -> None:
        self.sl = "auto"
        self.tl = tl
        self.text = text
        self.params = {
            "sl": self.sl,
            "tl": self.tl,
            "q": self.text,
            "hl": "en"
        }

    async def translate(self) -> str:
        url = BASE_URL
        connector = aiohttp.TCPConnector(limit=50)
        async with aiohttp.ClientSession(connector=connector) as session:
            res = await session.get(url=url, params=self.params)
            result = await res.text()

            # find translate
            translation = await self.find_translation(result)
            return translation


    async def find_translation(self, res):
        soup = bs(res, 'html.parser')
        translation = soup.find_all("div", {"class":"result-container"})[0].text
        return translation

    