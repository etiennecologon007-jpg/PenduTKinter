# Créé par Utilisateur, le 02/11/2024 en Python 3.7
from tkinter import*
from random import*
mode=[]
L=[]
A=[]
F=[]
def fichierpokemon():
    with open('quoicoubeh.txt','r')as fichier:
        lignes=fichier.readlines()
    indice=randint(0,len(lignes)-1)
    print(indice)
    return lignes[indice]
def fichiernormale():
    with open('Normale.txt','r')as fichier:
        lignes=fichier.readlines()
    indice=randint(0,len(lignes)-1)
    print(indice)
    return lignes[indice]
def Choix_Mot(indice):
    mots = {1: "ABANDONNER",2: "ABATTAGE",3: "ABONDANTE", 4: "ABRACADABRA", 5: "ACROBATE",6: "AFFECTIONNER",7: "AFFICHAGE",8: "AGRANDISSEMENT",9: "ALIMENTATION",10: "ANOMALIE",11: "APPRENTISSAGE",12: "ARABESQUE",13: "ARBITRAIRE",14: "ARTICHAUT",15: "ASTROLOGIE",16: "ATTACHEMENT",17: "AVANTAGEUX",18: "BOUSCULADE",19: "CALCULATEUR",20: "CHALEUREUX",21: "CHANGEMENT",22: "CHIFFONIER",23: "CHEVALERESQUE",24: "CITRONNIER",25: "CONFIANCE",26: "CONNAISSEUR",27: "CONSTELLATION",28: "NENUPHAR",29: "CONTAGIEUX",30: "CONTREDIRE",31: "CONVAINCRE",32: "COQUELICOT",33: "EXISTENCE",34: "FANTASTIQUE",35: "GLYCINE",36: "GRATITUDE",37: "HABITATION",38: "HIPPOCAMPE",39: "HIPPOPOTAME",40: "IMAGINATION",41: "IRRITATION",42: "JUSTIFIABLE",43: "MARGUERITE",44: "MOTIVATION",45: "MYSTERIEUSE",46: "ORGANISATION",47: "OSTENSIBLEMENT",48: "PISSENLIT",49: "RHODODENDRON",50: "SATSFACTION",51: "TRADITIONNEL",52: "TRANSFORMATION",53: "UTILISATION",54: "VAINQUEUR",55: "VARIATION",56: "VOLONTAIRE",57: "VOYAGEUR"}

    return mots.get(indice, None)
def Mot():
    motcherche=''
    #indice=randint(0,len())
    #print(indice)
    mot=fichierpokemon()
    for k in range(len(mot)-1):
        L.append(mot[k])
        A.append('_ ')
    for elem in A:
        motcherche+=elem
    return motcherche

def LettreTrouve():
    b=''
    Victory='GG'
    Lettre=entre.get()
    for k in range(len(L)): #si la lettre est bien dans la liste L à l'indice k, on ajoute la lettre dans la liste A à l'indice k
        if Lettre==L[k]:

            A[k]=L[k]

        print(A)
    if Lettre not in L:
        F.append(Lettre)
        #erreur+=1
        #print(erreur)
        if len(F)==7:
            BoutonOK.place(x='600',y='600')


        nomFichier = "pendu_"+str(len(F))+".png"
        photo=PhotoImage(file=nomFichier)
        labelpendu.config(image=photo)
        labelpendu.image=photo

        #labelpendu.place(x='80',y='10')
    for elem in A:
        b+=elem
    label0['text']=b
    if A==L:
        label['text']=Victory
        label.place(x='100',y='250')
        BoutonOK.place(x='600',y='600')
    print(F)
    print(L)
    print(A)
    print(mode)
def Motnormale():
    motcherche=''
    #indice=randint(0,57)
    #print(indice)
    mot=fichiernormale()
    for k in range(len(mot)-1):
        L.append(mot[k])
        A.append('_ ')
    for elem in A:
        motcherche+=elem
    return motcherche
def jeunormale():
    mode.append(' ')
    L.clear()
    A.clear()
    F.clear()
    #new_mot=Mot()
    label0['text']=Motnormale()
    label['text']='Choisis une lettre en maj'
    label.place(x='10',y='250')
    photo=PhotoImage(file="pendu_0.png")
    labelpendu.config(image=photo)
    labelpendu.image=photo
    BoutonOK.place(x='80',y='320')
    #=Button(fenetre, text="Valider", command=LettreTrouve)
    BoutonOK.place(x='80',y='320')
    BoutonPokemon.place(x='300',y='220')
    BoutonJeunormale.place(x='500',y='190')
    print(mode)
def jeupokemon():
    mode.clear()
    L.clear()
    A.clear()
    F.clear()
    #new_mot=Mot()
    label0['text']=Mot()
    label['text']='Choisis une lettre en maj'
    label.place(x='10',y='250')
    photo=PhotoImage(file="pendu_0.png")
    labelpendu.config(image=photo)
    labelpendu.image=photo
    BoutonOK.place(x='80',y='320')
    #=Button(fenetre, text="Valider", command=LettreTrouve)
    BoutonOK.place(x='80',y='320')
    BoutonJeunormale.place(x='300',y='190')
    BoutonPokemon.place(x='500',y='220')
    print(mode)



def rejouer():

    Victory='GG'
    Gneuh='Choisis une lettre en maj'
    L.clear()
    A.clear()
    F.clear()
    #new_mot=Mot()
    if mode==[]:
        label0['text']=Mot()
    else:
        label0['text']=Motnormale()

    label['text']='Choisis une lettre en maj'
    label.place(x='10',y='250')
    photo=PhotoImage(file="pendu_0.png")
    labelpendu.config(image=photo)
    labelpendu.image=photo
    BoutonOK.place(x='80',y='320')
    #=Button(fenetre, text="Valider", command=LettreTrouve)
    BoutonOK.place(x='80',y='320')
def AjouterMot():
    if mode==[]:

        NewMot=entre.get()+"\n"
        print(NewMot)
        with open('quoicoubeh.txt','a')as fichier:
            fichier.write(NewMot)
    else:
        NewMot=entre.get()+"\n"
        print(NewMot)
        with open('Normale.txt','a')as fichier:
            fichier.write(NewMot)



fenetre=Tk()
fenetre.geometry('400x400')
fenetre.title('Pendu')
fenetre['bg']='green'
fenetre.resizable(height=False,width=False)


photoSinge=PhotoImage(file="Wikipedia-sipi-image-db-mandrill-4.2.03-quantize-only-CCC.png")
labelimage=Label(fenetre,image=photoSinge)
labelimage.pack()


photo0=PhotoImage(file="pendu_0.png")
labelpendu=Label(fenetre,image=photo0)
labelpendu.place(x='80',y='10')


label0=Label(fenetre, text=Mot(), font=("Verdana"))
label0.place(x='80',y='200')

label=Label(fenetre, text="Choisis une lettre en maj", font=("Verdana",20,"italic bold"))
label.place(x='10',y='250')


BoutonFin=Button(fenetre, text="Quitter", command=fenetre.destroy)
BoutonFin.place(x='350',y='365')
ma_variable=StringVar
entre=Entry(fenetre,textvariable=ma_variable)
entre.place(x='80',y='300')

BoutonOK=Button(fenetre, text="Valider", command=LettreTrouve)
BoutonOK.place(x='80',y='320')

BoutonRejouer=Button(fenetre, text="Rejouer", command=rejouer )
BoutonRejouer.place(x='280',y='365')

BoutonAjouterMot=Button(fenetre, text="Ajouter un mot", command=AjouterMot)
BoutonAjouterMot.place(x='80',y='350')

BoutonJeunormale=Button(fenetre, text="Modenormale", command=jeunormale)
BoutonJeunormale.place(x='300',y='190')

BoutonPokemon=Button(fenetre, text="ModePokemon", command=jeupokemon)
BoutonPokemon.place(x='500',y='220')






fenetre.mainloop()