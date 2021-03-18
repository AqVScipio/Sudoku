'''
Utilisée pour charger une grille depuis un fichier json
ou la dernière sauvegarde du Joueur
'''

import json

def getSudokuFromJSON(index = 0):
    return_value = []

    with open('./Data/grids.txt') as json_file:
        data = json.load(json_file)
        return_value = data[index]["grid"]
        
    return return_value


# def loadLastSave():
#     with open('./Data/save.txt') as json_file:
#         data = json.load(json_file)
#         print('id:', data['id'])

#     for p in data:
#         print('id:', p['id'])