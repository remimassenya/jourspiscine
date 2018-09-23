
jour = int(input("Entrer le numero du jour"))
mois = int(input("Entrer le numero du mois"))
annee = int(input("Entrer l'année"))
cormois=0
resannee=0

def correspondancejourdesemaine():
    if (reste == 0):
        print("Dimanche")
    elif (reste == 1):
        print("Lundi")
    elif (reste == 2):
        print("Mardi")
    elif (reste == 3):
        print("Mercredi")
    elif (reste == 4):
        print("Jeudi")
    elif (reste == 5):
        print("Vendredi")
    elif (reste == 6):
        print("Samedi")

def correspondancemois():
    if (mois == 1):
        return 0
    elif (mois == 2):
        return 3
    elif (mois == 3):
        return 3
    elif (mois == 4):
        return 6
    elif (mois == 5):
        return 1
    elif (mois == 6):
        return 4
    elif (mois == 7):
        return 6
    elif (mois == 8):
        return 2
    elif (mois == 9):
        return 5
    elif (mois == 10):
        return 0
    elif (mois == 11):
        return 3
    elif (mois == 12):
        return 5

def bissextile():
    if (((annee % 100 == 0 & annee % 4 == 0) | (annee % 400 == 0)) & (mois <= 2)):
        resannee = resannee - 1

def siecle():
    siecle = int(annee / 100)
    if (siecle == 16):
        return 6
    elif (siecle == 17):
        return 4
    elif (siecle == 18):
        return 2
    elif (siecle == 19):
        return 0
    elif (siecle == 20):
        return 6
    elif (siecle == 21):
        return 4


resannee=annee%100
resannee=int(resannee+(resannee/4))
resannee=resannee+jour

resannee=resannee+correspondancemois()
bissextile()
resannee = resannee + siecle()

reste=resannee%7
correspondancejourdesemaine()