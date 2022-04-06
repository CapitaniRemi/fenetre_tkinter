from tkinter import*

def bonjour():
    nom = Entree.get()
    Message=Label(Fenetre,text='bonjour '+nom)
    Message.pack()
    Entree.delete(0,END)

Fenetre=Tk()
Fenetre.geometry("1000x800")
Fenetre.title("C'est plus ma première fenêtre")
Entree=Entry(Fenetre,width=1000)
Entree.pack()
bouton=Button(Fenetre, text='recup',command=bonjour)
bouton.place(x=683,y=384)

Fenetre.mainloop()
