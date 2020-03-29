from sense_hat import SenseHat
from random import randint
from time import sleep
from dieFaces import DieFaces

import os,sys,inspect
current = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent = os.path.dirname(current)
sys.path.insert(0, parent) 
import constants

class ElectronicDie:
    def __init__(self):
        self.__sense = SenseHat()
        self.__faces = DieFaces()
        self.__dt = 0.1
    
    def checkDie(self):
        acc = self.__sense.get_accelerometer_raw()
        x = acc['x']
        y = acc['y']
        z = acc['z']

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
        
            while (t < 1.0):
                num = randint(constants.MIN_DIE, constants.MAX_DIE)
                t += self.__dt
                self.__faces.setFace(num)
                sleep(t)
                
        return num
