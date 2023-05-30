# Créé par PIERRE.PELLEROT, le 16/05/2023 en Python 3.7

def reverse(texte):
    copy=""
    for i in range(len(texte)):
        copy+=texte[-(i+1)]

    return copy

print(reverse('informatique'))


