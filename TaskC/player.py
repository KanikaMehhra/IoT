from sense_hat import SenseHat
sense=SenseHat()

class player:
    def __init__(self,name):
        self.__name=name
        self.__currPoints = 0

    def getPlayerInfo(self):
        return {
            "name":self.__name,
            "points":self.__currPoints            
        }
    
    def addPoints(self, points):
        self.__currPoints += points

    def getCurrPoints(self):
        return self.__currPoints