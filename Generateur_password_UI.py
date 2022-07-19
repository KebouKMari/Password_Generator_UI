
"""Generateur de mot de passe"""

from tkinter import *
import hashlib
import pyperclip

def generate_password():
    mot=champEnter.get()
    mot=str(mot)
    mots=mot.encode()
    passw=hashlib.sha1(mots).hexdigest()
    champfin.insert(0,passw)
    
    
    
def effacer():
    champEnter.delete(0,END)
    champfin.delete(0,END)

def copie():
    motpasse=champfin.get()
    pyperclip.copy(motpasse)


fenetre=Tk()
fenetre.geometry("930x500")
fenetre.title("Blema Password Generator")
fenetre.config(bg="purple")

#Cadre principal
cadre_pincipal=Frame(fenetre,bg="purple")

#le premier cadre image
cadre_img=Frame(cadre_pincipal,bg="purple")
width=300
height=300
image=PhotoImage(file="MonLogo.png").zoom(10).subsample(20)
canvas=Canvas(cadre_img,width=width,height=height,bg="purple",bd=0,highlightthickness=0)
canvas.create_image(width/2,height/2,image=image)
canvas.pack(pady=10)
cadre_img.grid(row=0,column=0,sticky=W)

#le deuxieme cadre texte
cadre_text=Frame(cadre_pincipal,bg="purple")
bienvenue=Label(cadre_text,text="Generateur de mot de passe Blema", font=("Courrier",25),fg="orange",bg="purple")
bienvenue.pack(pady=35,padx=15)

cadreS1=Frame(cadre_text,bg="purple")
motEnter=Label(cadreS1,text="Entrez le mot de passe: ",font=("Courrier",15),bd=4,bg="purple",fg="white",height=3)
motEnter.pack(side=LEFT,padx=10,pady=5)
champ=StringVar()
champEnter=Entry(cadreS1,textvariable=champ,width=40,bg="purple",fg="white",selectbackground="green")
champEnter.pack(side=RIGHT,padx=10,pady=5)
cadreS1.pack()

champfin=Entry()
cadreS2=Frame(cadre_text,bg="purple")
suppr=Button(cadreS2,text="Supprimer",bg="red",fg="black",font=("courrier",13),height=1,width=17,command=effacer)
suppr.pack(side=LEFT,pady=10,padx=20)
valid=Button(cadreS2,text="Valider",bg="#bde0ff",fg="black",font=("courrier",13),height=1,width=17,command=generate_password)
valid.pack(side=RIGHT)
cadreS2.pack()

cadreS3=Frame(cadre_text,bg="purple")
motfin=Label(cadreS3,text="Mot de passe genere est: ",bg="purple",fg="white",font=("courrier",12))
motfin.pack(side=LEFT,pady=75)
champfin=Entry(cadreS3,fg="white",width=40,bg="purple",bd=2,selectbackground="green")
champfin.pack(side=RIGHT,padx=20)
copier=Button(cadreS3,text="Copier",bg="black",fg="white",command=copie)
copier.pack(side=RIGHT)
cadreS3.pack(expand=YES)

sortir=Button(cadre_text,text="Quitter",bg="red",fg="white",font=("courrier",11),command=fenetre.quit)
sortir.pack(side=RIGHT,padx=10,pady=5)


cadre_text.grid(row=0,column=1,sticky=W)
cadre_pincipal.pack()
fenetre.mainloop()

