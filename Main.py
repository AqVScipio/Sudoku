from Entities.Sudoku import *
from Service.Load import *
from View.Window import *

def main():
    window = Window(540, 600)
    sudoku = getSudokuFromJSON()
    display = "test" #Display(sudoku, window)
    print(display)

main()
    
