from tkinter import *
from random import randint


def change_couleur(): #fonction du boutton
    liste_couleur=['green','blue','pink','yellow','purple','red','black','white','orange','grey','cyan']
    #i=randint(0,10)
    #couleur=liste_couleur[i]
    MonMessage.config(bg='red', text='changement de couleur')
    Fenetre.config(bg=liste_couleur[randint(0,10)])

    
Fenetre=Tk()
Fenetre.geometry("1920x1080")
root = Tk()
root.attributes('-fullscreen', True)
MonMessage=Label(Fenetre, text="La Poste c'est cool",bg="yellow",font='Arial 18')
MonMessage.pack()
MonBouton=Button(Fenetre, text="Cliquez pour voir la Poste qui est cool",command=change_couleur)
MonBouton.pack()
photo=PhotoImage(file="Logo-laposte.png") #Le fichier doit être dans le même dossier
lab1=Label(Fenetre,image=photo)
lab1.pack()
Fenetre.mainloop()
