import asyncio

import httpx
from bs4 import BeautifulSoup

from constants import SAMPLE_URL


async def make_request(url: str) -> str:
    async with httpx.AsyncClient() as aclient:
        response = await aclient.get(url)
    return response.text


async def product_page_scraper(url: str):
    page = await make_request(url)
    soup = BeautifulSoup(page, "lxml")
    print(soup.prettify())


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(product_page_scraper(SAMPLE_URL))
