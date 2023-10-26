import sqlite3

import src.decors as decors
from constants import DB, DB_DIR


@decors.create_dir(DB_DIR)
def connect() -> sqlite3.Connection:
    return sqlite3.connect(DB)
