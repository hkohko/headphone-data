from typing import Any

from .db_main import connect


def create_table_image():
    Q_CREATE_TABLE = """CREATE TABLE IF NOT EXISTS imglink(
    id INTEGER,
    img_url TEXT UNIQUE,
    FOREIGN KEY(id) REFERENCES headphone(id)
    )
    """
    with connect() as conn:
        cur = conn.cursor()
        cur.execute(Q_CREATE_TABLE)


async def insert_into_db(data: dict[str, Any]):
    Q_INSERT_INTO = """INSERT OR IGNORE INTO imglink(
    id,
    img_url
    ) VALUES(
    :id,
    :img_url
    )
    """
    with connect() as conn:
        cur = conn.cursor()
        cur.execute(Q_INSERT_INTO, data)
        conn.commit()


if __name__ == "__main__":
    create_table_image()
