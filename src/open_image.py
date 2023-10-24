from io import BytesIO

import httpx
from dotenv import dotenv_values
from PIL import Image

from constants import ENV

key = dotenv_values(ENV)
url: str = key.get("SAMPLE_IMAGE")


def main():
    link = httpx.get(url)
    byte_img = BytesIO(link.content)
    img = Image.open(byte_img)
    img.show("sample")


if __name__ == "__main__":
    main()
