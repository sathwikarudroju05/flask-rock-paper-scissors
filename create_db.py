import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    profile_name TEXT NOT NULL,
    wins INTEGER DEFAULT 0,
    lost INTEGER DEFAULT 0,
    score INTEGER DEFAULT 0
)
""")

conn.commit()
conn.close()

print("✅ Database created successfully")
