import sqlite3

def init_db():
    conn = sqlite3.connect("session.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS session (
            timestamp TEXT, heart_rate INTEGER, feedback TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_sqlite(hr, feedback):
    conn = sqlite3.connect("session.db")
    c = conn.cursor()
    c.execute("INSERT INTO session VALUES (datetime('now'), ?, ?)", (hr, feedback))
    conn.commit()
    conn.close()
