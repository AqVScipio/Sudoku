import 

class GUIGrid:
 
    def __init__(self, grid, width, height):
        self.__grid = grid
        self.__cubes = [[Cube(self.board[i][j], i, j, width, height, size) for j in range(cols)] for i in range(rows)]
        self.__width = width
        self.__height = height
        self.__model = None
        self.__selected = None

    # Getters
    def getGrid(self):
        return self.__grid;
    def getCubes(self):
        return self.__cubes;
    def getModel(self):
        return self.__model;
    def getSelected(self):
        return self.__selected;

    def getWidth(self):
        return self.__width;
    def getHeight(self):
        return self.__height;

    # def __init__(self, rows, cols, width, height):
    #     self.rows = rows
    #     self.cols = cols
    #     self.cubes = [[Cube(self.board9[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
    #     self.width = width
    #     self.height = height
    #     self.model = None
    #     self.selected = None

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def place(self, val):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()

    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    def draw(self, win):
        # Draw Grid Lines
        gap = self.width / self.size
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

    def select(self, row, col):
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    def click(self, pos):
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

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True

