class Color:

    def __init__(self, r, g, b):
        self.__r = r
        self.__g = g
        self.__b = b

    def values(self):
        return self.__r, self.__g, self.__b