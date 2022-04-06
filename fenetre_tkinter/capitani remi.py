from tkinter import *
from random import randint
Fenetre=Tk()
#fonctions
def change_couleur(): #fonction du boutton
    liste_couleur=['green','blue','pink','yellow','purple','red','black','white','orange','grey','cyan',]
    Fenetre.config(bg=liste_couleur[randint(0,10)])

def Valider():
    a = Entree.get()
    if a=='' :
        phrase=("Veuillez entrer un pseudo et un mot de passe")
        MonMessage.config(text=phrase)
    else:
        phrase2 = "Bonjour "+a+", bienvenue sur le site certifié de la Poste :), vous pouvez le quitter maintenant!"
        MonMessage.config(text=phrase2)

def efface():
	Entree.delete(0,END)
	Entree2.delete(0,END)

#Paramètre de la fenêtre
Fenetre.attributes("-fullscreen", 1)

#bouton marrant
MonBouton=Button(Fenetre, text="Bouton marrant",activebackground="black",activeforeground="white",borderwidth="10px",background="white", command=change_couleur)
MonBouton.place(x=300,y=620)

#bouton effacer les zones de textes
BoutonEffacer=Button(text="Effacer",activebackground="black",activeforeground="white",borderwidth="10px",background="white",command=efface)
BoutonEffacer.place(x=820, y=500)

#bouton valider
bouton=Button(Fenetre, text='Valider',activebackground="black",activeforeground="white",borderwidth="10px",background="white",command=Valider)
bouton.place(x=940,y=500)

#icone de la page
Fenetre.iconbitmap("sapinstyle.ico")

#fenêtre
valeur=0
Fenetre.geometry("1366x768")
Fenetre.title("La Poste.fr")

#texte (titre)
MonMessage=Label(Fenetre, text="Le vrai site de la Poste certifié",bg="blue",font='Impact 24')
MonMessage.pack()

#image
photo=PhotoImage(file="Logo-laposte-removebg-preview.png")
lab1=Label(Fenetre,image=photo)
lab1.place(x=100,y=120)

#bouton pour fermer la fenêtre
MonBouton2=Button(Fenetre, text="X", activebackground="red",activeforeground="black",borderwidth="2px",height=1, width=1, background="red",font="Impact", command=Fenetre.destroy)
MonBouton2.place(x=1348,y=0)

#titre pour les zones de texte
titrezonedetexte1=Label(text="Entrez votre pseudo", bg="#33af25", font="Arial 20")
titrezonedetexte1.place(x=790 ,y=250)

#titre pour les zones de texte 2
titrezonedetexte2=Label(text="Entrez votre mot de passe", bg="#33af25", font="Arial 20")
titrezonedetexte2.place(x=750,y=400)

#zones de textes 1
Entree=Entry(Fenetre,width=50)
Entree.place(x=760,y=300)

#zone de texte 2
Entree2=Entry(Fenetre,width=50, show="*")
Entree2.place(x=760,y=450)

Fenetre.mainloop()
