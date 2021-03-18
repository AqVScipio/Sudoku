import pygame

class Window:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__window = pygame.display.set_mode((self.getWidth(), self.getHeight()))

    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height

    def getWindow(self):
        return self.__window

