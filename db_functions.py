import sqlite3
import datetime

def get_notes():
    conn = sqlite3.connect("notes.db")
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    rows = db.execute('''
    SELECT * from notes
    ''').fetchall()

    conn.commit()
    conn.close()

    return [dict(ix) for ix in rows]

def get_note(noteID):
    conn = sqlite3.connect("notes.db")
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    rows = db.execute(f"SELECT * from notes WHERE noteID = {int(noteID)};").fetchall()

    conn.commit()
    conn.close()

    return [dict(ix) for ix in rows]

def delete_note(noteID):
    conn = sqlite3.connect("notes.db")
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    db.execute(f"DELETE FROM notes WHERE noteID={int(noteID)};")
    conn.commit()
    conn.close()

def add_note(noteData):
    conn = sqlite3.connect("notes.db")
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    insert = "INSERT INTO notes (title, content, date) VALUES (?, ?, ?)"

    print(noteData)

    data = (noteData["title"], noteData["content"], datetime.datetime.now())

    db.execute(insert, data)
    conn.commit()
    conn.close()
    print("Completed")

def update_note(noteData):
    data = (noteData["title"], noteData["content"], datetime.datetime.now(), noteData["noteID"])

    print(data)

    conn = sqlite3.connect("notes.db")
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    command = "UPDATE notes SET title = ?, content = ?, date = ? WHERE noteID = ?"

    db.execute(command, data)
    conn.commit()
    conn.close()