
"""
Importation des modules contenant une boîte de dialogue permettant
de sélectionner un fichier ou un répertoire,
ils utilisent l'interface Tkinter
"""
import tkinter
import sqlite3
from sqlite3 import Connection
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import database as db


def getID(email):
    tmp = db.getAllUsers(c)
    for user in tmp:
        if email == user["email"]:
            return user["rowid"]
    return -1


def connecter():
    winCon = Toplevel()
    winCon.geometry(f"720x360+{xLeft}+{yTop}")
    winCon.attributes("-topmost", True)
    winCon.iconbitmap("logo1.ico")
    winCon.title("IDENTIFICATION")

    mail = StringVar()
    pwd = StringVar()

    frameCon = LabelFrame(winCon, text="Connectez-vous")
    frameCon2 = Frame(winCon)

    labelMail = Label(frameCon, text="Mail: ")
    entryMail = Entry(frameCon, width=30, textvariable=mail)
    labelPwd = Label(frameCon, text="Mot de passe: ")
    entryPwd = Entry(frameCon, width=30, textvariable=pwd)
    buttonConnect = Button(frameCon2, text="Connexion", command=lambda: validConnect())
    buttonQuit = Button(frameCon2, text="Quitter", command=lambda: quitwin(winCon))
    labelStatusPwd = Label(frameCon, text="", fg="red")

    frameCon.pack()
    frameCon2.pack(pady=25)

    labelMail.grid()
    entryMail.grid(row=0, column=1)
    labelPwd.grid(row=1, column=0)
    entryPwd.grid(row=1, column=1)
    labelStatusPwd.grid(row=2, column=0, columnspan=2)
    buttonConnect.grid(padx=(0, 100))
    buttonQuit.grid(row=0, column=1)

    def validConnect():
        cocktailMail = mail.get()
        cocktailPwd = pwd.get()
        if cocktailMail != "" and cocktailPwd != "":
            id = getID(cocktailMail)
            if id >= 0:
                user = db.getUser(c, id)
                if cocktailPwd == user["mdp"]:
                    winCon.destroy
                    win.update()
                else:
                    labelStatusPwd.config(text="Mot de passe incorrect", fg='red')
                    winCon.update()
            else:
                labelStatusPwd.config(text="L'utilisateur n'existe pas", fg="red")
                winCon.update()


def quitwin(window):
    window.destroy()


db_path = "database.db"

win = Tk()
xLeft = int(win.winfo_screenwidth() // 1 - 1400)
yTop = int(win.winfo_screenheight() // 1 - 800)
win.geometry(f"700x200+{xLeft}+{yTop}")
win.iconbitmap("logo1.ico")

winAcceuil = Toplevel()

photoAcceuil = PhotoImage(file='accueil.png')

labelstatus = StringVar()
labelstatus.set("             L'abus d'alcool est dangereux pour la santé, consommez avec modération")

winAcceuil.geometry(f"1200x600+{xLeft}+{yTop}")
winAcceuil.resizable(False, False)
winAcceuil.title("My Cocktail Recipe")
winAcceuil.iconbitmap("logo1.ico")


################
#
#  Widgets ... et activation

def show_about():
    about_window = tkinter.Toplevel(winAcceuil)
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
    about_admin = tkinter.Toplevel(winAcceuil)
    about_admin.title("Contacter l'Administrateur")
    about_admin.geometry("250x150")
    about_admin.iconbitmap("logo1.ico")
    lb1 = tkinter.Label(about_admin, text="\nstephanelossou@gmail.com \n Stéphane Lossou")
    messagebox.showinfo("Ecrivez-nous!", "RDV sur https://www.lossou.be, Tel:0476389045")
    lb1.pack()


def ask_questions():
    ask_questions = tkinter.Toplevel(winAcceuil)
    ask_questions.title("Posez-nous vos questions")
    ask_questions.geometry("350x600")
    ask_questions.iconbitmap("logo1.ico")
    lb2 = tkinter.Label(ask_questions)
    lb2.pack()


def show_help():
    about_window = tkinter.Toplevel(winAcceuil)
    about_window.title(" Aide ")
    about_window.geometry("350x600")
    about_window.iconbitmap("logo1.ico")
    lb = tkinter.Label(about_window, text="|||| !!!! PAGE EN CONSTRUCTION!!!! |||||")
    lb.pack()

# 1) - Création de la barre des menus
menuBar = Menu(winAcceuil)

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
menuQuestion.add_command(label="Contacter l'Administrateur", command=show_admin)
###
winAcceuil.config(menu=menuBar)
#
#
framewin = Frame(winAcceuil)
framewin2 = Frame(winAcceuil)
framewin3 = Frame(winAcceuil)

labelTitle = Label(framewin, text=" Bienvenue sur My Cocktail Recipe", font=("Constantia", 21, "bold"), fg="Navy blue")
lableLowTitle = Label(framewin, text=" Bienvenue sur My Cocktail Recipe", font=("Constantia", 15, "bold"), fg="red")
labelstatus = Entry(framewin, textvariable=labelstatus, width=75, state="disabled", font=("Constantia", 12, "bold"),
                    fg="Black")

labelImages = Label(framewin2, image=photoAcceuil)

buttonEnter = Button(framewin3, text="Connexion", font="Constantia", bd=2, fg="red", relief="groove", command=connecter)
buttonQuitter = Button(framewin3, text="Quitter", font="Constantia", bd=2, fg="red", relief="groove", command=quit)

framewin.pack(pady=10)
framewin2.pack()
framewin3.pack(pady=50)

labelTitle.grid(pady=10)
lableLowTitle.grid(row=1)
labelstatus.grid(row=3)

labelImages.pack()

buttonEnter.grid(padx=(0, 200))
buttonQuitter.grid(row=0, column=1)

if __name__ == '__main__':
    c = db.charger(db_path)
    winAcceuil.attributes("-topmost", True)
    win.mainloop()
