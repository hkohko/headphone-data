import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from constants import PRODUCT_IDENT_NAME, PRODUCT_IDENT_PATH, SAMPLE_RESPONSE_PATH
from decors import insert_to_headphone_db, write_result


@write_result(PRODUCT_IDENT_NAME)
def parse_json(sample_response: tuple[Path]) -> str:
    with open(*sample_response) as sample_file:
        file = json.load(sample_file)
    data = file.get("data")
    products = data.get("products")
    defaultdict(str)
    result = []
    for product in products:
        name = product.get("fullname")
        page = product.get("page")
        url = page.get("url")
        result.append({"name": name, "url": url})
    return json.dumps(result)


@insert_to_headphone_db
def open_product_ident(product_identity: tuple[Path]) -> list[dict[str, Any]]:
    with open(product_identity[0]) as file:
        jsonfile = json.load(file)
    return jsonfile


if __name__ == "__main__":
    parse_json(SAMPLE_RESPONSE_PATH)
    open_product_ident(PRODUCT_IDENT_PATH)
