import sqlite3
import datetime

conn = sqlite3.connect("users.db")
db = conn.cursor()

db.execute("""CREATE TABLE users (
    userID INTEGER PRIMARY KEY,
    fullName TEXT,
    email TEXT,
    password TEXT,
    date TIMESTAMP
);""")

insert = "INSERT INTO users (fullName, email, password, date) VALUES (?, ?, ?, ?)"

data = ("James Watling", "james.watling@gmail.com", "qwerty123456", datetime.datetime.now())


db.execute(insert, data)
conn.commit()

def get_notes():
    with conn:
        db.execute("SELECT * FROM users")
        print(db.fetchall())


get_notes()