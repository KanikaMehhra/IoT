from time import sleep
from sense_hat import SenseHat
from calibration import Calibration
from dataInput import DataInput
#reference for import of parent directory: https://gist.github.com/JungeAlexander/6ce0a5213f3af56d7369
import os,sys,inspect
current = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent = os.path.dirname(current)
sys.path.insert(0, parent) 

sense = SenseHat()
RED=(255,0,0)

class MonitorAndDisplay: 
    def __init__(self):
        self.__calib = Calibration()

    def initData(self, file):
        try:
            self.__data = DataInput(file).getData()
        except FileNotFoundError:
            sense.show_message("Sorry, missing a config file", text_colour=RED)
            print("Configuration file not found, closing program...")
            sense.clear()
            sys.exit()

        self.__cold_max = self.__data['cold_max'] 
        self.__comfortable_min = self.__data['comfortable_min'] 
        self.__comfortable_max = self.__data['comfortable_max'] 
        self.__hot_min = self.__data['hot_min'] 

    def runTemp(self):
        self.initData('config.json')

        while True:
            temp = self.__calib.get_calibrated_temp()

            if temp <= self.__cold_max:
                sense.show_message(str("%.1fC" % temp), text_colour=constants.RED)
            elif temp > self.__comfortable_min and temp < self.__comfortable_max:
                sense.show_message(str("%.1fC" % temp), text_colour =constants.GREEN)
            elif temp >= self.__hot_min:
                sense.show_message(str("%.1fC" % temp), text_colour = constants.RED) 
    
            sleep(10)
            sense.clear()