from pathlib import Path

from dotenv import dotenv_values

PROJ_DIR = Path(__file__).parents[1]
SRC = PROJ_DIR.joinpath("src")
ENV = PROJ_DIR.joinpath(".env")

SAMPLE_IMAGE = dotenv_values(ENV).get("SAMPLE_IMAGE")
SAMPLE_URL = dotenv_values(ENV).get("SAMPLE_URL")
LINKS_URL = dotenv_values(ENV).get("LINKS_URL")
