'''
Us
'''

import json
from random import randrange

'''
Loads a new random grid from the selected difficulty
'''
def getNewGrid(size = 9):
    return_value = []
    maxRange = -1
    if size == 9 : index = maxRange = 4
    elif size == 16 : maxRange = 2

    index = randrange(maxRange)
    if index >= 0:
        with open('./Data/grids' + str(size) + '.txt') as json_file:
            data = json.load(json_file)
            return_value = data[index]["grid"]
        
    return return_value

'''
Loads the player's last save
'''
def loadFromJSON():
    with open('./Data/save.txt') as json_file:
        data = json.load(json_file)
        return data["board"], data["answerSheet"]
        
    return None