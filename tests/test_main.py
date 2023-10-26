import json
from pathlib import Path

from constants import JSON_FILES
from src.data.headphone_db_query import connect


def open_file():
    filepaths: list[Path] = []
    for file in Path(JSON_FILES).iterdir():
        filepaths.append(file)
    print(filepaths)
    for path in filepaths:
        if path.suffix != "json":
            continue
        with open(path) as jsonfile:
            json.load(jsonfile)
        print(path)


def query_db():
    Q_TEST_SELECT = "SELECT name, url FROM headphone ORDER BY name ASC LIMIT 10"
    with connect() as conn:
        cur = conn.cursor()
        cur.execute(Q_TEST_SELECT)
        for result in cur:
            print(result)


if __name__ == "__main__":
    open_file()
    query_db()
