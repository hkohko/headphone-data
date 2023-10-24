import json
from collections import defaultdict

from constants import JSON_FILES


def parse_json() -> defaultdict[str, str]:
    with open(JSON_FILES.joinpath("sample_response.json")) as sample_file:
        file = json.load(sample_file)
    data = file.get("data")
    products = data.get("products")
    product_identity: defaultdict[str, str] = defaultdict(str)
    for idx, product in enumerate(products):
        name = product.get("fullname")
        page = product.get("page")
        url = page.get("url")
        product_identity[name] = url
    return product_identity


if __name__ == "__main__":
    parse_json()
