
class SuccessMessage:

    def __init__(self, msg, color):
        self.__color = color
        self.__msg = msg

    def getColor(self):
        return self.__color

    def getMsg(self):
        return self.__msg