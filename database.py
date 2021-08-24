#coding:utf-8
import sqlite3
from sqlite3 import Connection

import db

def getUser(co, id):
    co.row_factory = sqlite3.Row
    return co.execute("SELECT * FROM utilisateurs WHERE rowid=?",(id,)).fetchone()

def charger(path: str):
    co = sqlite3.connect(path)
    creerTable(co)
    return co


def creerTable(co):
    if co.execute("SELECT count() FROM sqlite_master WHERE type=\"table\" AND name=\"utilisateurs\"").fetchone()[0] == 0:
        print("Table n'existe pas")
        db.db(co)
        co.commit()

def getAllUsers(co):
    co.row_factory = sqlite3.Row
    return co.execute("SELECT rowid, * FROM utilisateurs").fetchall()

def getAllCocktail(co):
    co.row_factory = sqlite3.Row
    return co.execute("SELECT rowid, * FROM cocktails").fetchall()

def createUser(co: Connection, utilisateurs: dict):
    sql="""INSERT INTO utilisateurs(nom,prenom,email,mdp) VALUES (?,?,?,?)"""

    f_name = utilisateurs["nom"]
    l_name = utilisateurs["prenom"]
    mail = utilisateurs["email"]
    mdp = utilisateurs["pwd"]
    utilisateurs["id"] = co.execute(sql, (str(f_name),str(l_name),str(mail),str(mdp))).lastrowid
    
    co.commit()
    return utilisateurs

def deleteCocktails(co, rowid: int):
    co.execute("DELETE FROM cocktails where rowid = ? ",(rowid,))
    co.commit()

def createcocktail(co, cocktails):
    sql = """INSERT INTO cocktails(nom_cocktail,description,recette) VALUES (?,?,?)"""

    name = cocktails["nom_cocktail"]
    description = cocktails["description"]
    recette = cocktails["recette"]
    cocktails["id"] = co.execute(sql,(name,description,recette))

    co.commit()
    return cocktails

def updateCocktail(co, cocktails: dict):
    sql = """UPDATE cocktails SET nom_cocktail=?, description=?,recette=? WHERE rowid=?"""

    id=cocktails["id"]
    nom_cocktail = cocktails["nom_cocktail"]
    description = cocktails["description"]
    recette= cocktails["recette"]

    co.execute(sql,(str(nom_cocktail),str(description),str(recette), int(id)))
    co.commit()

def lire(co, rowid):
    co.row_factory = sqlite3.Row
    return co.execute("SELECT rowid, * FROM cocktails WHERE rowid=?", (rowid,)).fetchone()