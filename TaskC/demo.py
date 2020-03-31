from sense_hat import SenseHat
sense=SenseHat()
sense.clear(255,0,0)

while True:
    if sense.stick.direction_down:
        print("K")
        break
