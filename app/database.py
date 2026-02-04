import sqlite3

DATABASE = "ordenes.db"

def get_connection():
    return sqlite3.connect(DATABASE)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ordenes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            estado TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
