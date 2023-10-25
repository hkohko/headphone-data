import sqlite3
from typing import Any

from constants import DB


def connect() -> sqlite3.Connection:
    return sqlite3.connect(DB)


def create_table():
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
