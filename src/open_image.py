from io import BytesIO

import httpx
from PIL import Image

from constants import SAMPLE_IMAGE


def main() -> None:
    link = httpx.get(SAMPLE_IMAGE)
    byte_img = BytesIO(link.content)
    img = Image.open(byte_img)
    img.show("sample")
    img.close()


if __name__ == "__main__":
    main()
