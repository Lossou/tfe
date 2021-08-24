#coding:utf-8

# CONCEPTION D’UNE APPLICATION DE RECETTES DE COCKTAILS
# By Lossou
"""
Projet conçu dans le cas de la préparation de mon épreuve intégrée pour mon travail de fin d'étude.
Epreuve intégrée préparée sous la supervision de Cédric VanConingsloo, professeur de programmation.
Présentée : le 25 Août 2021, devant Jury.
"""
# _*_ Coding: by Steph'


from os import name
import sqlite3
from sqlite3 import Connection
from tkinter import *
from tkinter import messagebox
import database as db
from tkinter.filedialog import askopenfilename
import tkinter

def updateCocktails():
    winUpdate = Toplevel()
    nom_cocktail = StringVar()
    description = StringVar()
    recettes = StringVar()

    frameAdd = LabelFrame(winUpdate)
    frameAdd2 = Frame(winUpdate)

    frameAdd.pack(pady=15)
    frameAdd2.pack()

    labelname = Label(frameAdd, text="Nom:")
    entryname = Entry(frameAdd, textvariable=nom_cocktail)
    labeldescript = Label(frameAdd, text="Description:")
    entrydescript = Entry(frameAdd, textvariable=description)
    labelRecette = Label(frameAdd, text="Recette:")
    entryrecette = Entry(frameAdd, textvariable=recettes)

    buttonAddCocktail = Button(frameAdd2, text="Modifier", command=lambda: validUpdate())
    buttonQuitCocktail = Button(frameAdd2, text="Quitter", command=lambda: quitwin(winUpdate))

    labelname.grid(pady=10)
    entryname.grid(row=0, column=1,pady=10)
    labeldescript.grid(row=1, column=0,pady=10)
    entrydescript.grid(row=1, column=1,pady=10)
    labelRecette.grid(row=2,column=0,pady=10)
    entryrecette.grid(row=2, column=1,pady=10)

    buttonAddCocktail.grid(padx=20)
    buttonQuitCocktail.grid(row=0, column=1)
    
    def validUpdate():
        id = lbCocktail.curselection() [0] + 1
        cocktail = {"id": id,"nom_cocktail":entryname.get(),"description":entrydescript.get(),"recette":entryrecette.get()}
        db.updateCocktail(c, cocktail)
        remplir()
        win.update()
        winUpdate.destroy()
       

def lbClick(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0] + 1
        cocktail = db.lire(c, index)
        entrynom.delete('1.0', END)
        entryDescription.delete('1.0', END)
        entryIngredient.delete('1.0', END)
        entrynom.insert('1.0',cocktail["nom_cocktail"])
        entryDescription.insert('1.0',cocktail["description"])
        entryIngredient.insert('1.0',cocktail["recette"])
     
def addCocktails():
    winAdd = Toplevel()
    winAdd.geometry("400x400")
    win.title("Ajouter votre cocktail")
    winAdd.resizable(False, False)
    winAdd.iconbitmap("logo1.ico")

    nom_cocktail = StringVar()
    description = StringVar()
    recettes = StringVar()

    frameAdd = LabelFrame(winAdd)
    frameAdd2 = Frame(winAdd)

    frameAdd.pack(pady=15)
    frameAdd2.pack()

    labelname = Label(frameAdd, text="Nom:")
    entryname = Entry(frameAdd, textvariable=nom_cocktail)
    labeldescript = Label(frameAdd, text="Description:")
    entrydescript = Entry(frameAdd, textvariable=description)
    labelRecette = Label(frameAdd, text="Recette:")
    entryrecette = Entry(frameAdd, textvariable=recettes)

    buttonAddCocktail = Button(frameAdd2, text="Ajouter", command=lambda: createCocktail())
    buttonQuitCocktail = Button(frameAdd2, text="Quitter", command=lambda: quitwin(winAdd))

    labelname.grid(pady=10)
    entryname.grid(row=0, column=1,pady=10)
    labeldescript.grid(row=1, column=0,pady=10)
    entrydescript.grid(row=1, column=1,pady=10)
    labelRecette.grid(row=2,column=0,pady=10)
    entryrecette.grid(row=2, column=1,pady=10)

    buttonAddCocktail.grid(padx=20)
    buttonQuitCocktail.grid(row=0, column=1)

    def createCocktail():
        cocktails = {"id": -1, "nom_cocktail":entryname.get(),"description":entrydescript.get(),"recette":entryrecette.get()}
        db.createcocktail(c, cocktails)
        remplir()
        win.update()
        winAdd.destroy()
        messagebox.showinfo("OK!","Vous avez ajouté un nouveau cocktail!")

def deletecocktail():
    id = lbCocktail.curselection() [0]+1
    db.deleteCocktails(c, id)
    remplir()
    messagebox.showwarning("Yep!","Vous venez de supprimer un cocktail ! avec succès")

def admin():
    winAdmin = Toplevel()
    winAdmin.geometry(f"400x400+{xLeft}+{yTop}")
    winAdmin.title("Connect Administrator")
    winAdmin.iconbitmap("logo1.ico")

    mailAdmin = str("stephanelossou@gmail.com")
    pwdAdmin = str("1234")

    frameAdmin = LabelFrame(winAdmin,text="Connect Master")
    frameAdmin2 = Frame(winAdmin)

    frameAdmin.pack(pady=20)
    frameAdmin2.pack()

    labelAdmin = Label(frameAdmin,text="Your mail: ")
    entryAdmin = Entry(frameAdmin,textvariable=mail, width=30)
    labelAdminPwd = Label(frameAdmin, text="Your password: ")
    entryAdminpwd = Entry(frameAdmin, textvariable=pwd, width=30)
    labelStatue = Label(frameAdmin,text="")

    buttonCon = Button(frameAdmin2, text="Connect", command=lambda: confirmed())
    ButtonQuit = Button(frameAdmin2, text="Quitter", command=lambda: quitwin(winAdmin))

    labelAdmin.grid(pady=10)
    entryAdmin.grid(row=0, column=1)
    labelAdminPwd.grid(row=1)
    entryAdminpwd.grid(row=1, column=1)
    labelStatue.grid(row=2, columnspan=2)

    buttonCon.grid(padx=25)
    ButtonQuit.grid(row=0, column=1)

    def confirmed():
        adminmail = entryAdmin.get()
        adminpwd = entryAdminpwd.get()
        if adminmail == mailAdmin and adminpwd == pwdAdmin:
            quitwin(winAdmin)
            addCocktail.config(state="normal")
            deleteCocktail.config(state="normal")
            updateCocktail.config(state="normal")
            messagebox.showinfo("Ok", "Vous êtes connecté !")
            win.update()
        else:
            labelStatue.config(text="Mot de passe ou utilisateur incorrect",fg="red")

def validConnect():
    cocktailMail = mail.get()
    cocktailPwd = pwd.get()
    if cocktailMail != "" and cocktailPwd != "":
        id = getID(cocktailMail)
        if id >= 0:
            user = db.getUser(c, id)
            if cocktailPwd == user["mdp"]:
                winAcceuil.destroy()
                win.update()
            else:
                labelStatusPwd.config(text="Mot de passe incorrect", fg="RED")
                winAcceuil.update()
        else:
            labelStatusPwd.config(text="L'utilisateur n'existe pas", fg="RED")
            winAcceuil.update()

def getID(email):
    tmp = db.getAllUsers(c)
    print("tmp créer")
    for i in tmp:
        print(f"{i[0]}{i[1]},{i[2]},{i[3]}")
        for user in tmp:
            print("user print")
            if email == user["email"]:
                return user["rowid"]
    print("retourne -1")
    return -1
    
def quitwin(window):
    window.destroy()

def remplir():
    lbCocktail.delete(0, END)

    for i in db.getAllCocktail(c):
        lbCocktail.insert(i["rowid"],f"{i['nom_cocktail']}")

def newuser():
    winNewUser = Toplevel()
    winNewUser.geometry(f"400x400+{xLeft}+{yTop}")
    winNewUser.title("New User")
    winNewUser.attributes("-topmost", True)
    winNewUser.iconbitmap("logo1.ico")
    frameNewUser = LabelFrame(winNewUser,text="Create a new user")
    frameNewUser2 = Frame(winNewUser)
    frameNewUser.pack(pady=20)
    frameNewUser2.pack()

    # Variable nécessaire
    firstName = StringVar()
    lastName = StringVar()
    mail = StringVar()
    pwd = StringVar()
    validPwd = StringVar()

    # première frame
    labelNom = Label(frameNewUser, text="Nom: ")
    entryNom = Entry(frameNewUser, width=30, textvariable= lastName)
    labelprenom = Label(frameNewUser, text="Prénom: ")
    entryprenom = Entry(frameNewUser, width=30,textvariable=firstName)
    labelMail = Label(frameNewUser, text="Email: ")
    entryMail = Entry(frameNewUser, width=30, textvariable=mail)
    labelPwd = Label(frameNewUser, text="Mot de passe: ")
    entryPwd2= Entry(frameNewUser, width=30, textvariable=pwd)
    labelValidPwd = Label(frameNewUser, text="Confirmer le mot de passe:")
    entryValidPwd = Entry(frameNewUser, width=30, textvariable=validPwd)
    labelStatusPwd = Label(frameNewUser, text="", fg="red")

    # deuxième frame
    buttonAdd = Button(frameNewUser2, text="Créer", command=lambda: validuser())
    buttonQuitter = Button(frameNewUser2, text="Quitter", command=lambda: quitwin(winNewUser))


    #Grid premiere frame
    labelNom.grid(pady=15)
    entryNom.grid(row=0, column=1, pady=15)
    labelprenom.grid(row=1, column=0, pady=15)
    entryprenom.grid(row=1,column=1, pady=15)
    labelMail.grid(row=2,column=0, pady=15)
    entryMail.grid(row=2, column=1, pady=15)
    labelPwd.grid(row=3,column=0, pady=15)
    entryPwd2.grid(row=3, column=1, pady=15)
    labelValidPwd.grid(row=4, column=0, pady=15)
    entryValidPwd.grid(row=4, column=1, pady=15)
    labelStatusPwd.grid(row=5, columnspan=2)

    # Grid deuxième frame
    buttonAdd.grid(padx=40)
    buttonQuitter.grid(row=0, column=1)

    def validuser():
        if entryPwd2.get() == entryValidPwd.get():
            utilisateurs = {"id":-1,"nom": entryNom.get(), "prénom": entryprenom.get(), "email": entryMail.get(), "pwd":entryPwd2.get()}
            db.createUser(c, utilisateurs)
            winNewUser.destroy()
            messagebox.showinfo("Bienvenue","Votre utilisateur a bien été crée!")
        else:
            labelStatusPwd.config(text="Mot de passe incorrect\n Veuillez réinscrire votre mot de passe")



# chemin de la db 
db_path = "database.db"

# Configuration du menu
win = Tk()
xLeft = int(win.winfo_screenwidth()//1 - 1400)
yTop = int(win.winfo_screenheight()//1 - 800)
win.geometry(f"1400x700+{xLeft}+{yTop}")
win.resizable(False, False)
win.config(bg="gray25")
win.title("My Cocktail Recipes")
win.iconbitmap("logo1.ico")
##
################
#
#  Widgets ...création des definitions et activation
#

def show_about():
    about_window = tkinter.Toplevel(win)
    about_window.title(" A propos")
    about_window.geometry("350x600")
    about_window.iconbitmap("logo1.ico")
    lb = tkinter.Label(about_window, text="|||| !!!! PAGE EN COURS DE CONSTRUCTION!!!! |||||")
    messagebox.showinfo("A vous revoir!", "|||| !!!! PAGE EN COURS DE CONSTRUCTION!!!! |||||\nMerci pour la compréhension")
    lb.pack()



def open_file():
    file = askopenfilename(title="Choisisez le fichierà ouvrir ",
            filetypes=[("PNG image", ".png"), ("GIF image", ".gif"), ("All files", ".*")])
    print(file)


def save_as():
    file = tkinter.filedialog.asksaveasfile(title="Enregistrer sous … un fichier",
            filetypes=[('CSV files', '.csv')])
    print(file.name)


def show_admin():
    about_admin = tkinter.Toplevel(win)
    about_admin.title("Contactez l'Administrateur")
    about_admin.geometry("250x150")
    about_admin.iconbitmap("logo1.ico")
    lb1 = tkinter.Label(about_admin, text="\nstephanelossou@gmail.com \n Stéphane Lossou")
    messagebox.showinfo("Ecrivez-nous!", "RDV sur https://www.mycocktailsrecipes.be, Tel:0476389045")
    lb1.pack()


def ask_questions():
    ask_questions = tkinter.Toplevel(win)
    ask_questions.title("Posez-nous vos questions")
    ask_questions.geometry("350x600")
    ask_questions.iconbitmap("logo1.ico")
    lb2 = tkinter.Label(ask_questions)
    lb2.pack()


def show_help():
    about_window = tkinter.Toplevel(win)
    about_window.title(" Aide ")
    about_window.geometry("350x600")
    about_window.iconbitmap("logo1.ico")
    lb = tkinter.Label(about_window, text="|||| !!!! PAGE EN CONSTRUCTION!!!! |||||")
    lb.pack()

# 1) - Création de la barre des menus
menuBar = Menu(win)

# 2) - Création des menus principaux
menuFichier = Menu(menuBar)
menuEdition = Menu(menuBar)
menuOutil = Menu(menuBar)
menuAide = Menu(menuBar)
menuQuestion = Menu(menuBar)

# 3) - Création des menus principaux à la barre des menus
menuBar.add_cascade(label="Fichier", menu=menuFichier)
menuBar.add_cascade(label="Edition", menu=menuEdition)
menuBar.add_cascade(label="Outils", menu=menuOutil)
menuBar.add_cascade(label="Aide", menu=menuAide)
menuBar.add_cascade(label="?", menu=menuQuestion)

# 4) - Ajout de commandes au menu principal
# commande Fichier
menuFichier.add_command(label="Nouveau")
menuFichier.add_command(label="Ouvrir", command=open_file)
menuFichier.add_command(label="Ajouter à mon carnet")
menuFichier.add_command(label="Enregistrer sous", command=save_as)
menuFichier.add_command(label="Imprimer")
menuFichier.add_command(label="Quitter", command=quit)

# commande Edition
menuEdition.add_command(label="Copier")
menuEdition.add_command(label="Coller")
menuEdition.add_command(label="Couper")
menuEdition.add_command(label="Ajouter un cocktail")
menuEdition.add_command(label="Modifier un cocktail")
menuEdition.add_command(label="Supprimer un cocktail")

# commande Outils
menuOutil.add_command(label="Outils de Cocktails")
menuOutil.add_separator()
menuOutil.add_command(label="Ustensils de Cocktails")

# commande Aide
menuAide.add_command(label="Afficher Aide", command=show_help)
menuAide.add_command(label="Ajouter un commentaire")
menuAide.add_command(label="Magasins partenaire ")
menuAide.add_command(label="A propos", command=show_about)

# commande Question
menuQuestion.add_command(label="Posez-nous vos questions", command=ask_questions)
menuQuestion.add_separator()
menuQuestion.add_command(label="Contactez l'Administrateur", command=show_admin)
###
win.config(menu=menuBar)
#
# Variable nécessaire
photoAcceuil = PhotoImage(file='accueil.png')
#photoLogo = PhotoImage(file='logo1.png') !!! problem to add logo
labelstatus = StringVar()
labelstatus.set("  << L'abus d'alcool est dangereux pour la santé, consommez avec modération! >>")
mail = StringVar()
pwd = StringVar()
nom = StringVar()
description = StringVar()
ingredients = StringVar()
# Mise en page du menu
frameWinMenu = Frame(win,bg="gray25")
frameWinMenu2 = Frame(win, bg="gray25")
frameWinMenu3 = LabelFrame(win)


# Première frame
labelTitleMenu = Label(frameWinMenu, text="My Cocktail Recipe", font=("Constantia", 21, "bold"), fg="red",bg="gray25")
labelstatusMenu = Entry(frameWinMenu, textvariable=labelstatus, width=70, state="disabled", font=("Constantia", 12, "bold"), fg="white")

frameWinMenu.pack(pady=10)
frameWinMenu2.pack(padx=((300,0)),side="left")
frameWinMenu3.pack(side="right", padx=((0,50)),pady=((50,0)))

labelTitleMenu.grid(pady=20)
labelstatusMenu.grid(row=1)

# Deuxième Frame
# consultCocktail = Button(frameWinMenu2, text="Consulter les Cocktails",font=("Constantia", 12, "bold"), fg="red", bg="gray25")
addCocktail = Button(frameWinMenu2, text="Ajouter un Cocktail",font=("Constantia", 12, "bold"), fg="red", bg="gray25",  command=addCocktails, state='disabled')
deleteCocktail = Button(frameWinMenu2, text="Supprimer un Cocktail",font=("Constantia", 12, "bold"), fg="red", bg="gray25",command=deletecocktail, state='disabled')
updateCocktail = Button(frameWinMenu2, text="Modifier un Cocktail",font=("Constantia", 12, "bold"), fg="red", bg="gray25", command=updateCocktails, state='disabled')
adminCocktail = Button(frameWinMenu2,text="Admin", font=("Constantia", 12, "bold"), fg="red", bg="gray25", command=admin)
quitCocktail = Button(frameWinMenu2, text="Quitter", font=("Constantia", 12, "bold"), fg="red", bg="gray25", command=quit)
lbCocktail = Listbox(frameWinMenu2,height=15,width=50)


# consultCocktail.grid(pady=15)
addCocktail.grid(row=1, pady=15)
deleteCocktail.grid(row=2, pady=15)
updateCocktail.grid(row=3, pady=15)
adminCocktail.grid(row=4, pady=15)
quitCocktail.grid(row=5, pady=15)
lbCocktail.grid(row=0, rowspan=5, column=1,padx=((150,0)))
lbCocktail.bind("<<ListboxSelect>>", lbClick)

# Troisième frame
labelNom = Label(frameWinMenu3, text="Nom:")
entrynom = Text(frameWinMenu3,height=0,width=20)
labelDescription = Label(frameWinMenu3, text="Description:")
entryDescription = Text(frameWinMenu3, height=10, width=50)
labelIngredient = Label(frameWinMenu3, text="Ingrédients:")
entryIngredient = Text(frameWinMenu3, height=10, width=50)

labelNom.grid(pady=20)
entrynom.grid(row=0, column=1, columnspan=2)
labelDescription.grid(row=1, column=0, pady=20)
entryDescription.grid(row=1, column=1,pady=15)
labelIngredient.grid(row=2,column=0,pady=15)
entryIngredient.grid(row=2, column=1,pady=15)


# Configuration et mise en page de l'accueil
winAcceuil = Toplevel()
xLeft = int(win.winfo_screenwidth()//1 - 1400)
yTop = int(win.winfo_screenheight()//1 - 800)
winAcceuil.geometry(f"1400x700+{xLeft}+{yTop}")
winAcceuil.resizable(False, False)
winAcceuil.title("My Cocktail Recipes")
winAcceuil.iconbitmap("logo1.ico")

framewin = Frame(winAcceuil)
framewin2 = Frame(winAcceuil)
framewin3 = LabelFrame(winAcceuil, text="Connectez-vous")
framewin4 = Frame(winAcceuil)

labelMail = Label(framewin3, text="Mail: ")
entryMail = Entry(framewin3, width=30, textvariable=mail)
labelPwd = Label(framewin3, text="Mot de passe: ")
entryPwd = Entry(framewin3, width=30, textvariable=pwd)
labelStatusPwd = Label(framewin3, text="", fg="red")

labelTitle = Label(framewin, text="  Bienvenue sur MyCocktailRecipes", font=("Constantia", 21, "bold"),fg="Navy blue")
lableLowTitle = Label(framewin, text="LE COCKTAIL A LA PORTEE DE TOUS LES AMATEURS", font=("Constantia", 15, "bold"),fg="red")
labelstatus = Entry(framewin, textvariable=labelstatus, width=70, state= "disabled", font=("Constantia", 12, "bold"), fg="Black")

labelImages = Label(framewin2, image=photoAcceuil)

buttonEnter = Button(framewin4, text="Connexion", font="Constantia",bd=2, fg="red",relief="groove", command=validConnect)
buttonAdd = Button(framewin4,text="Nouveau utilisateur",font="Constantia",bd=2, fg="red",relief="groove", command=newuser)
buttonQuitter = Button(framewin4, text="Quitter",font="Constantia",bd=2,fg="red",relief="groove", command= quit)

framewin.pack(pady=10)
framewin2.pack()
framewin3.pack(pady=50)
framewin4.pack()

labelTitle.grid(pady=10)
lableLowTitle.grid(row=1)
labelstatus.grid(row=3)

labelImages.pack()

buttonEnter.grid(padx=(0,200))
buttonAdd.grid(row=0, column=1, padx=((0,200)), pady=10)
buttonQuitter.grid(row=0, column=2)

labelMail.grid(pady=15)
entryMail.grid(row=0, column=1)
labelPwd.grid(row=1, column=0)
entryPwd.grid(row=1, column=1)
labelStatusPwd.grid(row=2, column=0, columnspan=2)

if __name__ == '__main__':
    c = db.charger(db_path)
    remplir()
    winAcceuil.attributes("-topmost", True)
    win.mainloop()
