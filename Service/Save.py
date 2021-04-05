'''
Utilisée pour sauver une grille dans le fichier /Data/save.txt
Ecrase la précedente partie. Il ne peut y avoir qu'une sauvegarde
(Possible d'en faire plusieurs, mais nous avons opté pour 1 sauvegarde)
'''
import json

def saveGrid(data):
    with open('./Data/save.txt', 'w') as outfile:
        json.dump(data, outfile)