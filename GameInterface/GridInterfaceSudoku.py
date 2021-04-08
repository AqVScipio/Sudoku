import pygame
import time
from math import sqrt
from Entities.Color import *
from Entities.DataToSave import *
from Entities.SuccessMessage import *
from Service.Save import *

pygame.font.init()

class Grid:
    #Paramètre le sudoku
    def __init__(self, sudoku, Window, widtheightBoard, answerSheet=None, scale = 1):
        self.__board = sudoku
        self.__win = Window
        self.__width = widtheightBoard #width
        self.__height = widtheightBoard #.height
        self.__size = len(sudoku)
        self.__cols = self.__size
        self.__rows = self.__size
        self.__selected = {
            "row": None,
            "col": None,
        }
        
        self.__answerSheet = self.__setAnswerSheet(answerSheet)
        self.setDataToSave()
        self.setSuccessMessage('', Color(0,0,0))

    def __setAnswerSheet(self, answerSheet):
        if answerSheet != None:
            return answerSheet
        else:
            return [[[] for i in range(self.__size)] for j in range(self.__size)]

    def __setAnswer(self, value):
        if value in self.__answerSheet[self.__selected["row"]][self.__selected["col"]]:
            self.__answerSheet[self.__selected["row"]][self.__selected["col"]].remove(value)
        else:
            self.__answerSheet[self.__selected["row"]][self.__selected["col"]].append(value)

    def getDataToSave(self):
        return self.__save
    
    def setDataToSave(self):
        self.__save = DataToSave(self.__board, self.__answerSheet)

    def setSuccessMessage(self, msg, color):
        self.__successMessage = SuccessMessage(msg, color)

    def __setSelectedNode(self, row, col):
        # Reset all other
        self.__selected["row"] = 0
        self.__selected["col"] = 0
       
        self.__selected["row"] = row
        self.__selected["col"] = col

        return self.__selected

    def update(self, events, run=True):
        key = None

        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and self.__emptyNodeSelected():
                if event.key == pygame.K_1 or event.key == pygame.K_KP1 :
                    key = "1"
                if event.key == pygame.K_2 or event.key == pygame.K_KP2 :
                    key = "2"
                if event.key == pygame.K_3 or event.key == pygame.K_KP3 :
                    key = "3"
                if event.key == pygame.K_4 or event.key == pygame.K_KP4 :
                    key = "4"
                if event.key == pygame.K_5 or event.key == pygame.K_KP5 :
                    key = "5"
                if event.key == pygame.K_6 or event.key == pygame.K_KP6 :
                    key = "6"
                if event.key == pygame.K_7 or event.key == pygame.K_KP7 :
                    key = "7"
                if event.key == pygame.K_8 or event.key == pygame.K_KP8 :
                    key = "8"
                if event.key == pygame.K_9 or event.key == pygame.K_KP9 :
                    key = "9"
                if event.key == pygame.K_a :
                    key = "A"
                if event.key == pygame.K_b :
                    key = "B"
                if event.key == pygame.K_c :
                    key = "C"
                if event.key == pygame.K_d :
                    key = "D"
                if event.key == pygame.K_e :
                    key = "E"
                if event.key == pygame.K_f :
                    key = "F"
                if event.key == pygame.K_g :
                    key = "G"


            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = self.__clickNode(pos)
                if clicked:
                    self.__setSelectedNode(clicked[0], clicked[1])
                    key = None
        
        self.__assessInput(key)
        self.__drawGrid()
        return run

    '''
    Checks if input okay
    '''
    def __assessInput(self, key):
        if self.__selected["row"] != None and self.__selected["col"] != None and key != None:
            self.__setAnswer(key)

    '''
    Draws the entire grid based on the player's choice
    '''
    def __drawGrid(self):
        self.__win.fill((255,255,255))
        # Draw Grid Lines
        gap = self.__width / self.__size

        for i in range(self.__rows+1):
            if i % sqrt(self.__size) == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.__win, (0,0,0), (0, i*gap), (self.__width, i*gap), thick)
            pygame.draw.line(self.__win, (0, 0, 0), (i * gap, 0), (i * gap, self.__height), thick)

        # Draw Node
        for i in range(self.__rows):
            for j in range(self.__cols):
                value = self.__board[i][j]['valeur']
                self.__drawNode(value, j, i)

        if len(self.__successMessage.getMsg()) > 0:
            self.displaySuccessMessage(False)

    '''
    Takes care of the text in each Node
    '''
    def __drawNode(self, value, col, row):
        fnt_size = self.__width / self.__size / sqrt(self.__size) * 3
        fnt = pygame.font.SysFont("comicsans", int(fnt_size))
        fnt_small = pygame.font.SysFont("comicsans", int(fnt_size / 2))

        gap = self.__width / self.__size
        x = col * gap
        y = row * gap

        # Draw answer(s) in a Node
        node = self.__answerSheet[row][col]
        if len(node) > 0:
            # If only one anwser, draw it in the center of the Node
            if len(node) == 1:
                text = fnt.render(node[0], 1, (0,191,255))
                self.__win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

            # If multiple answers, draw them in a grid format
            elif len(node) > 1:
                baseOffset = 5
                incrementalOffset = self.__width / self.__size / sqrt(self.__size)
                if self.__size == 16: baseOffset = 2
                xOffset, yOffset = baseOffset, baseOffset

                for i in range(len(node)):
                    text = fnt_small.render(node[i], 1, (128,128,128))
                    self.__win.blit(text, (x+xOffset, y+yOffset))

                    if (i+1) % sqrt(self.__size) == 0:
                        xOffset = baseOffset
                        yOffset += incrementalOffset
                    else:
                        xOffset += incrementalOffset
            
        # Draw default visible values
        if "-" not in self.__board[row][col]['valeur']:
            text = fnt.render(str(value), 1, (0, 0, 0))
            self.__win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

        # Focus on selected Node
        if row == self.__selected["row"] and col == self.__selected["col"]:
            pygame.draw.rect(self.__win, (255,0,0), (x,y, gap ,gap), 3)

    '''
    Returns corresponding Node position when clicked
    '''
    def __clickNode(self, pos):
        if pos[0] < self.__width and pos[1] < self.__height:
            gap = self.__width / self.__size
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y),int(x))
        else:
            return None

    '''
    Checks if wheter or not an empty node is selected
    '''
    def __emptyNodeSelected(self):
        return "-" in self.__board[self.__selected["row"]][self.__selected["col"]]['valeur']

    '''
    Checks if the grid is filles and contains no error
    Used to set the corresponding message to display
    '''
    def __gridIsFilled(self):
        errorFound = False

        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                if "-" in self.__board[i][j]['valeur']: 
                    if len(self.__answerSheet[i][j]) == 1:
                        if str(self.__board[i][j]['valeur']).replace('-', '') != self.__answerSheet[i][j][0]:
                            errorFound = True
                    else:
                        return False
        
        if errorFound:
            self.setSuccessMessage('Mistakes were made !', Color(200,0,0))
        else:
            self.setSuccessMessage('Success !', Color(0,200,0))

        return True

    '''
    This function displays the corresponding message
    '''
    def displaySuccessMessage(self, checkIfGridFilled = True):
        if checkIfGridFilled:
            if not self.__gridIsFilled():
                self.setSuccessMessage('Grid not filled yet !', Color(200,0,0))
        
        fnt = pygame.font.SysFont("comicsans", 40)
        r = self.__successMessage['color'].r
        g = self.__successMessage['color'].g
        b = self.__successMessage['color'].b
        text = fnt.render(self.__successMessage['msg'], 1, (r,g,b))

        self.__win.blit(text, (self.__width / 2 - text.get_width() / 2, self.__height + 20))

        


