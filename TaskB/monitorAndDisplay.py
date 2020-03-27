from time import sleep

from sense_hat import SenseHat

from calibration import Calibration
from dataInput import DataInput

sense = SenseHat()
calib = Calibration()

data = DataInput('config.json').getData()
cold_max = data['cold_max'] 
comfortable_min = data['comfortable_min'] 
comfortable_max = data['comfortable_max'] 
hot_min = data['hot_min'] 

while True:
    temp = calib.get_calibrated_temp()

    if temp <= cold_max:
        sense.show_message(str("%.1fC" % temp), text_colour=(0, 0, 255))
    elif temp > comfortable_min and temp < comfortable_max:
        sense.show_message(str("%.1fC" % temp), text_colour =(0, 255, 0))
    elif temp >= hot_min:
        sense.show_message(str("%.1fC" % temp), text_colour = (255, 0, 0)) 
    
    sleep(10)
    sense.clear()