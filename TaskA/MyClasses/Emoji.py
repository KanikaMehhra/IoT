from sense_hat import SenseHat
sense=SenseHat()

class Emoji:
    def __init__(self,shapeArray, backGroundColor, outlineColor, fillInColor):
        super().__init__()
        self.__shapeArray=shapeArray
        self.__backGroundColor=backGroundColor
        self.__outlineColor=outlineColor
        self.__fillInColor=fillInColor

    def drawEmoji(self):
        color=""
        for row in range(len(self.__shapeArray)):
            for col in range(len(self.__shapeArray[row])):
                if self.__shapeArray[row][col]=='b':
                    color=self.__backGroundColor
                elif self.__shapeArray[row][col]=='o':
                    color=self.__outlineColor
                elif self.__shapeArray[row][col]=='f':
                    color=self.__fillInColor

                sense.set_pixel(row,col,color)


