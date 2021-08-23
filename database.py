import sqlite3
from sqlite3 import Connection

import db

def getUser(cur, id):
    cur.row_factory = sqlite3.Row
    return cur.execute("SELECT * FROM utilisateurs WHERE rowid=?", (id,)).fetchone()

def charger(path: str):
    cur = sqlite3.connect(path)
    creerTable(cur)
    return cur


def creerTable(cur):
    if cur.execute("SELECT count() FROM sqlite_master WHERE type=\"table\" AND name=\"utilisateurs\"").fetchone()[0] == 0:
        print("Table n'existe pas")
        db.db(cur)
        cur.commit()

def getAllUsers(cur):
    cur.row_factory = sqlite3.Row
    return cur.execute("SELECT rowid, * FROM utilisateurs").fetchall()