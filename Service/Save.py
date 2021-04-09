'''
Used to save a grid in /Data/save.txt
Erases previous save, there can only be one save
'''
import json
from json import JSONEncoder
from io import StringIO

class DataToSaveEncoder(JSONEncoder):
    def default(self,o):
        return o.__dict__

def saveGrid(data):

    # with open('./Data/save.txt', 'w') as outfile:
    #     json.dump(data, outfile, cls=DataToSaveEncoder)

    io = StringIO()
    json.dump(data, io, cls=DataToSaveEncoder)
    dataToWrite = io.getvalue().replace('_DataToSave__','').replace('_Answer__','')

    with open('./Data/save.txt', 'w') as file:
        file.write(dataToWrite)

