'''
Used to save a grid in /Data/save.txt
Erases previous save, there can only be one save
'''
import json

def saveGrid(data):
    with open('./Data/save.txt', 'w') as outfile:
        json.dump(data, outfile)