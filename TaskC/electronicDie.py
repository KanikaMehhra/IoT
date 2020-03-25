from sense_hat import SenseHat
from MyClasses.Shake import Shake
from time import sleep
import random

sense=SenseHat()
sense.clear(0,0,0)
initialOrientation=Shake()
initOrienTuple=initialOrientation.getCurrentOrientationTuple()
dieValue=random.randint(1,6)

while True:
    newOrientation=Shake()
    newOrienTuple=newOrientation.getCurrentOrientationTuple()
    
    #if die is shaking
    if initOrienTuple!=newOrienTuple:
        sense.clear(255,255,0)
        dieValue=random.randint(1,6)
    else:  #when die is shaken
        sense.clear(0,0,0)
        sense.show_letter("{}".format(dieValue))
    initOrienTuple=newOrienTuple
