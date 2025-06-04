import uuid
import sqlite3

class UserProfile:
    def __init__(self, name: str, age: int, height_cm: float, weight_kg: float, body_fat_pct: float, objective: str):
        self.user_id = str(uuid.uuid4())
        self.name = name
        self.age = age
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.body_fat_pct = body_fat_pct
        self.objective = objective

    def to_dict(self):
        return self.__dict__

    def save_to_db(self):
        conn = sqlite3.connect("session.db")
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                name TEXT,
                age INTEGER,
                height_cm REAL,
                weight_kg REAL,
                body_fat_pct REAL,
                objective TEXT
            )
        """)
        c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)", (
            self.user_id,
            self.name,
            self.age,
            self.height_cm,
            self.weight_kg,
            self.body_fat_pct,
            self.objective
        ))
        conn.commit()
        conn.close()