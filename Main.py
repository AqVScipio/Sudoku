from Entities.Sudoku import *
from Service.Load import *
from Entities.Window import *
from Components.Grid import *
from Components.Menu import *
from Service.Save import *
from Service.Load import *
import pygame

# Selects difficulty level
def newGame(size = 9):
    start(size)

# Saves the current game
def saveGame(grid):
    saveGrid(grid)

# Loads the player's last save
def loadGame():
    start(0, True)

# Checks if grid is complete
def checkBoard(board):
    board.check()
    #board.displaySuccessMessage()

# Start the new Sudoku
def start(size = 9, load = False):
    width = 800
    height = width
    window = Window(width + 300, height)

    sudoku,answerSheet = None, None

    if load: sudoku,answerSheet = loadFromJSON()
    else: sudoku = getNewGrid(size)

    win = pygame.display.set_mode((window.getWidth(), window.getHeight()))
    gridSurface = width

    board = Grid(sudoku, win, gridSurface, answerSheet)
    nav = Menu(win, gridSurface, newGame, loadGame, saveGame, checkBoard, board, board.getDataToSave())
    update(board, nav)

def update(board, nav):
        run = True

        while run:
            run = board.update(pygame.event.get())
            nav.update()
            pygame.display.update()

newGame(9)
pygame.quit()
    
