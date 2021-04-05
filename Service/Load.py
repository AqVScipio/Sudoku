'''
Utilisée pour charger une grille depuis un fichier json
ou la dernière sauvegarde du Joueur
'''

import json

def getSudokuFromJSON(size=9, index = 0):
    return_value = []

    with open('./Data/grids' + str(size) + '.txt') as json_file:
        data = json.load(json_file)
        return_value = data[index]["grid"]
        
    return return_value

def loadFromJSON():
    with open('./Data/save.txt') as json_file:
        data = json.load(json_file)
        return data["board"], data["answerSheet"]
        
    return None

# def loadLastSave():
#     with open('./Data/save.txt') as json_file:
#         data = json.load(json_file)
#         print('id:', data['id'])

#     for p in data:
#         print('id:', p['id'])