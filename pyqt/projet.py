from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys
from datetime import datetime   #import de la bibliothèque datetime

prenom=["Pierre", "Téo", "Tom", "Zaho"]
date_de_naissance=["08/06","07/02","25/08","15/12"]
evenements=[]


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('accueil.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable


        #lance la vérification du mot de passe lorsqu'on clique sur Entrer
        self.entrer.clicked.connect(self.verifier_pw)
        #ajoute les prénoms
        self.user.addItems(prenom)
        self.user.currentIndexChanged.connect(self.open_pw)
        self.evenement.hide()
        self.show()             #affiche la fenêtre MainWindows

    def verifier_pw(self):

        choix=self.user.currentText()
        print(choix)
        date=self.pw.text() # récupère la date entrée

        id=prenom.index(choix)
        print(id)
        print('texte saisi:',date,type(date)) #affiche le texte et le type
        if date==date_de_naissance[id]:
            print("Entrée acceptée")
            self.acceder_espace()
        else:
            print("refus")

    def open_pw(self): #donne accès au mdp

        self.pw.setEnabled(True)

    def acceder_espace(self):
        print("ok")
        self.pw.setHidden(True)
        self.user.setHidden(True)
        self.entrer.setHidden(True)
        self.date.setHidden(True)
        self.enfant.setHidden(True)
        self.evenement.setHidden(False)



app = QApplication(sys.argv)
window = MainWindows()
app.exec_()
