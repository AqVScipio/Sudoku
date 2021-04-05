from Entities.Sudoku import *
from Service.Load import *
from View.Window import *
from GridInterfaceSudoku import *
import pygame

def main():
    window = Window(500, 600)
    #sudoku = getSudokuFromJSON()
    sudoku, answerSheet = loadFromJSON()

    win = pygame.display.set_mode((window.getWidth(), window.getHeight()))
    widtheight = 500

    board = Grid(sudoku, win, widtheight, answerSheet)
    board.runInterface()

main()
pygame.quit()
    
