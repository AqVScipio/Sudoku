# classe Sudoku
from Entities.Node import *

class Sudoku:

    #constructeur
    def __init__(self, grid):
        self.__grid = self.initialize(grid)
        print("Grille sudoku de taille", self.getSize(), "créée.")    

    # Initialisateur
    def initialize(self, grid):
        matrice = []

        for y in range(0, len(grid)):
            matrice.append([])
            for x in range(0, len(grid[y])):
                node = Node(grid[y][x]["valeur"])
                matrice[y].append(node)

        return matrice

    # Debug
    '''
    def displayGrid(self):
        for y in range(0, len(self.getGrid())):
            for x in range(0, len(self.getGrid()[y])):
                self.getGrid()[y][x].displayNode()
    '''
    
    #accesseur get/set sur une valeur de la matrice
    def getSize(self):
        return len(self.getGrid())

    def getGrid(self):
        return self.__grid
    
    def getValeur(self, iLig, iCol):
        return self.getGrid()[iLig][iCol]
    
    def setValeur(self, valeur, iLig, iCol):
        self.getGrid()[iLig][iCol] = valeur
        
        


    
