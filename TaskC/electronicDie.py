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
        while temp:
            acceleration = sense.get_accelerometer_raw()
            x = acceleration['x']
            y = acceleration['y']
            z = acceleration['z']

            x = abs(x)
            y = abs(y)
            z = abs(z)

            if x > 1 or y > 1 or z > 1:
                sense.clear(255,255,0)
                sense.low_light=True
                sleep(1)
                sense.low_light=False
                sleep(1)
                self.setFaceValue(randint(1,6))
                print(self.__faceValue)
                sense.show_letter("{}".format(self.__faceValue))
                sleep(2)
                temp=False



        """
        acc = sense.get_accelerometer_raw()
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
                num = randint(0, 6)
                t += self.__dt
                sleep(t)
        self.setFaceValue(num)      
        sense.show_letter("{}".format(self.__faceValue))
        """
        """
        shakingIntervalCount=1
        while True:
            acceleration = sense.get_accelerometer_raw()
            x = acceleration['x']
            y = acceleration['y']
            z = acceleration['z']

            x = abs(x)
            y = abs(y)
            z = abs(z)

            sleep(2)
            if x > 1 or y > 1 or z > 1:
                sense.clear(255,255,0)
            else:
                self.setFaceValue(randint(1,6))
                print(self.__faceValue)
                sense.show_letter("{}".format(self.__faceValue))
            



        newOrienTuple=modules.getCurrentOrientationTuple()
        while self.__initOrienTuple!=newOrienTuple:
            sense.clear(255,255,0)
            self.__faceValue=randint(1,6)
            self.__initOrienTuple=newOrienTuple
            newOrienTuple=modules.getCurrentOrientationTuple()
            print(self.__faceValue)
            sense.show_letter("{}".format(self.__faceValue))
            sense.stick.direction_any=break
            
"""