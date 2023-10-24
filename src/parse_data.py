import json
from collections import defaultdict

from constants import JSON_FILES
from decors import write_result


@write_result("product_identity.json")
def parse_json() -> defaultdict[str, str]:
    with open(JSON_FILES.joinpath("sample_response.json")) as sample_file:
        file = json.load(sample_file)
    data = file.get("data")
    products = data.get("products")
    product_identity: defaultdict[str, str] = defaultdict(str)
    for product in products:
        name = product.get("fullname")
        page = product.get("page")
        url = page.get("url")
        product_identity[name] = url
    return json.dumps(product_identity)


if __name__ == "__main__":
    parse_json()
