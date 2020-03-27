from time import sleep

from sense_hat import SenseHat

from calibration import Calibration
from dataInput import DataInput
#reference for import of parent directory: https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369
import os,sys,inspect
current = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent = os.path.dirname(current)
sys.path.insert(0, parent) 
import constants

sense = SenseHat()
calib = Calibration()

data = DataInput('TaskB/config.json').getData()
cold_max = data['cold_max'] 
comfortable_min = data['comfortable_min'] 
comfortable_max = data['comfortable_max'] 
hot_min = data['hot_min'] 

while True:
    temp = calib.get_calibrated_temp()

    if temp <= cold_max:
        sense.show_message(str("%.1fC" % temp), text_colour=constants.RED)
    elif temp > comfortable_min and temp < comfortable_max:
        sense.show_message(str("%.1fC" % temp), text_colour =constants.GREEN)
    elif temp >= hot_min:
        sense.show_message(str("%.1fC" % temp), text_colour = constants.RED) 
    
    sleep(10)
    sense.clear()