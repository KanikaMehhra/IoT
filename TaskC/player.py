from sense_hat import SenseHat
sense=SenseHat()

class player:
    def __init__(self,name):
        self.__name=name
        self.__currPoints = 0
        self.__activeStatus = False

    def addPoints(self, points):
        self.__currPoints += points

    def getPlayerInfo(self):
        return {
            "name":self.__name,
            "points":self.__currPoints            
        }

    def setActive(self, active):
        self.__active = active
    