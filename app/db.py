import sqlite3

database = 'database.db'

class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if not self.connection:
            self.connection = sqlite3.connect(database)
            self.connection.row_factory = sqlite3.Row
        return self.connection

db = Database()

def create_tables():
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS prestamo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        user_id INTEGER,
        amount REAL NOT NULL,
        interest_rate REAL NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL,
        FOREIGN KEY (client_id) REFERENCES clients (id),
        FOREIGN KEY (user_id) REFERENCES users (id)
    )""")
    conn.close()

def insert_user(username, email, password):
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    conn.commit()
    conn.close()

def insert_client(name, last_name, email, password, user_id):
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clients (name, last_name, email, password, user_id) VALUES (?, ?, ?, ?, ?)", (name, last_name, email, password, user_id))
    conn.commit()
    conn.close()

def insert_prestamo(client_id, user_id, amount, interest_rate, start_date, end_date):
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO prestamo (client_id, user_id, amount, interest_rate, start_date, end_date) VALUES (?, ?, ?, ?, ?, ?)", (client_id, user_id, amount, interest_rate, start_date, end_date))
    conn.commit()
    conn.close()

create_tables()

