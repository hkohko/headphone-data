from typing import Any

from .db_main import connect


def create_headphone_table():
    Q_CREATE_TABLE = """CREATE TABLE IF NOT EXISTS headphone(
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    url TEXT
    )
    """
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(Q_CREATE_TABLE)


def insert_into_headphones(data: list[dict[str, Any]]):
    Q_INSERT_HEADPHONES = """INSERT OR IGNORE INTO headphone(
    name,
    url
    ) VALUES(
    :name,
    :url
    )
    """

    with connect() as conn:
        cursor = conn.cursor()
        cursor.executemany(Q_INSERT_HEADPHONES, data)
        conn.commit()


def query_all_data():
    Q_QUERY_TABLE = "SELECT * FROM headphone"
    with connect() as conn:
        cur = conn.cursor()
        cur.execute(Q_QUERY_TABLE)
        for id, name, url in cur:
            yield id, name, url
