from random import randint
from sense_hat import SenseHat
from time import sleep

import os,sys,inspect
current = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent = os.path.dirname(current)
sys.path.insert(0, parent) 
import constants

class ElectronicDie:    
    def __init__(self):
        super().__init__()
        self.__faceValue=0
        self.__dt = 0.1
        self.__sense=SenseHat()

    def getFaceValue(self):
        return self.__faceValue

    def setFaceValue(self,faceValue):
        self.__faceValue=faceValue

    def listenForShake(self):
        acceleration = self.__sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x = round(x, 0)
        y = round(y, 0)
        z = round(z, 0)

        x = abs(x)
        y = abs(y)
        z = abs(z)
        
        num = 0
        if x > 1 or y > 1 or z > 1:
            #for purposes of fake animation
            t = 0.0
        
        #shows short animation to get the feeling of rolling a die 
            while (t < 1.0):
                num = randint(constants.MIN_DIE, constants.MAX_DIE)
                t += self.__dt
                if t > 1.0:
                    self.__sense.show_letter(str(num), constants.RED)
                else:
                    self.__sense.show_letter(str(num))
                sleep(t)
        
            self.setFaceValue(num)
            
        return num
            