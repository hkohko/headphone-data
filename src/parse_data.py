import json
from constants import JSON_FILES

def parse_json() -> None:
    with open(JSON_FILES.joinpath("sample_response.json")) as sample_file:
        file = json.load(sample_file)
    data = file.get("data")
    products = data.get("products")
    print(len(products))


if __name__ == "__main__":
    parse_json()
