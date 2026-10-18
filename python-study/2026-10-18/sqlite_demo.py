import sqlite3

conn = sqlite3.connect("demo.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        done INTEGER NOT NULL DEFAULT 0
    )
""")

cur.execute("INSERT INTO todos (content, done) VALUES (?, ?)", ("买菜", 0))
cur.execute("INSERT INTO todos (content, done) VALUES (?, ?)", ("写作业", 0))
cur.execute("INSERT INTO todos (content, done) VALUES (?, ?)", ("健身", 1))
cur.execute("UPDATE todos SET done = ? WHERE id = ? ", (1,2))
cur.execute("DELETE FROM todos WHERE id = ?", (3,))

print("---修改后---")

for row in cur.execute("SELECT * FROM todos"):
    print(row)

conn.commit()
conn.close()