from tkinter import*
def augmenter():
    global valeur
    valeur+=1
    MonMessage.config(text=valeur)

valeur=0
Fenetre=Tk()                                 #création de la fenetre principale
Fenetre.geometry("400x300")                 #précise la taille de la fenetre
Fenetre.title("ma premiere fenetre")
MonMessage=Label(Fenetre,text=valeur,fg='black')   #création de l'objet
MonMessage.pack()

MonBouton=Button(Fenetre, text="+", command = augmenter)
MonBouton.pack()
MonBouton2=Button(Fenetre, text="Quitter", command=Fenetre.destroy)
MonBouton2.pack()

Fenetre.mainloop()
