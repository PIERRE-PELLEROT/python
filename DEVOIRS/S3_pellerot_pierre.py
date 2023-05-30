# Créé par pierre.PELLEROT, le 17/01/2023

"""codeMorseLettres=['.-','-...','-.-.','-..','.','..-.','--.','....','..',
           '.---','-.-','.-..','--','-.','---','.--.','--.-','.-.',
           '...','-','..-','...-','.--','-..-','-.--','--..']
codeMorseChiffres =['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']

texte=str(input("votre texte ?"))

code=""
texte=texte.upper()

for i in range(len(texte)):
    if texte[i].isalpha():
        caractere=codeMorseLettres[ord(texte[i])-65]
        print(caractere)
    if texte[i].isdigit():
        caractere=codeMorseChiffres[int(texte[i])]
        print(caractere)"""


"""def double(mot):
    texte=""
    for i in range(len(mot)):
        texte+=mot[i]*2
    return texte

print(double("bon"))"""



