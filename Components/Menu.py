import pygame
from Entities.Timer import *

class Menu:
    def __init__(self, window, xOffset, funcNewGame, funcLoad, funcSave, funcCheck, board, dataToSave):
        self.__win = window
        self.__xOffset = xOffset + 50
        self.__funcNewGame = funcNewGame
        self.__funcLoad = funcLoad
        self.__funcSave = funcSave
        self.__funcCheck = funcCheck
        self.__dataToSave = dataToSave
        self.__board = board
        self.__timer = Timer()
    
    def update(self):

        white = (200,200,200)
        green = (0,200,0)
        margin = 40
        wdt = 125
        hgh = 30
            
        self.button("Nouveau 9x9", self.__xOffset, margin * 1,wdt,hgh, white, green, self.__funcNewGame, 9)
        
        self.button("Nouveau 16x16", self.__xOffset, margin * 2,wdt,hgh, white, green, self.__funcNewGame, 16)

        self.button("Charger partie", self.__xOffset, margin * 3,wdt,hgh, white, green, self.__funcLoad)

        self.button("Sauvegarder partie", self.__xOffset, margin * 4,wdt,hgh, white, green, self.__funcSave, self.__dataToSave)

        self.button("Vérifier", self.__xOffset, margin * 5,wdt,hgh, white, green, self.__funcCheck, self.__board)

        if self.__timer.isPaused(): 
            self.button("Reprendre", self.__xOffset, margin * 6,wdt,hgh, white, green, self.__timer.resume)
        else:
            self.button("Pause", self.__xOffset, margin * 6,wdt,hgh, white, green, self.__timer.pause)
        
        font = pygame.font.Font("freesansbold.ttf",20)
        text = font.render(self.__timer.getTimePassedSinceStart(), 1, (0,0,0))
        self.__win.blit(text, (self.__xOffset + 70, margin * 7))


    def button(self, msg,x,y,w,h,ic,ac, action=None, param = None):
        mouse = pygame.mouse.get_pos()
        #click = pygame.mouse.get_pressed()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.__win, ac,(x,y,w,h))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if param != None : action(param)
                    else: action()

        else:
            pygame.draw.rect(self.__win, ic,(x,y,w,h))

        smallText = pygame.font.Font("freesansbold.ttf",12)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        self.__win.blit(textSurf, textRect)

    def text_objects(self, text, font):
        textSurface = font.render (text, 1, (0,0,0))
        return textSurface, textSurface.get_rect()