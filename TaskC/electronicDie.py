from random import randint
from sense_hat import SenseHat
import modules
from time import sleep

sense=SenseHat()
MAX_SHAKING_INTERVAL=3

class electronicDie:    
    def __init__(self):
        super().__init__()
        self.__faceValue=0
        self.__dt = 0.1


    def getFaceValue(self):
        return self.__faceValue

    def setFaceValue(self,faceValue):
        self.__faceValue=faceValue

    def listenForShake(self):
        temp=True
        while True:
            acceleration = sense.get_accelerometer_raw()
            x = acceleration['x']
            y = acceleration['y']
            z = acceleration['z']

            x = abs(x)
            y = abs(y)
            z = abs(z)

            if x > 1 or y > 1 or z > 1:
                sense.clear(255,255,0)
                sleep(1)
                self.setFaceValue(randint(1,6))
                sense.show_letter("{}".format(self.__faceValue))
                sleep(2)
                #temp=False
                break