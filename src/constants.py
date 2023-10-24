from pathlib import Path

PROJ_DIR = Path(__file__).parents[1]
SRC = PROJ_DIR.joinpath("src")
ENV = PROJ_DIR.joinpath(".env")
