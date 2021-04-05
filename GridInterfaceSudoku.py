import pygame
import time
from math import sqrt
from Entities.Color import *
from Service.Save import *
pygame.font.init()


class Grid:
    #Paramètre le sudoku
    def __init__(self, sudoku, Window, widtheightBoard, answerSheet=None):
        self.board = sudoku
        
        self.win = Window
        self.width = widtheightBoard #.width
        self.height = widtheightBoard #.height
        self.size = len(sudoku)
        self.cols = self.size
        self.rows = self.size
        self.selected = {
            "row": None,
            "col": None,
        }
        
        self.__answerSheet = self.setAnswerSheet(answerSheet)
        self.__save = {"board": self.board, "answerSheet": self.__answerSheet}

        self.__successMessage = ''
        self.__successMessageColor = Color(0,0,0)

    def setAnswerSheet(self, answerSheet):
        if answerSheet != None:
            return answerSheet
        else:
            # return [[[]*self.size for i in range(self.size)]*self.size for j in range(self.size)]
            return [[[] for i in range(self.size)] for j in range(self.size)]


    def runInterface(self):
        run = True

        while run:
            key = None

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN and self.board[self.selected["row"]][self.selected["col"]]['valeur'] <= 0 :
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1 :
                        key = 1
                    if event.key == pygame.K_2 or event.key == pygame.K_KP2 :
                        key = 2
                    if event.key == pygame.K_3 or event.key == pygame.K_KP3 :
                        key = 3
                    if event.key == pygame.K_4 or event.key == pygame.K_KP4 :
                        key = 4
                    if event.key == pygame.K_5 or event.key == pygame.K_KP5 :
                        key = 5
                    if event.key == pygame.K_6 or event.key == pygame.K_KP6 :
                        key = 6
                    if event.key == pygame.K_7 or event.key == pygame.K_KP7 :
                        key = 7
                    if event.key == pygame.K_8 or event.key == pygame.K_KP8 :
                        key = 8
                    if event.key == pygame.K_9 or event.key == pygame.K_KP9 :
                        key = 9


                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    clicked = self.__click(pos)
                    if clicked:
                        self.__select(clicked[0], clicked[1])
                        key = None
            
            if self.selected["row"] != None and self.selected["col"] != None and key != None:
                self.__setAnswer(key)
                saveGrid(self.__save)
                # Update answerSheet

            self.__drawGrid()
            
            if self.gridIsFilled():
                self.displaySuccessMessage()

            pygame.display.update()



    def __drawGrid(self):
        self.win.fill((255,255,255))
        # Draw Grid Lines
        gap = self.width / self.size

        for i in range(self.rows+1):
            if i % sqrt(self.size) == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(self.win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Draw Node
        for i in range(self.rows):
            for j in range(self.cols):
                value = self.board[i][j]['valeur']
                self.__drawNode(value, j, i)

    def __drawNode(self, value, col, row):
        fnt = pygame.font.SysFont("comicsans", 40)
        fnt_small = pygame.font.SysFont("comicsans", 20)

        gap = self.width / self.size
        x = col * gap
        y = row * gap

        # Draw answer(s) in a Node
        node = self.__answerSheet[row][col]
        if len(node) > 0:
            # If only one anwser, draw it in the center of the Node
            if len(node) == 1:
                text = fnt.render(str(node[0]), 1, (0,191,255))
                self.win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

            # If multiple answers, draw them in a grid format
            elif len(node) > 1:
                

                xOffset, yOffset = 5,5
                for i in range(len(node)):
                    text = fnt_small.render(str(node[i]), 1, (128,128,128))
                    self.win.blit(text, (x+xOffset, y+yOffset))

                    if (i+1) % sqrt(self.size) == 0:
                        xOffset = 5
                        yOffset += self.size * 2
                    else:
                        xOffset += self.size * 2
            
        # Draw default visible values
        if self.board[row][col]['valeur'] > 0:
            text = fnt.render(str(value), 1, (0, 0, 0))
            self.win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

        # Focus on selected Node
        if row == self.selected["row"] and col == self.selected["col"]:
            pygame.draw.rect(self.win, (255,0,0), (x,y, gap ,gap), 3)
    
    def __setAnswer(self, value):
        if value in self.__answerSheet[self.selected["row"]][self.selected["col"]]:
            self.__answerSheet[self.selected["row"]][self.selected["col"]].remove(value)
        else:
            self.__answerSheet[self.selected["row"]][self.selected["col"]].append(value)


    def __select(self, row, col):
        # Reset all other
        self.selected["row"] = 0
        self.selected["col"] = 0
       
        self.selected["row"] = row
        self.selected["col"] = col

        return self.selected

    def __click(self, pos):
        """
        :param: pos
        :return: (row, col)
        """
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / self.size
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y),int(x))
        else:
            return None

    def gridIsFilled(self):
        errorFound = False

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j]['valeur'] < 0: 
                    if len(self.__answerSheet[i][j]) == 1:
                        if str(self.board[i][j]['valeur']).replace('-', '') != self.__answerSheet[i][j][0]:
                            errorFound = True
                    else:
                        return False
        
        if errorFound:
            self.__successMessage = 'Mistakes were made !'
            self.__successMessageColor = Color(200,0,0)
        else:
            self.__successMessage = 'Success !'
            self.__successMessageColor = Color(0,200,0)

        return True

    def displaySuccessMessage(self):
        fnt = pygame.font.SysFont("comicsans", 40)
        r = self.__successMessageColor.r
        g = self.__successMessageColor.g
        b = self.__successMessageColor.b
        text = fnt.render(self.__successMessage, 1, (r,g,b))

        self.win.blit(text, (self.width / 2 - text.get_width() / 2, self.height + 20))

        


