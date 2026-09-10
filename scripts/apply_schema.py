import sqlite3

# Path to your DB
db_path = r"C:\BLUESTOCK PROJECTS\nifty100\db\nifty100.db"

# Read schema.sql
with open(r"C:\BLUESTOCK PROJECTS\nifty100\db\schema.sql", "r") as f:
    schema_sql = f.read()

# Connect and apply schema
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.executescript(schema_sql)
conn.commit()
conn.close()

print("✅ Schema applied successfully to nifty100.db")
