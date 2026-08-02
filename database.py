import sqlite3

conn = sqlite3.connect("fingerprints.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS fingerprints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ssid TEXT,
    avg_rssi REAL,
    avg_latency REAL,
    channel TEXT,
    encryption TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")