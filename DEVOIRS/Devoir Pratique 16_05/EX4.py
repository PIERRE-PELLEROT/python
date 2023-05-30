# Créé par PIERRE.PELLEROT, le 16/05/2023 en Python 3.7

def correspond(mot,mot_a_trous):

    if len(mot)!=len(mot_a_trous):
        return False

    for i in range(len(mot)):

        if not(mot[i]==mot_a_trous[i] or mot_a_trous[i]=='*'):


            return False

    return True


print(correspond('INFORMATIQUE', 'INFO*MA*IQUE')) #True
print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE')) #False
print(correspond('STOP', 'S*')) #False
print(correspond('AUTA', '*UTA')) #True

