class DataToSave:

    def __init__(self, board, answerSheet):
        self.__board = board
        self.__answerSheet = answerSheet

    def getBoard(self):
        return self.__board
    
    def getAnswerSheet(self):
        return self.__answerSheet