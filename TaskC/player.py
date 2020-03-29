class Player:
    def __init__(self):
        self.__points = 0
        self.__active = False
        self.__win = False

    def addPoints(self, points):
        self.__points += points

    def getPoints(self):
        return self.__points

    def setActive(self, active):
        self.__active = active
    
    def getActive(self):
        return self.__active

    def setWin(self):
        self.__win = True

    def getWin(self):
        return self.__win