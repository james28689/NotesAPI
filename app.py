from flask import Flask, request
from flask_cors import CORS, cross_origin
import json, sqlite3, os, time
from db_functions import *

# Sets up app with CORS
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

conn = sqlite3.connect("notes.db")
db = conn.cursor()

@app.route('/getNotes')
def getNotes():
    # returns all notes from notes.db
    return json.dumps(get_notes())

@app.route('/getNote/<noteID>')
def getNote(noteID):
    note = get_note(noteID)
    return json.dumps(note)

@app.route('/deleteNote/<noteID>')
def deleteNote(noteID):
    if delete_note(noteID):
        return json.dumps("Done")
    else:
        return json.dumps("Did not complete")

@app.route('/addNote', methods=['POST'])
def addNote():
    jsonData = request.get_json()
    add_note(jsonData)
    return request.get_json()

@app.route('/updateNote', methods=['PUT'])
def updateNote():
    jsonData = request.get_json()
    update_note(jsonData)
    return json.dumps("Done")

# Runs the app, with auto-generated certs for benwilliamson.org
if __name__ == "__main__":
    app.run(debug=True)