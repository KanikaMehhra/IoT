from random import randint
from sense_hat import SenseHat
from time import sleep
import constants

sense=SenseHat()

class ElectronicDie:    
    def __init__(self):
        super().__init__()
        self.__faceValue=0

    def getFaceValue(self):
        return self.__faceValue

    def setFaceValue(self,faceValue):
        self.__faceValue=faceValue

    def listenForShake(self):
        while True:
            acceleration = sense.get_accelerometer_raw()
            x = acceleration['x']
            y = acceleration['y']
            z = acceleration['z']

            x = abs(x)
            y = abs(y)
            z = abs(z)

            if x > 1 or y > 1 or z > 1:
                #sense.clear(255,255,0)
                self.performAnimation()
                sleep(1)
                self.setFaceValue(randint(1,6))
                sense.show_letter("{}".format(self.__faceValue),constants.T_COLOUR)
                sleep(2)
                break
        
        #shows short animation to get the feeling of rolling a die 
    def performAnimation(self):
        interval=0.0
        while (interval < constants.MAX_INTERVAL):
            num = randint(constants.MIN_DIE, constants.MAX_DIE)
            interval += constants.SMALL_INTERVAL
            sense.show_letter("{}".format(num))
            sleep(interval)
