from sense_hat import SenseHat
import os,sys,inspect
current = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent = os.path.dirname(current)
sys.path.insert(0, parent) 
import constants

class DieFaces:
    def __init__(self): 
        self.__sense = SenseHat()

    def setFace(self, number):
        if number == 1:
            self.__sense.set_pixels(constants.ONE)
        elif number == 2:
            self.__sense.set_pixels(constants.TWO)
        elif number == 3:
            self.__sense.set_pixels(constants.THREE)
        elif number == 4:
            self.__sense.set_pixels(constants.FOUR)
        elif number == 5:
            self.__sense.set_pixels(constants.FIVE)
        elif number == 6:
            self.__sense.set_pixels(constants.SIX)
        else: 
            print("There is a problem with a number that has been recieved")

