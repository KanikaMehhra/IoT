from sense_hat import SenseHat
from time import sleep
import random

sense=SenseHat()
sense.clear()
acc=sense.get_orientation()
initRoll=abs(round((acc['roll'])))
initpitch=abs(round(acc['pitch']))
inityaw=abs(round(acc['yaw']))

while True:
    acc=sense.get_orientation()
    newRoll=abs(round((acc['roll'])))
    newpitch=abs(round(acc['pitch']))
    newyaw=abs(round(acc['yaw']))

    if initRoll!=newRoll and initpitch!=newpitch and inityaw!=newyaw:
        sense.show_message("!")
    else:
        sense.clear(0,0,0)
    initRoll=newRoll
    initpitch=newpitch
    inityaw=newyaw
