import sqlite3
import datetime

conn = sqlite3.connect("users.db")
db = conn.cursor()

db.execute("""CREATE TABLE notes (
    noteID INTEGER PRIMARY KEY,
    title TEXT,
    content TEXT,
    date TIMESTAMP
);""")

insert = "INSERT INTO notes (title, content, date) VALUES (?, ?, ?)"

data = ("test title", "test content", datetime.datetime.now())


db.execute(insert, data)
conn.commit()

def get_notes():
    with conn:
        db.execute("SELECT * FROM notes")
        print(db.fetchall())


get_notes()