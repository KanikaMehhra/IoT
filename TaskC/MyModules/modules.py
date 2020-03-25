from sense_hat import SenseHat
sense=SenseHat()

def getRotation():
    acc=sense.get_accelerometer_raw()
    x=round(acc['x'])
    y=round(acc['y'])

    if x==1:
        return 270
    elif x==-1:
        return 90
    elif y==-1:
        return 180
    else:
        return 0

        
def getCurrentOrientationTuple():
    orientation=sense.get_orientation()
    roll=abs(round(orientation["roll"]))
    pitch=abs(round(orientation["pitch"]))
    yaw=abs(round(orientation["yaw"]))

    return (roll, pitch, yaw)