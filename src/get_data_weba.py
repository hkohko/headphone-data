import json

import httpx

from constants import LINKS_URL  # type: ignore


def postman_paste() -> None:
    # write_header(headers)
    # write_payload(payload)
    pass


def write_header(obj: dict) -> None:
    with open("headers.json", "w") as headerfile:
        json.dump(obj, headerfile)


def write_payload(obj: dict) -> None:
    with open("payload.json", "w") as payloadfile:
        json.dump(obj, payloadfile)


def create_samplefile() -> None:
    with open("headers.json") as headerfile:
        headers = json.load(headerfile)
    with open("payload.json") as payloadfile:
        payload = json.loads(json.dumps(payloadfile.read()))
    response = httpx.post(LINKS_URL, headers=headers, data=payload)
    with open("sample_response.json", "w") as sample_file:
        json.dump(response.json(), sample_file)


def parse_json() -> None:
    with open("sample_response.json") as sample_file:
        file = json.load(sample_file)
    data = file.get("data")
    products = data.get("products")
    print(len(products))


if __name__ == "__main__":
    parse_json()
