class Color:
    def __init__(self):
        super().__init__()
        self.__red=(255,0,0)
        self.__green=(0,255,0)
        self.__blue=(0,0,255)
        self.__noColor=(0,0,0)

    def getRedColor(self):
        return self.__red

    def getGreenColor(self):
            return self.__green
            
    def getBlueColor(self):
            return self.__blue

    def getNoColorColor(self):
        return self.__noColor
