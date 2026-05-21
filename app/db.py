import sqlite3

database = 'database'

def get_connection():
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    return conn