

import sqlite3


def db(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS utilisateurs(nom TEXT, prenom TEXT, email TEXT, mdp TEXT)" )
    print("\n Tables utilisateur créer")

    utilisateur = [("Lossou", "Stephane", "stephanelossou@gmail.com", "1234"),
                    ("Ferbeck", "Nicolas", "nicolito@bogoss.net", "1234"),
                    ("Lossou", "Arthur", "alossou@bogoss.net", "1234")]
    cur.executemany("INSERT INTO utilisateurs VALUES (?, ?, ?, ?)", utilisateur)

    print("\n3 users add")

    cur.execute("SELECT * FROM utilisateurs")
    tmp = cur.fetchall()
    for i in tmp:
        print(f"{i[0]}\t {i[1]}\t {i[2]}\t {i[3]})")
    
    cur.execute("CREATE TABLE IF NOT EXISTS cocktails(nom_cocktail TEXT, description TEXT, recette TEXT)")

    print("\n Table cocktail créer")

    listCocktail = [("Gin Tonic","\nDescription: Bonne petite bouteille de gin venu des tropiques servie avec du bon Schweppes tonic sortie du frigo",
                    "\nRecette:\nGin --> 4 cl\nTonic --> 1 bouteille 25 cl \nGlaçon\nlamel de citron")]
    
    cur.executemany("INSERT INTO cocktails VALUES (?,?,?)", listCocktail)

    print("1 cocktail ajouté")

    cur.execute("SELECT * FROM cocktails")
    tmp2 = cur.fetchall()
    for i in tmp2:
        print(f"{i[0]}\t {i[1]}\t {i[2]}")

    cur.execute("CREATE TABLE IF NOT EXISTS ingredients(nom TEXT, quantiter TEXT)")
    print("\n Tables ingredients créer")

    ingredients = [("Citron","1 l"),
                    ("Menthe","3 feuilles")]
                   

    
    cur.executemany("INSERT INTO ingredients VALUES (?,?)", ingredients)
    cur.execute("SELECT * FROM ingredients")
    tmp= cur.fetchall()
    for i in tmp:
        print(f"{i[0]},{i[1]}")

    cur.execute("CREATE TABLE IF NOT EXISTS alcools(nom TEXT, degrer TEXT)")
    print("\n Table alcool created ")

    alcools = [("GIN","45%"),
                ("Cointreau","50%"),
                ("Vodka","70%"),
                ("Tequila","60%")
                ]

    cur.executemany("INSERT INTO alcools VALUES (?,?)", alcools)
    cur.execute("SELECT * FROM alcools")
    tmp= cur.fetchall()
    for i in tmp:
        print(f"{i[0]},{i[1]}")

    cur.execute("CREATE TABLE IF NOT EXISTS type(type TEXT , gout TEXT)")
    print("\n Table Type created ")

    types = [("Rhum","Rhum"),
                ("Tequila","Tequila"),
                ("Vodka","Vodka"),
                ("Gin","Gin")
                ]

    cur.executemany("INSERT INTO type VALUES (?,?)", types)
    cur.execute("SELECT * FROM type")
    tmp= cur.fetchall()
    for i in tmp:
        print(f"{i[0]},{i[1]}")

      
if __name__ == "__main__":
    connection = sqlite3.connect("database.db")
    cur = connection.cursor()
    db(cur)