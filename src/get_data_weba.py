import json
from pathlib import Path

import httpx

from constants import JSON_FILES, LINKS_URL  # type: ignore

if not Path(JSON_FILES).exists():
    Path(JSON_FILES).mkdir()

h_file = JSON_FILES.joinpath("headers.json")
p_file = JSON_FILES.joinpath("payload.json")
sample_response = JSON_FILES.joinpath("sample_response.json")
def postman_paste() -> None:
    # write_header(headers)
    # write_payload(payload)
    pass


def write_header(obj: dict) -> None:
    with open(h_file, "w") as headerfile:
        json.dump(obj, headerfile)


def write_payload(obj: dict) -> None:
    with open(p_file, "w") as payloadfile:
        json.dump(obj, payloadfile)


def create_samplefile() -> None:
    with open(h_file) as headerfile:
        headers = json.load(headerfile)
    with open(p_file) as payloadfile:
        payload = json.loads(json.dumps(payloadfile.read()))
    response = httpx.post(LINKS_URL, headers=headers, data=payload)
    with open(sample_response, "w") as sample_file:
        json.dump(response.json(), sample_file)


if __name__ == "__main__":
    pass
