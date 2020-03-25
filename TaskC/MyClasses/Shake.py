from sense_hat import SenseHat

sense=SenseHat()

class Shake:
    def __init__(self):
        super().__init__()
        __orientation=sense.get_orientation()
        self.__roll=abs(round(__orientation["roll"]))
        self.__pitch=abs(round(__orientation["pitch"]))
        self.__yaw=abs(round(__orientation["yaw"]))
        
    def getCurrentOrientationTuple(self):
        return (self.__roll, self.__pitch, self.__yaw)