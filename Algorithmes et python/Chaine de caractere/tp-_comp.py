# Créé par PIERRE.PELLEROT, le 01/12/2022 en Python 3.7

def insertionTexte(texte): #retourne une chaine de caractères
    nouv_texte=""
    for i in range(len(texte)-1):
        nouv_texte+=texte[i]+'*'

    nouv_texte+=texte[-1]
    return nouv_texte

def inversionmot(texte):
    nouv_texte=""
    mot=texte

    for j in range(len(mot)-1,-1,-1):
        nouv_texte+=mot[j]


    return nouv_texte
def palindrome(texte):
    nouv_texte=""


    for j in range(len(texte)-1,-1,-1):
        nouv_texte+=texte[j]


    return texte==nouv_texte





chaine=input('chaine de caractere')
print(palindrome(chaine))
