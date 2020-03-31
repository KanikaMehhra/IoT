from random import randint
from sense_hat import SenseHat
import modules

sense=SenseHat()

class ElectronicDie:    
    def __init__(self,faceValue,initOrienTuple):
        super().__init__()
        self.__faceValue=faceValue
        self.__initOrienTuple=initOrienTuple

    def listenForShake(self):
        newOrienTuple=modules.getCurrentAccelerationTuple()
        while self.__initOrienTuple!=newOrienTuple:
            sense.clear(255,255,0)
            self.__faceValue=randint(1,6)
            self.__initOrienTuple=newOrienTuple
            sense.show_letter("{}".format(self.__faceValue))

initOrientationTuple=modules.getCurrentAccelerationTuple()
die=ElectronicDie(randint(1,6), initOrientationTuple)

die.listenForShake()


