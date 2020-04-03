
from MyClasses.Color import Color
from MyClasses.Emoji import Emoji
from time import sleep
from sense_hat import SenseHat

sense=SenseHat()
color=Color()
noColor=color.getNoColorColor()
red=color.getRedColor()
green=color.getGreenColor()
blue=color.getBlueColor()

#Naming convention for the image array:
#'b' is the background colour
#'o' is the outline colour
#'f' is the fill-in colour
happyEmoji=Emoji([
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', 'o', 'o', 'f', 'f', 'o', 'o', 'b'],
    ['b', 'o', 'o', 'f', 'f', 'o', 'o', 'b'],
    ['b', 'f', 'f', 'f', 'f', 'f', 'f', 'b'],
    ['b', 'o', 'f', 'f', 'f', 'f', 'o', 'b'],
    ['b', 'o', 'o', 'o', 'o', 'o', 'o', 'b'],
    ['b', 'f', 'o', 'o', 'o', 'o', 'f', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
], red, green, blue)

sadEmoji=Emoji([
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', 'o', 'o', 'f', 'f', 'o', 'o', 'b'],
    ['b', 'o', 'o', 'f', 'f', 'o', 'o', 'b'],
    ['b', 'f', 'f', 'f', 'f', 'f', 'f', 'b'],
    ['b', 'f', 'o', 'o', 'o', 'o', 'f', 'b'],
    ['b', 'o', 'o', 'o', 'o', 'o', 'o', 'b'],
    ['b', 'o', 'f', 'f', 'f', 'f', 'o', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
],red,green,blue)

purplexedEmoji=Emoji([
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', 'o', 'o', 'f', 'f', 'o', 'o', 'b'],
    ['b', 'o', 'o', 'f', 'f', 'o', 'o', 'b'],
    ['b', 'f', 'f', 'f', 'f', 'f', 'f', 'b'],
    ['b', 'o', 'o', 'o', 'o', 'o', 'o', 'b'],
    ['b', 'o', 'o', 'o', 'o', 'o', 'o', 'b'],
    ['b', 'f', 'f', 'f', 'f', 'f', 'f', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
],red,green,blue)

emojis=[happyEmoji,sadEmoji,purplexedEmoji]

#creates different emojis at an interval of 3 sec 
#untill a keyboard external break cmd is not given
joystick_used=False
while not joystick_used:
    joystick_event_list = sense.stick.get_events()
    if (len(joystick_event_list)) is not 0:
        joystick_used = True   
        sense.clear(0,0,0)
    else:
        for emoji in range(len(emojis)):   
            emojis[emoji].drawEmoji()
            sleep(3)


   