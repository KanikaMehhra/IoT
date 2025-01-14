# Reference: https://raspberrypi.stackexchange.com/questions/61524/how-to-approximate-room-temperature-in-a-better-way
from sense_hat import SenseHat
import os

sense = SenseHat()

class Calibration:
    def __init__(self):
        self.__t = None
        
# Get CPU temperature.
    def get_cpu_temp(self):
        res = os.popen("vcgencmd measure_temp").readline()
        return float(res.replace("temp=","").replace("'C\n",""))

# Use moving average to smooth readings.
    def get_smooth(self, x):
        if not hasattr(self.get_smooth, "t"):
            self.__t = [x,x,x]
    
        self.__t[2] = self.__t[1]
        self.__t[1] = self.__t[0]
        self.__t[0] = x

        return (self.__t[0] + self.__t[1] + self.__t[2]) / 3

    def get_calibrated_temp(self):
        t_corr = 0.0
        for x in range(10):
            t1 = sense.get_temperature_from_humidity()
            t2 = sense.get_temperature_from_pressure()
            t_cpu = self.get_cpu_temp()

            t = (t1 + t2) / 2
            t_corr = t - ((t_cpu - t) / 1.5)
            t_corr = self.get_smooth(t_corr)
            x += 1
            
        return t_corr


