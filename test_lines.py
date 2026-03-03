import sqlite3
from main import DB_NAME

conn = sqlite3.connect(DB_NAME)
c = conn.cursor()
c.execute("SELECT p.id, e.content FROM papers p JOIN edits e ON p.id = e.paper_id ORDER BY e.version DESC LIMIT 1")
row = c.fetchone()
lines = row[1].splitlines()
for i in range(5):
    print(f"{i}: {repr(lines[i])}")
