class Node:
    #constructeur
    def __init__(self, valeur = 0):
        self.__valeur = valeur
        self.__possibilites = []
        self.__attribue = -1

    # Debug
    '''
    def displayNode(self):
        print("---------------------")
        print("Valeur :", self.getValue())
        print("---------------------")
    '''
    
    def getValue(self):
        return self.__valeur
