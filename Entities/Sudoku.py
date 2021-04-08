# classe Sudoku
from Entities.Node import *

class Sudoku:
    def __init__(self, grid):
        self.__grid = self.initialize(grid)
        print("Grille sudoku de taille", self.getSize(), "créée.")    

    def initialize(self, grid):
        matrice = []

        for y in range(0, len(grid)):
            matrice.append([])
            for x in range(0, len(grid[y])):
                node = Node(grid[y][x]["valeur"])
                matrice[y].append(node)

        return matrice
    
    def getSize(self):
        return len(self.getGrid())

    def getGrid(self):
        return self.__grid
    
    def getValeur(self, iLig, iCol):
        return self.getGrid()[iLig][iCol]
    
    def setValeur(self, valeur, iLig, iCol):
        self.getGrid()[iLig][iCol] = valeur
        
        


    
