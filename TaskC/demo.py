from sense_hat import SenseHat
sense=SenseHat()
sense.clear(255,0,0)

event = sense.stick.wait_for_event()
def action(event):
    sense.show_message("{}".format(event))

action(event)

def action(event):
    sense.show_message("{}".format(event))
