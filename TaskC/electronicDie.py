from sense_hat import SenseHat
from time import sleep
import random
from MyModules import modules

sense=SenseHat()
sense.clear(0,0,0)
initOrienTuple=modules.getCurrentOrientationTuple()
dieValue=random.randint(1,6)

while True:
    newOrienTuple=modules.getCurrentOrientationTuple()
    
    #if die is shaking
    if initOrienTuple!=newOrienTuple:
        sense.clear(255,255,0)
        dieValue=random.randint(1,6)
    else:  #when die is shaken
        #sense.set_rotation(modules.getRotation())
        sense.clear(0,0,0)
        sense.show_letter("{}".format(dieValue))
    initOrienTuple=newOrienTuple
