import sqlite3
from flask import g, session
import json
import os.path

DATABASE = 'db.db'

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def execute(query, args=()):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, DATABASE)

    con = sqlite3.connect(db_path)
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute(query, args)
    con.commit()
    rv = cur.fetchall()
    lastrowid = cur.lastrowid
    cur.close()
    return rv, lastrowid

def insertUser(email, password):
    rv,lastrowid = execute("INSERT INTO users (email, password) VALUES (?,?)", (email, password,))

def getUserWithEmail(email):
    rv,lastrowid = execute("SELECT * FROM users WHERE email=?", (email,))
    if len(rv) == 0:
        return False
    return rv[0]

def getUser(id=""):
    if id == "":
        id = session['id']

    rv,lastrowid = execute("SELECT * FROM users WHERE id=?", (id,))
    if len(rv) == 0:
        return False
    return rv[0]

def getBookmarks():
    rv,lastrowid = execute("SELECT bookmarks FROM users WHERE id=?", (session['id'],))
    if len(rv) == 0:
        return False
    return json.loads(rv[0]['bookmarks'])

def setBookmarks(bookmarks):
    rv,lastrowid = execute("UPDATE users SET bookmarks=? WHERE id=?;", (bookmarks, session['id'],))

def getUsersTheme():
    rv,lastrowid = execute("SELECT theme FROM users WHERE id=?", (session['id'],))
    if len(rv) == 0:
        return []
    return getTheme(rv[0]['theme'])

def setUsersTheme(theme):
    rv,lastrowid = execute("UPDATE users SET theme=? WHERE id=?", (theme, session['id'],))

def getTheme(id):
    rv,lastrowid = execute("SELECT * FROM themes WHERE id=?", (id,))
    if len(rv) == 0:
        return []
    return rv[0]

def getCSS(id):
    rv,lastrowid = execute("SELECT css FROM themes WHERE id=?", (id,))
    if len(rv) == 0:
        return []
    return rv[0]['css']

def getUsersCSS():
    theme = getUsersTheme()
    if theme == []:
        return "{}"
    else:
        return theme['css']

def getThemes():
    rv,lastrowid = execute("SELECT * FROM themes WHERE 1", ())
    for i in range(0, len(rv)):
        rv2, lastrowid2 = execute("SELECT Count(*) as ROWS FROM users WHERE theme=?", (rv[i]['id'],))
        rv[i]['active_users'] = rv2[0]['ROWS']
    return rv

def insertTheme(title, css):
    rv,lastrowid = execute("INSERT INTO themes (author, title, css) VALUES (?,?,?)", (session['id'], title, css,))
    return lastrowid

def setTheme(id, title, css):
    rv,lastrowid = execute("UPDATE themes SET title=?, css=? WHERE id=?;", (title, css, id,))
