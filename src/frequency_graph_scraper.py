import asyncio
import re

import httpx
from bs4 import BeautifulSoup

from constants import JSON_FILES, SAMPLE_URL


async def make_request(url: str) -> str:
    async with httpx.AsyncClient() as aclient:
        response = await aclient.get(url)
    return response.text


def open_page() -> str:
    with open(JSON_FILES.joinpath("sample_response.html")) as file:
        html = file.read()
    return html


async def change_img_size(url: str, image_size: str) -> str:
    sizes = ("tiny", "small", "medium", "large")
    newline = "\n"
    if image_size not in sizes:
        raise ValueError(f"Allowed sizes:\n{newline.join(sizes)}")
    pattern = r"(\w+)(\.jpg)"
    change_image_size = re.sub(pattern, rf"{image_size}\g<2>", url)
    return change_image_size


async def frequency_response_img(url: str, img_size: str) -> str:
    page = await make_request(url)
    soup = BeautifulSoup(page, "lxml")
    div = soup.find("div", {"class": "product_page", "data-part": "ProductPage"})
    div2 = div.find("div", {"class": "product_page-test_results is-using-categories"})
    div3 = div2.find("div", {"class": "product_page-test_results-content"})
    div4 = div3.find("div", {"class": "e-simple_grid is-aligned"})
    div5 = div4.find("div", {"data-id": "7902"})
    a = div5.find("a", {"class": "simple_image-link"})
    img_url = a.find("img").get("src")
    resized_img = await change_img_size(img_url, img_size)
    return resized_img


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        print(runner.run(frequency_response_img(SAMPLE_URL, "medium")))
