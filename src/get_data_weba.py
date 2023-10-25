import json

import httpx

import decors
from constants import JSON_FILES, LINKS_URL

h_file = JSON_FILES.joinpath("headers.json")
p_file = JSON_FILES.joinpath("payload.json")
sample_response = JSON_FILES.joinpath("sample_response.json")


def postman_paste() -> None:
    # paste data from postman first
    # write_header(headers)
    # write_payload(payload)
    pass


@decors.create_dir(JSON_FILES)
def write_header(obj: tuple[dict]) -> None:
    with open(h_file, "w") as headerfile:
        json.dump(*obj, headerfile)


@decors.create_dir(JSON_FILES)
def write_payload(obj: tuple[dict]) -> None:
    with open(p_file, "w") as payloadfile:
        json.dump(*obj, payloadfile)


def create_samplefile() -> None:
    with open(h_file) as headerfile:
        headers = json.load(headerfile)
    with open(p_file) as payloadfile:
        payload = json.loads(json.dumps(payloadfile.read()))
    response = httpx.post(LINKS_URL, headers=headers, data=payload)
    with open(sample_response, "w") as sample_file:
        json.dump(response.json(), sample_file)


if __name__ == "__main__":
    postman_paste()
    create_samplefile()
